Lob Python Wrapper
==========
[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python) [![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob) [![Downloads](https://pypip.in/d/lob/badge.png)](https://crate.io/packages/lob) [![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.png?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master) [![Dependency Status](https://gemnasium.com/lob/lob-python.svg)](https://gemnasium.com/lob/lob-python)


This is the python wrapper for the lob.com API.

This wrapper works in the object oriented style, that is, to make calls you have to call the method on a class and the
return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

Installation
============

You can use `pip` or `easy_install` for installing the package.

```
pip install lob
easy_install lob
```

Testing
=======

Install all requirements with `pip install -r requirements.txt`.

You can run all tests with the command `nosetests` in the main directory.

Usage
======

## Intialization and Configuration

To initialize the wrapper, import `lob` and set the `api_key`

```python
import lob
lob.api_key = 'your-api-key'
```

## Addresses

### Create a new address

```python
#List addresses
lob.Address.list()

#List Addresses with Count and Offset
lob.Address.list(count=5, offset=2)

# You can query an address with its `ID`
lob.Address.retrieve(id=<id>)

#or another way
lob.Address.retrieve(<id>)

#Basic Address Create
lob.Address.create(
    name='Joe Smith',
    address_line1='104, Printing Boulevard',
    address_city='Boston',
    address_state='MA',
    address_country='US',
    address_zip='12345'
)

#Create Address with Optional Parameters
lob.Address.create(
    name='Joe Smith',
    email='support@lob.com',
    phone='555-555-5555',
    address_line1='104, Printing Boulevard',
    address_line2='Sunset Town', email='sidchilling@gmail.com',
    address_city='Boston',
    address_state='MA',
    address_country='US',
    address_zip='12345'
)

#Delete an address
lob.Address.delete(<id>)

#or another way
lob.Address.delete(<id>)
```

## Address Verification

```python
#You can verify an address using the following code:
print lob.Verification.create(
    name='Lob',
    address_line1='185 Berry Street',
    address_line2='Suite 1510',
    address_city='San Francisco',
    address_state='CA',
    address_zip='94107',
    address_country='US
)
```
This will output:
```bash
{
  "address": {
    "address_city": "SAN FRANCISCO",
    "address_country": "US",
    "address_line1": "185 BERRY ST STE 1510",
    "address_line2": "",
    "address_state": "CA",
    "address_zip": "94107-5705"
  },
  "message": "Default address: The address you entered was found but more information is needed (such as an apartment, suite, or box number) to match to a specific address."
}
```
## Setting

### List all Settings

```python
#List All Settings
lob.Setting.list()

#Retrieve a Setting
print lob.Setting.retrieve(id=100)

#or another way
print lob.Setting.retrieve(100)
```

## Services

```python
#List All Services
lob.Service.list()
```

## Packaging

### List all packagings

```python
#List All Packagings
lob.Packaging.list()
```

## Objects

```python
# Returns a list of Object objects
lob.Object.list()

# Can specify count and offset
lob.Object.list(count=4, offset=2)

#Retrieve a specifc object
lob.Object.retrieve(<id>)

# Delete an object via it's ID
lob.Object.delete(<id>)

#Create an Object using a URL
lob.Object.create(
    name='Joe Smith',
    file='https://www.lob.com/test.pdf',
    setting_id='201',
    quantity=1
)

#Create an Object using a local file
lob.Object.create(
    name='Local File Object',
    file=open('/path/to/local/file', 'rb'),
    setting_id='100',
    quantity=1
)
```

## Jobs

```python
# Returns a list of Job objects
lob.Job.list()

# Can specify count and offset as well
lob.Job.list(count=5, offset=1)

#Retrieve a specific job by id
lob.Job.retrieve(<id>)

#Create Job Using IDs for Address and Object
lob.Job.create(
    name='Joe First Job',
    to_address=<address_id>,
    from_address=<address_id>,
    objects = <object_id>
)

#Create a Job Using Lob Python Objects
addresses = lob.Address.list(count=2).data
to_addr = addresses[0]
from_addr = addresses[1]
obj = lob.Object.list(count=1).data[0]
lob.Job.create(
    to_address = to_addr,
    from_address = from_addr,
    objects = obj
)

#Create Job Using Inline Address and Object
lob.Job.create(
    to_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    from_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    objects = {
        'name': 'Test Object',
        'file': 'https://www.lob.com/test.pdf',
        'setting_id': '201'
    }
)

#Create a Multi-Object Job
lob.Job.create(
    to_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    from_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    objects = [{
        'name': 'Test Object 1',
        'file': 'https://www.lob.com/test.pdf',
        'setting_id': '201'
    }, {
        'name': 'Test Object 2',
        'file': 'https://www.lob.com/test.pdf',
        'setting_id': '201'
    }]
)
```

## Postcard

Works on the `Postcard` class.

```python
lob.Postcard.list() # Returns a list of Postcard objects
lob.Postcard.list(count=5, offset=3) # Can also pass count and offset
```

### Creating a postcard

You must either specify the `message` argument or the `back` argument (but not both). Both `to` and `from_address` addresses can contain Address ID or Address parameters (as in creation of Job).

```python
# Specifying message
print lob.Postcard.create(name='Siddharth Test Postcard', to=lob.Address.list(count=1)[0].id,
                           message='This is a standard test message',
                           front='https://www.lob.com/postcardfront.pdf',
                           from_address=from_address)

# Specifying back and address as parameters (using from_address defined earlier in Job creation)
print lob.Postcard.create(name='Siddharth New Test Postcard', to=lob.Address.list(count=1)[0].id,
                          front='https://www.lob.com/postcardfront.pdf',
                          back='https://www.lob.com/postcardback.pdf', from_address=from_address)

# create a postcard using a local file
lob.Postcard.create(name='MY Test Postcard', to={'name' : 'Bon Jovi',
                'address_line1' : '220 William T Morrissey',
                'address_line2' : 'Sunset Town',
                'address_city' : 'Boston',
                'address_state' : 'MA',
                'address_country' : 'US',
                'address_zip' : '02125'},
                           message='This is a standard test message',
                           front=open('test.pdf','rb'),
                           from_address={'name' : 'Michelle Obama',
                'address_line1' : '220 William T Morrissey',
                'address_line2' : 'Sunset Town',
                'address_city' : 'Boston',
                'address_state' : 'MA',
                'address_country' : 'US',
                'address_zip' : '02125'}).to_dict()
```
## Bank Account

Works on the `BankAccount` class.

```python
lob.BankAccount.list() # Returns a list of BankAccount objects
lob.BankAccount.list(count=5, offset=3) # Can also pass count and offset
lob.BankAccount.get(id='<bank-account-id>') # Can find a bank account based on its ID - Returns a BankAccount instance.
```

### Creating a bank account

```python
print lob.BankAccount.create(
    routing_number='122100024',
    account_number='123456789',
    bank_address=lob.Address.list(count=1, offset=4)[0].id,
    account_address=lob.Address.list(count=1)[0].id,
    bank_code=None).to_dict()
```

`routing_number` (required): The bank's routing number

`account_number` (required): The account number at the bank

`bank_address` (required): The bank branch address. Must either be an address ID or an array with correct address parameters. If an array is used, an address will be created for you and returned with an ID.

`account_address` (required): The address associated with your account. Must either be an address ID or an array with correct address parameters. If an array is used, an address will be created for you and returned with an ID.

`bank_code` (optional): The bank code that is printed on your checks. Added for extra security. You can usually find this near the bank address on the check.


## Check

Works on the `Check` class.

```python
lob.Check.list() # Returns a list of Check objects
lob.Check.list(count=5, offset=3) # Can also pass count and offset
lob.Check.get(id='<check-id>') # Can find a check based on its ID - Returns a Check instance.
```

### Creating a check

```python
to_address = {
    'name': 'Ralph Receiver',
    'address_line1': '1234 E Grant St',
    'address_line2': None,
    'address_city': 'Tucson',
    'address_state': 'AZ',
    'address_country': 'US',
    'address_zip': '85712'
}

print lob.Check.create(
    bank_account=lob.BankAccount.list(count=1)[0].id,
    to=to_address,
    amount=1000.00,
    name='Demo Check',
    check_number=None,
    message='Hi Ralph. Thanks for your work. - Paul',
    memo='Services rendered.'
).to_dict()
```

`name` (optional): Description name for the check. E.g. 'Demo Check'

`check_number` (optional): Checks will default starting at 10000 and increment accordingly.

`bank_account` (required): Must be a bank account ID.

`to` (required): Must either be an address ID or an array with correct address parameters. If an array is used, an address will be created for you and returned with an ID.

`amount` (required): The payment amount to be sent.

`message` (optional): Max of 400 characters to be included on the top of the check.

`memo` (optional): Max of 40 characters to be included on the memo line of the check.
