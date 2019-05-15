from __future__ import print_function

import sys
import os

# Load lob-python root directory into the import path so you can use the lob package without having to install it through pip.
sys.path.insert(0, os.path.abspath(__file__+'../../..'))
import lob

# Replace this API key with your own.
lob.api_key = 'YOUR_API_KEY'

# Creating an Address Object

example_address = lob.Address.create(
    name='Joe Smith',
    description='Joe - Home',
    metadata={
        'group': 'Members'
    },
    address_line1='104, Printing Boulevard',
    address_city='Boston',
    address_state='MA',
    address_country='US',
    address_zip='12345'
)

print("\n")
print("Address Response")
print("\n")
print("=======================================================")
print("\n")
print(example_address)
print("\n")
print("=======================================================")
print("\n")

# Creating a Bank Account using the previously created account_address

example_bank_account = lob.BankAccount.create(
    description='Example bank account',
    routing_number='122100024',
    account_number='1234564789',
    account_type='company',
    signatory='John Doe'
)

print("Bank Account Response")
print("\n")
print("=======================================================")
print("\n")
print(example_bank_account)
print("\n")
print("=======================================================")
print("\n")

# Verifying a Bank Account with the microdeposit amounts

example_bank_account = lob.BankAccount.verify(
    id=example_bank_account.id,
    amounts=[23, 77]
)

print("Bank Account Verify Response")
print("\n")
print("=======================================================")
print("\n")
print(example_bank_account)
print("\n")
print("=======================================================")
print("\n")

# Creating a Check using the previously created and verified bank account

example_check = lob.Check.create(
    description='Example Check',
    metadata={
        'FY': '2015'
    },
    to_address=example_address,
    from_address={
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    bank_account=example_bank_account,
    amount=1000,
    memo='Services Rendered',
    check_bottom="""
      <html>
        <head>
          <style>
            @font-face {
              font-family: 'Loved by the King';
              src: url('https://s3-us-west-2.amazonaws.com/public.lob.com/fonts/lovedByTheKing/LovedbytheKing.ttf');
            }
          </style>
        </head>
        <body><h1>Demo check for {{name}}</h1></body>
      </html>""",
    merge_variables={
        'name': example_address.name
    },
    logo='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/check_logo.png'
)

print("Check Response")
print("\n")
print("=======================================================")
print("\n")
print(example_check)
print("\n")
print("=======================================================")
print("\n")
