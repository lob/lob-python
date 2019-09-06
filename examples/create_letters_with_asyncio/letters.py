"""
Letter Creation example using Pythons asyncio

This example bypasses the lob Python library and instead uses asyncio
to create letters, attempting to saturate the rate limit. It requires
Python 3.7 or later.

To customize:

* set API_KEY and API_BASE as needed; these may be set in the Python
  code or via environment variables
* update getPayload to map an input row to the letter create payload
* update from_address as needed

These customziation points are marked with `TODO` comments in the code.

"""

import asyncio
import csv
import datetime
import functools
import os
import sys
import time

import aiohttp
import lob


# TODO: set your API key
API_KEY = lob.api_key = os.getenv('API_KEY')
API_BASE = lob.api_base = os.getenv('API_BASE', 'https://api.lob.com/v1')

DEBUG = False

SUCCESS_LOG_FIELDS = [
    'name',
    'id',
    'url',
    'address_line1',
    'address_line2',
    'address_city',
    'address_state',
    'address_zip'
]
ERROR_LOG_FIELDS = ['error', 'status']
WORKERS = 100

def logFiles():
    """Create an output directory for log files and return the filenames.

    Returns (success_filename, error_filename)
    """
    # create the output directory,
    output_dir = os.path.join('.',  'output')
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    try:
        output_dir = os.path.join(output_dir, timestamp)
        os.mkdir(output_dir)
    except Exception as e:
        print('Error: ' + str(e))
        print('Failed to create output directory. Aborting all sends.')
        raise e

    # output csv names
    success_filename = os.path.join(output_dir, 'success.csv')
    errors_filename = os.path.join(output_dir, 'errors.csv')

    return (success_filename, errors_filename)


async def logSuccess(successLog, letter):
    """Logs a successful letter send to successLog.

    `successLog` is a CSV writer and `letter` is a dict.
    """
    successLog.writerow({
        'name':          letter['to']['name'],
        'id':            letter['id'],
        'url':           letter['url'],
        'address_line1': letter['to']['address_line1'],
        'address_line2': letter['to']['address_line2'],
        'address_city':  letter['to']['address_city'],
        'address_state': letter['to']['address_state'],
        'address_zip':   letter['to']['address_zip'],
    })

    sys.stdout.write('.')
    sys.stdout.flush()


async def logError(errorLog, resp):
    if isinstance(resp, Exception):
        errorLog.writerow(
            {'error': resp},
        )
    else:
        errorLog.writerow(
            {'error': await resp.json(), 'status': resp.status},
        )

    sys.stdout.write('E')
    sys.stdout.flush()


# TODO: customize getPayload based on your input file
def getPayload(row):
    """Return a create letter payload for the inputRow.

    inputRow is a dict read from the input CSV.

    This *must* return a dict suitable for serializing as a JSON letter
    create request.
    """

    payload = dict(
        description='Bill for ' + row['name'],
        metadata=dict(
            **row.get('metadata', {}),
        ),
        to={
            'name':          row['name'],
            'address_line1': row['address1'],
            'address_line2': row['address2'],
            'address_city':  row['city'],
            'address_zip':   row['postcode'],
            'address_state': row['state']
        },
        file=row['file'],
        merge_variables={
            'date':   datetime.datetime.now().strftime("%m/%d/%Y"),
            'name':   row['name'],
            'amount': row['amount']
        },
        color=True,
    )
    payload['from'] = row['from_address']

    return payload


async def sendWorker(session, queue, getPayload, underRateLimit, successLog, errorLog):
    """asyncio worker for processing letters from the queue.

    session is the aiohttp session used to send requests.

    queue is an asyncio.Queue, from which letters are read.

    getPayload is a function which takes a row from the queue and returns
    the create letter payload.

    underRateLimit is an asyncio Event object, which is triggered when it's
    safe to send.

    successLog and errorLog are CSV writers used for logging results.
    """

    url = '%s/letters' % API_BASE

    # get the first letter to operate on
    row = await queue.get()

    while True:
        # wait until we're under the rate limit
        await underRateLimit.wait()

        # send the request
        payload = None
        try:
            payload = getPayload(row)
        except Exception as e:
            await logError(errorLog, e)

        if payload is not None:
            async with session.post(url, json=payload) as resp:
                if resp.status == 200:
                    # if successful, mark the task done and wait for another letter
                    letter = await resp.json()
                    await logSuccess(successLog, letter)

                elif resp.status == 429:
                    # if rate limited, set flag, sleep for delay, clear flag, repeat the loop
                    resetTime = float(resp.headers.get('X-Rate-Limit-Reset'))
                    delay = abs(resetTime - time.time())
                    sys.stdout.write('W')
                    sys.stdout.flush()

                    # block work by other workers, wait, and then set the "all clear" flag
                    underRateLimit.clear()
                    await asyncio.sleep(delay)
                    underRateLimit.set()

                    # continue without fetching another letter to work on
                    continue

                else:
                    # report an error and mark the task as done
                    await logError(errorLog, resp)

        queue.task_done()
        row = await queue.get()


async def send_letters(inputCSV, *, getPayload=getPayload, extraData=None):
    extraData = extraData or {}
    successes, errors = logFiles()

    with open(successes, 'w') as success, \
        open(errors, 'w') as error:

        # Print mode to screen
        mode = API_KEY.split('_')[0]
        print('Sending letters in ' + mode.upper() + ' mode.')

        # create success and error logs
        success_csv = csv.DictWriter(success, fieldnames=SUCCESS_LOG_FIELDS)
        errors_csv = csv.DictWriter(error, fieldnames=ERROR_LOG_FIELDS)
        success_csv.writeheader()
        errors_csv.writeheader()

        # create the Event used to signal the rate limit has been reached
        underRateLimit = asyncio.Event()
        underRateLimit.set()

        # create a queue to hold the Tasks for each Letter
        letters = asyncio.Queue()

        # Create worker tasks to process the queue concurrently
        async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(API_KEY),
        ) as session:
            tasks = []
            for i in range(WORKERS):
                tasks.append(
                    asyncio.create_task(
                        sendWorker(session, letters, getPayload, underRateLimit, success_csv, errors_csv)
                    )
                )

            # add the letters to the queue
            for letter in inputCSV:
                letter.update(extraData)
                await letters.put(letter)

            # wait for all letters to complete
            await letters.join()

            # Cancel our worker tasks.
            for task in tasks:
                task.cancel()

            # Wait until all worker tasks are cancelled.
            await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    # TODO: Create your from_address
    try:
        from_address = lob.Address.create(
            name='Your Name',
            company='Your Company',
            address_line1='123 Test Avenue',
            address_line2='STE 456',
            address_city='San Francisco',
            address_state='CA',
            address_zip='94107'
        )
    except Exception as e:
        print('Error: ' + str(e))
        print('Failed to create from_address.')
        sys.exit(1)


    with open('letter.html', 'r') as html_file:
        letter_html = html_file.read()

    with open(sys.argv[-1], 'r') as inputFile:
        # TODO: customize `extraData` if you need additional information to
        # generate the create letter payload in `getPayload`
        #
        # extraData is added to every row from the input CSV, providing a channel
        # to pass additional values into getPayload
        extraData = dict(
            metadata=dict(csv=sys.argv[-1]),
            from_address=from_address.id,
            file=letter_html,
        )

        input_csv = csv.DictReader(inputFile)
        asyncio.run(send_letters(input_csv, extraData=extraData), debug=DEBUG)
