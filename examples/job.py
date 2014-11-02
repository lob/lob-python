import lob
lob.api_key = "test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc" # Replace this API key with your own.

# Creating an Address Object

example_address = lob.Address.create(
    name = 'Joe Smith',
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
    name = 'Example Object',
    file = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    setting_id = '201',
    quantity = 1,
    double_sided = 1
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
