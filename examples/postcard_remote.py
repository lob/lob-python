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
    front='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/4x6_pc_template.pdf',
    merge_variables={
        'name': example_address.name
    },
    back='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/4x6_pc_template.pdf'
)

print("Postcard Response")
print("\n")
print("=======================================================")
print("\n")
print(example_postcard)
print("\n")
print("=======================================================")
print("\n")
