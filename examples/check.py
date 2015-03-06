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

# Creating a Bank Account using the previously created account_address

example_bank_account = lob.BankAccount.create(
    routing_number = '122100024',
    account_number = '1234564789',
    signatory = 'John Doe',
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
    memo = 'Services Rendered',
    logo = 'https://s3-us-west-2.amazonaws.com/lob-assets/lob_check_logo.png'
)

print "Check Response"
print "\n"
print "======================================================="
print "\n"
print example_check
print "\n"
print "======================================================="
print "\n"
