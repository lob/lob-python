import sys, os
sys.path.insert(0, os.path.abspath(__file__+'../../..'))

import lob
lob.api_key = "test_fc26575412e92e22a926bc96c857f375f8b" # Replace this API key with your own.

# Creating an Address Object

example_address = lob.Address.create(
    name = 'Joe Smith',
    description = 'Joe - Home',
    metadata = {
        'group': 'Members'
    },
    address_line1 = '104, Printing Boulevard',
    address_city = 'Boston',
    address_state = 'MA',
    address_country = 'US',
    address_zip = '12345'
)

print "\n"
print "Address Response"
print "\n"
print "======================================================="
print "\n"
print example_address
print "\n"
print "======================================================="
print "\n"

# Creating a Postcard

example_postcard = lob.Postcard.create(
    description = 'Test Postcard',
    metadata = {
        'campaign': 'Member welcome'
    },
    to_address = example_address,
    from_address = example_address,
    front = """
      <html>
        <head>
          <style>
            @font-face {
              font-family: 'Loved by the King';
              src: url('https://s3-us-west-2.amazonaws.com/lob-assets/LovedbytheKing.ttf');
            }
          </style>
        </head>
        <body><h1>Hi {{name}}</h1></body>
      </html>""",
    merge_variables = {
        'name': example_address.name
    },
    message = "Welcome to the club!"
)

print "Postcard Response"
print "\n"
print "======================================================="
print "\n"
print example_postcard
print "\n"
print "======================================================="
print "\n"
