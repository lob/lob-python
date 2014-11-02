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

# Creating a Postcard

example_postcard = lob.Postcard.create(
    to_address = example_address,
    from_address = example_address,
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf'
)

print "Postcard Response"
print "\n"
print "======================================================="
print "\n"
print example_postcard
print "\n"
print "======================================================="
print "\n"
