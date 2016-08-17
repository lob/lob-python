# usage:
#   python postcard.py input.csv
#   logs to csv's in the output directory

import csv
import datetime
import lob
import os
import sys

sys.path.insert(0, os.path.abspath(__file__+'../../..'))

###########################################################
# TODO: Provide your API Key, keep this secure
lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

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
except Exception, e:
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
except Exception, e:
    print('Error: ' + str(e))
    print('Failed to create output directory. Aborting all sends.')
    sys.exit(1)

# output csv names
success_filename = os.path.join(output_dir, 'success.csv')
errors_filename = os.path.join(output_dir, 'errors.csv')

with open('postcard_front.html', 'r') as front_file,\
     open('postcard_back.html', 'r') as back_file:
    front_html = front_file.read()
    back_html = back_file.read()

try:
    with open(input_filename, 'r') as input, \
         open(success_filename, 'w') as success, \
         open(errors_filename, 'w') as errors:

        # Print mode to screen
        mode = lob.api_key.split('_')[0]
        print('Sending postcards in ' + mode.upper() + ' mode.')

        input_csv = csv.DictReader(input)
        errors_csv_fields += input_csv.fieldnames

        success_csv = csv.DictWriter(success, fieldnames=success_csv_fields)
        errors_csv = csv.DictWriter(errors, fieldnames=errors_csv_fields)

        err_count = 0

        # Loop through input CSV rows
        for idx, row in enumerate(input_csv):
            # Create postcard from row
            try:
                postcard = lob.Postcard.create(
                    to_address={
                        'name':            row['name'],
                        'address_line1':   row['address_line1'],
                        'address_line2':   row['address_line2'],
                        'address_city':    row['address_city'],
                        'address_state':   row['address_state'],
                        'address_zip':     row['address_zip'],
                        'address_country': row['address_country']
                    },
                    from_address=from_address,
                    size='6x11',
                    front=front_html,
                    back=back_html,
                    data={
                        'background_image': row['background_image'],
                        'background_color': row['background_color'],
                        'name':             row['name'],
                        'car':              row['car'],
                        'mileage':          row['mileage']
                    }
                )
            except Exception, e:
                error_row = {'error': e}
                error_row.update(row)
                errors_csv.writerow(error_row)
                err_count += 1
                sys.stdout.write('E')
                sys.stdout.flush()
            else:
                success_csv.writerow({
                    'name':          postcard.to_address.name,
                    'id':            postcard.id,
                    'url':           postcard.url,
                    'address_line1': postcard.to_address.address_line1,
                    'address_line2': postcard.to_address.address_line2,
                    'address_city':  postcard.to_address.address_city,
                    'address_state': postcard.to_address.address_state,
                    'address_zip':   postcard.to_address.address_zip
                })

                # Print success
                sys.stdout.write('.')
                sys.stdout.flush()

            # New lines for larger csv's
            if idx % 10 is 9:
                sys.stdout.write('\n')
                sys.stdout.flush()

except Exception, e:
    print('Error: ' + str(e))
    sys.exit(1)

print('')
print('Done with ' + (str(err_count) if err_count else 'no') + ' errors.')
print('Results written to ' + str(output_dir) + '.')
