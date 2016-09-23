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

# Creating an Object

example_object = lob.Object.create(
    description = 'Example Object',
    file = """
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
    data = {
        'name': example_address.name
    },
    setting = '201',
    quantity = 1
)

print "Object Response"
print "\n"
print "======================================================="
print "\n"
print example_object
print "\n"
print "======================================================="
print "\n"

# Creating a Job using the previously created address and object

example_job = lob.Job.create(
    description = 'Test Job',
    metadata = {
        'campaign': 'Member survey'
    },
    to_address = example_address,
    from_address = example_address,
    objects = example_object,
)

print "Job Response"
print "\n"
print "======================================================="
print "\n"
print example_job
print "\n"
print "======================================================="
print "\n"
