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

# Creating a Postcard

example_postcard = lob.Postcard.create(
    description='Test Postcard',
    metadata={
        'campaign': 'Member welcome'
    },
    to_address=example_address,
    from_address=example_address,
    front="""
      <html>
        <head>
          <style>
            @font-face {
              font-family: 'Loved by the King';
              src: url('https://s3-us-west-2.amazonaws.com/public.lob.com/fonts/lovedByTheKing/LovedbytheKing.ttf');
            }
          </style>
        </head>
        <body><h1>Hi {{name}}</h1></body>
      </html>""",
    merge_variables={
        'name': example_address.name
    },
    back="<h1>Welcome to the club!</h1>",
    headers={
      'Idempotency-Key': '026e7634-24d7-486c-a0bb-4a17fd0eebc5'
    }
)

print("Postcard Response")
print("\n")
print("=======================================================")
print("\n")
print(example_postcard)
print("\n")
print("=======================================================")
print("\n")
