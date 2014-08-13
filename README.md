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

We've provided an example script you can run in examples/ that has examples of
how to use the lob-python wrapper with some of our core endpoints.

## Intialization and Configuration

To initialize the wrapper, import `lob` and set the `api_key`

```python
import lob
lob.api_key = 'your-api-key'
```

## Addresses

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
    address_line2='Sunset Town',
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

## Routes

```python
#Retrieve routes for given zip codes
lob.Route.list(zip_codes=[94158,60031])
```

## Areas

```python
#List areas
lob.Area.list()

#List Areas with Count and Offset
lob.Area.list(count=5, offset=2)

# You can query an area with its `ID`
lob.Area.retrieve(id=<id>)

#or another way
lob.Area.retrieve(<id>)

#Basic Area Create with Zip Codes
lob.Area.create(
    name='Lob',
    front = 'https://www.lob.com/areafront.pdf',
    back = 'https://www.lob.com/areaback.pdf',
    routes = ['94158','60031'],
    target_type = 'all',
    full_bleed = '1'
)

#Basic Area Create with Routes Object
var routes = lob.Route.list(zip_codes=[94158,60031])
lob.Area.create(
    name='Lob',
    front = 'https://www.lob.com/areafront.pdf',
    back = 'https://www.lob.com/areaback.pdf',
    routes = routes,
    target_type = 'all',
    full_bleed = '1'
)


#Create Area with Optional Parameters
lob.Area.create(
    front = 'https://www.lob.com/areafront.pdf',
    back = 'https://www.lob.com/areaback.pdf',
    routes = '94158',
)
```

## Settings

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

## Packagings

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

# Delete an object via it's ID
lob.Object.delete(<id>)
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

## Postcards

```python
# Returns a list of Postcard objects
lob.Postcard.list()

# Can specify count and offset as well
lob.Postcard.list(count=5, offset=1)

#Retrieve a specific postcard by id
lob.Postcard.retrieve(<id>)

#Create a Postcard Using IDs for Address
lob.Postcard.create(
    to_address=<address_id>,
    from_address=<address_id>,
    front = 'https://www.lob.com/test.pdf',
    back = 'https://www.lob.com/test.pdf'
)

#Create a Postcard Using Lob Python Objects
addresses = lob.Address.list(count=2).data
to_addr = addresses[0]
from_addr = addresses[1]
lob.Postcard.create(
    to_address = to_addr,
    from_address = from_addr,
    front = 'https://www.lob.com/test.pdf',
    back = 'https://www.lob.com/test.pdf'
)

#Create Postcard Using Inline Addresses
lob.Postcard.create(
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
    front = 'https://www.lob.com/test.pdf',
    back = 'https://www.lob.com/test.pdf'
)

#Create Postcard Using Inline Addresses and Local File
lob.Postcard.create(
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
    front = open('/path/to/local/file', 'rb'),
    back = open('/path/to/local/file', 'rb')
)

#Create Postcard with Message Instead of Back
lob.Postcard.create(
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
    front = open('/path/to/local/file', 'rb'),
    message = 'Hello this is the message!'
)
```
## Bank Accounts

```python
# Returns a list of BankAccount objects
lob.BankAccount.list()

# Can specify count and offset as well
lob.BankAccount.list(count=5, offset=1)

#Retrieve a specific BankAccount by id
lob.BankAccount.retrieve(<id>)

#Create Bank Account Using Address Ids
lob.BankAccount.create(
    routing_number = '123456789',
    account_number = '1234564789',
    bank_address = <address_id>,
    account_address = <address_id>
)

#Create Bank Account with Inline Addresses
lob.BankAccount.create(
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
    account_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    }
)

#Delete a specific BankAccount by id
lob.BankAccount.delete(<id>)
```

## Checks

```python
# Returns a list of Check objects
lob.Check.list()

# Can specify count and offset as well
lob.Check.list(count=5, offset=1)

#Retrieve a specific Check by id
lob.Check.retrieve(<id>)

#Create Check with Address Id
lob.Check.create(
    name = 'Check Test',
    to_address = <address_id>,
    bank_account = <bank_account_id>,
    amount = 1000,
    memo = 'Services Rendered'
)

#Create Check with Inline Address
lob.Check.create(
    name = 'Check Test',
    to_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_zip': '94107',
        'address_country': 'US'
    },
    bank_account = <bank_account_id>,
    amount = 1000,
    memo = 'Services Rendered'
)
```
