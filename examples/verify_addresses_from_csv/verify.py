# usage:
#     python verify.py input.csv
#     logs output in csv directory

import csv
import datetime
import lob
import os
import sys

sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

# TODO: Provide your API key, keep this secure
lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

# Input check
if len(sys.argv) < 2:
    print("Please provide an input CSV file as an argument.")
    print("usage: python verify.py <CSV_FILE>")
    sys.exit(1)

input_filename = sys.argv[1]

success_csv_fields = [
    'address_line1',
    'address_line2',
    'address_city',
    'address_state',
    'address_zip'
]
errors_csv_fields = ['error']

#create the output directory,
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

try:
    with open(input_filename, 'r') as input, \
         open(success_filename, 'w') as success, \
         open(errors_filename, 'w') as errors:

    # print mode to screen

        input_csv = csv.DictReader(input)
        errors_csv_fields += input_csv.fieldnames

        success_csv = csv.DictWriter(success, fieldnames=success_csv_fields)
        errors_csv = csv.DictWriter(errors, fieldnames=errors_csv_fields)

        err_count = 0

        # Loop through input CSV rows
        for idx, row in enumerate(input_csv):
            # Create letter from row
            try:
                verifiedAddress = lob.Verification.create(
                    address_line1=row['address1'],
                    address_line2=row['address2'],
                    address_city=row['city'],
                    address_state=row['state'],
                    address_zip=row['postcode'],
                    address_country='US'
                )
            except Exception as e:
                error_row = {'error': e}
                error_row.update(row)
                errors_csv.writerow(error_row)
                err_count += 1
                sys.stdout.write('E')
                sys.stdout.flush()
            else:
                success_csv.writerow({
                    'address_line1': verifiedAddress.address.address_line1,
                    'address_line2': verifiedAddress.address.address_line2,
                    'address_city':  verifiedAddress.address.address_city,
                    'address_state': verifiedAddress.address.address_state,
                    'address_zip':   verifiedAddress.address.address_zip
                })

                # Print success
                sys.stdout.write('.')
                sys.stdout.flush()

            # New lines for larger csv's
            if idx % 10 is 9:
                sys.stdout.write('\n')
                sys.stdout.flush()

except Exception as e:
    print('Error: ' + str(e))
    sys.exit(1)

print('')
print('Done with ' + (str(err_count) if err_count else 'no') + ' errors.')
print('Results written to ' + str(output_dir) + '.')
