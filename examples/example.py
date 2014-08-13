import lob
lob.api_key = "test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc" # Replace this API key with your own.

# Creating an Address Object

example_address = lob.Address.create(
    name='Joe Smith',
    address_line1='104, Printing Boulevard',
    address_city='Boston',
    address_state='MA',
    address_country='US',
    address_zip='12345'
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
    name='Example Object',
    file='https://www.lob.com/test.pdf',
    setting_id='201',
    quantity=1,
    double_sided=1
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

# Creating a Postcard

example_postcard = lob.Postcard.create(
    to_address = example_address,
    from_address = example_address,
    front = 'https://www.lob.com/test.pdf',
    back = 'https://www.lob.com/test.pdf'
)

print "Postcard Response"
print "\n"
print "======================================================="
print "\n"
print example_postcard
print "\n"
print "======================================================="
print "\n"

# Creating a Bank Account

example_bank_account = lob.BankAccount.create(
    routing_number = '123456789',
    account_number = '1234564789',
    bank_address = {
        'name': 'Bank Address',
        'address_line1': '123 Wall Street',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94158',
        'address_country': 'US'
    },
    account_address = example_address
)

print "Bank Account Response"
print "\n"
print "======================================================="
print "\n"
print example_bank_account
print "\n"
print "======================================================="
print "\n"

# Creating a Check using the previously created bank account

example_check = lob.Check.create(
    name = 'Example Check',
    to_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    bank_account = example_bank_account,
    amount = 1000,
    memo = 'Services Rendered'
)

print "Check Response"
print "\n"
print "======================================================="
print "\n"
print example_check
print "\n"
print "======================================================="
print "\n"
