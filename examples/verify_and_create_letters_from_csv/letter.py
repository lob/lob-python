# Usage
# python verify.py input.csv
import sys,os
sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

import lob
import csv
import datetime

lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

skipFirstLine  = True

# Column indices in CSV
name      = 0
amount    = 1
address1  = 2;
address2  = 3;
city      = 4;
state     = 5;
postcode  = 6;
country   = 'US'

try:
  sys.argv[1]
except IndexError:
  print "Please provide an input CSV file as an argument."
  sys.exit()

# Open input files
inputFile = open(sys.argv[1], 'rU')
csvInput = csv.reader(inputFile)

# Create output files
errors = open('errors.csv', 'w')
verified = open('verified.csv', 'w')
success = open('success.csv', 'w')

# Loop through input CSV rows
for idx, row in enumerate(csvInput):
  if skipFirstLine and idx == 0:
    continue

  # Sanity check
  sys.stdout.write('.')
  sys.stdout.flush()

  # Verify addresses
  try:
    verifiedAddress = lob.Verification.create(
      address_line1 = row[address1],
      address_line2 = row[address2],
      address_city = row[city],
      address_state = row[state],
      address_zip = row[postcode],
      address_country = country
    )
  except Exception, e:
    outputRow = ",".join(row) + "," + str(e)+ "\n"
    errors.write(outputRow)
  else:
    outputRow  = row[name] + ","
    outputRow += row[amount] + ","
    outputRow += verifiedAddress.address.address_line1 + ","
    outputRow += verifiedAddress.address.address_line2 + ","
    outputRow += verifiedAddress.address.address_city + ","
    outputRow += verifiedAddress.address.address_state + ","
    outputRow += verifiedAddress.address.address_zip + "\n"
    verified.write(outputRow)

    # Create letter for verified addresses
    try:
      createdLetter = lob.Letter.create(
          description = 'Bill for ' + row[name],
          metadata = {
              'campaign': 'billing_statements'
          },
          to_address = {
              'name': row[name],
              'address_line1': verifiedAddress.address.address_line1,
              'address_city': verifiedAddress.address.address_city,
              'address_zip': verifiedAddress.address.address_zip,
              'address_state': verifiedAddress.address.address_state,
          },
          from_address = {
              'name': 'Your Name/Company',
              'address_line1': '123 Test Avenue',
              'address_city': 'San Francisco',
              'address_state': 'CA',
              'address_zip': '94107',
          },
          file = open('letter_template.html', 'r').read(),
          data = {
              'date': datetime.datetime.now().strftime("%m/%d/%Y"),
              'name': row[name],
              'amountDue': row[amount]
          },
          color = True
      )
    except Exception, e:
      print "Error: " + str(e) + " in " + str(row)
    else:
      outputRow = createdLetter.id + ","
      outputRow += createdLetter.url + ","
      outputRow += row[name] + ","
      outputRow += row[amount] + ","
      outputRow += (createdLetter.to_address.address_line1 if createdLetter.to_address.address_line1 != None else " ") + ","
      outputRow += (createdLetter.to_address.address_line2 if createdLetter.to_address.address_line2 != None else " ") + ","
      outputRow += (createdLetter.to_address.address_city  if createdLetter.to_address.address_city  != None else " ") + ","
      outputRow += (createdLetter.to_address.address_state if createdLetter.to_address.address_state != None else " ") + ","
      outputRow += (createdLetter.to_address.address_zip   if createdLetter.to_address.address_zip   != None else " ") + "\n"
      success.write(outputRow)


errors.close()
verified.close()
success.close()
print "\n"

