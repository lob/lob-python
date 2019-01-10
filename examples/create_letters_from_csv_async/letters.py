from __future__ import print_function
# usage:
#   python letters.py input.csv
#   logs to csv's in the output directory
#

import sys
try:
    import concurrent.futures
except ImportError:
    print("""This script requires concurrent.futures;
    run with Python 3.2 or later, or install the backport.

    https://pypi.org/project/futures/
    """)
    sys.exit(1)

import csv
import datetime
import os

import lob

MAX_CONCURRENCY = 5
sys.path.insert(0, os.path.abspath(__file__+'../../..'))

###########################################################
# TODO: Provide your API Key, keep this secure
lob.api_key = ''

if not lob.api_key:
    print("Please set your API key in", __file__)
    sys.exit(1)

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

###########################################################

# Input check
if len(sys.argv) < 2:
    print("Please provide an input CSV file as an argument.")
    print("usage: python letter.py <CSV_FILE>")
    sys.exit(1)

input_filename = sys.argv[1]

success_csv_fields = [
    'name',
    'id',
    'url',
    'address_line1',
    'address_line2',
    'address_city',
    'address_state',
    'address_zip'
]

errors_csv_fields = ['error']

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
    sys.exit(1)

# output csv names
success_filename = os.path.join(output_dir, 'success.csv')
errors_filename = os.path.join(output_dir, 'errors.csv')

with open('letter.html', 'r') as html_file:
    letter_html = html_file.read()


with open(input_filename, 'r') as input, \
        open(success_filename, 'w') as success, \
        open(errors_filename, 'w') as errors, \
        concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:

    # Print mode to screen
    mode = lob.api_key.split('_')[0]
    print('Sending letters in ' + mode.upper() + ' mode.')

    input_csv = csv.DictReader(input)

    success_csv = csv.DictWriter(success, fieldnames=success_csv_fields)
    errors_csv = csv.DictWriter(errors, fieldnames=errors_csv_fields)
    success_csv.writeheader()
    errors_csv.writeheader()

    err_count = 0

    # Loop through input CSV rows
    futures_to_indices = {}
    for i, row in enumerate(input_csv):
        futures_to_indices[
            executor.submit(lob.Letter.create,
                description='Bill for ' + row['name'],
                metadata={
                    'campaign': 'billing_statements',
                    'csv':      input_filename
                },
                to_address={
                    'name':          row['name'],
                    'address_line1': row['address1'],
                    'address_line2': row['address2'],
                    'address_city':  row['city'],
                    'address_zip':   row['postcode'],
                    'address_state': row['state']
                },
                from_address=from_address.id,
                file=letter_html,
                merge_variables={
                    'date':   datetime.datetime.now().strftime("%m/%d/%Y"),
                    'name':   row['name'],
                    'amount': row['amount']
                },
                color=True,
            )] = i

    for future in concurrent.futures.as_completed(futures_to_indices):
        index = futures_to_indices[future]
        try:
            # future.result() will return the result of the call to
            # lob.Letters.create. If the call raised, result() will
            # raise the same exception.
            letter = future.result()

            # finished successfully
            success_csv.writerow({
                'name':          letter.to_address.name,
                'id':            letter.id,
                'url':           letter.url,
                'address_line1': letter.to_address.address_line1,
                'address_line2': letter.to_address.address_line2,
                'address_city':  letter.to_address.address_city,
                'address_state': letter.to_address.address_state,
                'address_zip':   letter.to_address.address_zip
            })
            sys.stdout.write('.')
            sys.stdout.flush()
        except Exception as e:
            # an error occured
            error_row = {'error': e}
            errors_csv.writerow(error_row)
            err_count += 1
            sys.stdout.write('E')
            sys.stdout.flush()


print('')
print('Done with ' + (str(err_count) if err_count else 'no') + ' errors.')
print('Results written to ' + str(output_dir) + '.')
