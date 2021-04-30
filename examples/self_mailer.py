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

# Creating a Self Mailer
example_self_mailer = lob.SelfMailer.create(
    description='Test Self Mailer',
    metadata={
        'campaign': 'Member welcome'
    },
    to_address=example_address,
    from_address=example_address,
    outside="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/6x18_sfm_outside.pdf",
    inside="<h1>Hello {{name}}</h1>",
    merge_variables={
        'name': example_address.name
    },
)

print("Self Mailer Response")
print("\n")
print("=======================================================")
print("\n")
print(example_self_mailer)
print("\n")
print("=======================================================")
print("\n")
