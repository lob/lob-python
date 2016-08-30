# Usage
# python letter.py input.csv
import sys,os
sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

import lob
import csv
import datetime

lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

skipFirstLine  = True

# Column indices in CSV
name          = 0
amount        = 1
address_line1 = 2
address_line2 = 3
address_city  = 4
address_state = 5
address_zip   = 6
country       = 'US'

try:
  sys.argv[1]
except IndexError:
  print "Please provide an input CSV file as an argument."
  sys.exit()

# Open input files
inputFile = open(sys.argv[1], 'rU')
csvInput = csv.reader(inputFile)

# Create output files
errors = open(os.path.dirname(os.path.abspath(__file__)) + '/errors.csv', 'w')
success = open(os.path.dirname(os.path.abspath(__file__)) + '/success.csv', 'w')

# Loop through input CSV rows
for idx, row in enumerate(csvInput):
  if skipFirstLine and idx == 0:
    continue

  # Create letter for verified addresses
  try:
    createdLetter = lob.Letter.create(
      description = 'Bill for ' + row[name],
      metadata = {
          'campaign': 'billing_statements',
          'csv': inputFile.name
      },
      to_address = {
          'name': row[name],
          'address_line1': row[address_line1],
          'address_line2': row[address_line2],
          'address_city': row[address_city],
          'address_zip': row[address_zip],
          'address_state': row[address_state],
      },
      from_address = {
          'name': 'Your Name/Company',
          'address_line1': '123 Test Avenue',
          'address_city': 'San Francisco',
          'address_state': 'CA',
          'address_zip': '94107',
      },
      file = open(os.path.dirname(os.path.abspath(__file__)) + '/letter.html', 'r').read(),
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
success.close()
print "\n"
