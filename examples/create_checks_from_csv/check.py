from __future__ import print_function

# usage:
#   python check.py input.csv
#   logs to csv's in the output directory

import csv
import datetime
import os
import sys

# Load lob-python root directory into the import path so you can use the lob package without having to install it through pip.
sys.path.insert(0, os.path.abspath(__file__+'../../..'))
import lob

###########################################################
# TODO: Provide your API Key, keep this secure
lob.api_key = 'YOUR_API_KEY'

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

# TODO: Create and verify your bank account
try:
    bank_account = lob.BankAccount.create(
        description='Your Bank Account',
        routing_number='122100024',
        account_number='0123456478',
        account_type='company',
        signatory='John Hancock'
    )
except Exception as e:
    print('Error: ' + str(e))
    print('Failed to create bank account')
    sys.exit(1)

try:
    example_bank_account = lob.BankAccount.verify(
        id=bank_account.id,
        amounts=[23, 77]
    )
except Exception as e:
    print('Error: ' + str(e))
    print('Failed to verify bank account.')

# TODO: Add a logo to your check
CHECK_LOGO = 'https://s3-us-west-2.amazonaws.com/public.lob.com/assets/check_logo.png'

###########################################################

# Input check
if len(sys.argv) < 2:
    print("Please provide an input CSV file as an argument.")
    print("usage: python check.py <CSV_FILE>")
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

with open('check.html', 'r') as html_file:
    check_html = html_file.read()

try:
    with open(input_filename, 'r') as input, \
            open(success_filename, 'w') as success, \
            open(errors_filename, 'w') as errors:

        # Print mode to screen
        mode = lob.api_key.split('_')[0]
        print('Sending checks in ' + mode.upper() + ' mode.')

        input_csv = csv.DictReader(input)
        errors_csv_fields += input_csv.fieldnames

        success_csv = csv.DictWriter(success, fieldnames=success_csv_fields)
        errors_csv = csv.DictWriter(errors, fieldnames=errors_csv_fields)
        success_csv.writeheader()
        errors_csv.writeheader()

        err_count = 0
        # Loop through input CSV rows
        for idx, row in enumerate(input_csv):
            # Create checks from row
            try:
                check = lob.Check.create(
                    description='Check for ' + row['name'],
                    metadata={
                        'csv': input_filename
                    },
                    to_address={
                        'name':          row['name'],
                        'address_line1': row['address_line1'],
                        'address_line2': row['address_line2'],
                        'address_city':  row['address_city'],
                        'address_zip':   row['address_zip'],
                        'address_state': row['address_state']
                    },
                    from_address=from_address,
                    bank_account=bank_account,
                    amount=row['amount'],
                    memo='Service payment',
                    check_bottom=check_html,
                    merge_variables={
                        'name': row['name'],
                    },
                    logo=CHECK_LOGO
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
                    'name':          check.to_address.name,
                    'id':            check.id,
                    'url':           check.url,
                    'address_line1': check.to_address.address_line1,
                    'address_line2': check.to_address.address_line2,
                    'address_city':  check.to_address.address_city,
                    'address_state': check.to_address.address_state,
                    'address_zip':   check.to_address.address_zip
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
