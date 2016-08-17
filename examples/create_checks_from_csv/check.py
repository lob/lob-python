# Usage
# python check.py input.csv
import sys,os
sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

import lob
import csv

lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b' # TODO Replace with your API key

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

# Creating a Bank Account using the previously created account_address

bankAccount = lob.BankAccount.create(
    description = 'Example bank account',
    routing_number = '122100024',
    account_number = '1234564789',
    account_type = 'company',
    signatory = 'John Doe'
)

# Verifying a Bank Account with the microdeposit amounts

example_bank_account = lob.BankAccount.verify(
    id = bankAccount.id,
    amounts = [23, 77]
)

# Loop through input CSV rows
for idx, row in enumerate(csvInput):
  if skipFirstLine and idx == 0:
    continue

  # Create letter for verified addresses
  try:
    createdCheck = lob.Check.create(
      description = 'Check for ' + row[name],
      metadata = {
          'campaign': 'Bill pay',
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
      bank_account = bankAccount,
      amount = row[amount],
      memo = 'Service payment',
      check_bottom = open(os.path.dirname(os.path.abspath(__file__)) + '/check.html', 'r').read(),
      data = {
          'name': row[name],
      },
      logo = 'https://s3-us-west-2.amazonaws.com/lob-assets/lob_check_logo.png'
    )
  except Exception, e:
    print "Error: " + str(e) + " in " + str(row)
  else:
    outputRow = createdCheck.id + ","
    outputRow += createdCheck.url + ","
    outputRow += row[name] + ","
    outputRow += row[amount] + ","
    outputRow += (createdCheck.to_address.address_line1 if createdCheck.to_address.address_line1 != None else " ") + ","
    outputRow += (createdCheck.to_address.address_line2 if createdCheck.to_address.address_line2 != None else " ") + ","
    outputRow += (createdCheck.to_address.address_city  if createdCheck.to_address.address_city  != None else " ") + ","
    outputRow += (createdCheck.to_address.address_state if createdCheck.to_address.address_state != None else " ") + ","
    outputRow += (createdCheck.to_address.address_zip   if createdCheck.to_address.address_zip   != None else " ") + "\n"
    success.write(outputRow)


errors.close()
success.close()
print "\n"
