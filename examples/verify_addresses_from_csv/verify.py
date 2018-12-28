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
lob.api_key = 'YOUR_API_KEY'

# Input check
if len(sys.argv) < 2:
    print("Please provide an input CSV file as an argument.")
    print("usage: python verify.py <CSV_FILE>")
    sys.exit(1)

input_filename = sys.argv[1]

verifications_csv_fields = [
    'primary_line',
    'secondary_line',
    'urbanization',
    'last_line',
    'deliverability'
]

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
verifications_filename = os.path.join(output_dir, 'verifications.csv')

try:
    with open(input_filename, 'r') as input, \
         open(verifications_filename, 'w') as verifications:

        input_csv = csv.DictReader(input)

        verifications_csv = csv.DictWriter(verifications, fieldnames=verifications_csv_fields)
        verifications_csv.writeheader()

        for idx, row in enumerate(input_csv):
            verifiedAddress = lob.USVerification.create(
                primary_line=row['primary_line'],
                secondary_line=row['secondary_line'],
                city=row['city'],
                state=row['state'],
                zip_code=row['zip_code'],
            )

            verifications_csv.writerow({
                'primary_line': verifiedAddress.primary_line,
                'secondary_line': verifiedAddress.secondary_line,
                'urbanization':  verifiedAddress.urbanization,
                'last_line':  verifiedAddress.last_line,
                'deliverability': verifiedAddress.deliverability
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
print('Results written to ' + str(output_dir) + '.')
