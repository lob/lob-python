# lob-python

[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python) [![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob) [![Downloads](https://pypip.in/download/lob/badge.svg)](https://pypi.python.org/pypi/lob/) [![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.svg?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master) [![Dependency Status](https://gemnasium.com/lob/lob-python.svg)](https://gemnasium.com/lob/lob-python)

This is the python wrapper for the Lob.com API.

This wrapper works in the object oriented style, that is, to make calls you have to call the method on a class and the
return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Supported Image Types](#supported-image-types)
- [Initialization and Configuration](#initialization-and-configuration)
- [API Reference](#api-reference)
- [Testing](#testing)

## Installation

You can use `pip` or `easy_install` for installing the package.

```
pip install lob
easy_install lob
```

## Usage

We've provided an example script you can run in examples/ that has examples of
how to use the lob-python wrapper with some of our core endpoints.

## Supported Image Types
The Lob.com API supports the following image types:

- PDF
- PNG
- JPEG

For more information on prepping the images please see the [Lob documentation](https://lob.com/docs/python#prepping).

#### Creating a PDF

We recommed using [python-pdfkit](https://github.com/JazzCore/python-pdfkit) to generate PDFs using HTML input. This depends on having [wkhtmltopdf](http://wkhtmltopdf.org/) installed.

You can find an example [here](examples/create_pdf.py)

## Initialization and Configuration

To initialize the wrapper, import `lob` and set the `api_key`

```python
import lob
lob.api_key = 'your-api-key'

// set an api version (optional)
lob.api_version = 'api-version'
```

## API Reference
- [Simple Print Service](#simple-print-service)
  - [lob.Job](#lobjob)
    - [lob.Job.create](#lobjobcreate)
    - [lob.Job.list](#lobjoblist)
    - [lob.Job.retrieve](#lobjobretrieve)
  - [lob.Address](#lobaddress)
    - [lob.Address.create](#lobaddresscreate)
    - [lob.Address.list](#lobaddresslist)
    - [lob.Address.retrieve](#lobaddressretrieve)
    - [lob.Address.delete](#lobaddressdelete)
  - [lob.Country](#lobcountry)
    - [lob.Country.list](#lobcountrylist)
  - [lob.State](#lobstate)
    - [lob.State.list()](#lobstatelist)
  - [lob.Object](#lobobject)
    - [lob.Object.create](#lobobjectcreate)
    - [lob.Object.list](#lobobjectlist)
    - [lob.Object.retrieve](#lobobjectretrieve)
    - [lob.Object.delete](#lobobjectdelete)
  - [lob.Setting](#lobsetting)
    - [lob.Setting.list](#lobsettinglist)
    - [lob.Setting.retrieve](#lobsettingretrieve)
  - [lob.services](#lobservice)
    - [lob.services.list](#lobservicelist)
- [Simple Postcard Service](#simple-postcard-service)
  - [lob.Postcard](#lobpostcard)
    - [lob.Postcard.create](#lobpostcardcreate)
    - [lob.Postcard.list](#lobpostcardlist)
    - [lob.Postcard.retrieve](#lobpostcardretrieve)
- [Simple Check Service](#simple-check-service)
  - [lob.Check](#lobcheck)
    - [lob.Check.create](#lobcheckcreate)
    - [lob.Check.list](#lobchecklist)
    - [lob.Check.retrieve](#lobcheckretrieve)
  - [lob.BankAccount](#lobbankaccount)
    - [lob.BankAccount.create](#lobbankaccountcreate)
    - [lob.BankAccount.list](#lobbankaccountlist)
    - [lob.BankAccount.retrieve](#lobbankaccountretrieve)
- [Simple Area Mail](#simple-area-mail)
  - [lob.Area](#lobarea)
    - [lob.Area.create](#lobareacreate)
    - [lob.Area.list](#lobarealist)
    - [lob.Area.retrieve](#lobarearetrieve)
  - [lob.Route](#lobroute)
    - [lob.Route.retrieve](#lobrouteretrieve)
- [Address Verification](#address-verification)
  - [lob.Verification](#lobverification)
    - [lob.Verification.create](#lobverificationcreate)

## Simple Print Service

### lob.Job

#### lob.Job.list

```python
#Returns a list of Job objects
lob.Job.list()

#Can specify count and offset as well
lob.Job.list(count=5, offset=1)
```

#### lob.Job.retrieve

```python
#Retrieve a specific job by id
lob.Job.retrieve(<id>)
```

#### lob.Job.create

```python
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
        'file': 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
        'setting': '201'
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
        'file': 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
        'setting': '201'
    }, {
        'name': 'Test Object 2',
        'file': 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
        'setting': '201'
    }]
)
```

### lob.Address

#### lob.Address.list

```python
#List addresses
lob.Address.list()

#List Addresses with Count and Offset
lob.Address.list(count=5, offset=2)
```

#### lob.Address.retrieve
```python
# You can query an address with its `ID`
lob.Address.retrieve(id=<id>)

#or another way
lob.Address.retrieve(<id>)
```

#### lob.Address.create
```python
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
```

#### lob.Address.delete
```python
#Delete an address
lob.Address.delete(<id>)

#or another way
lob.Address.delete(<id>)
```

### lob.Country

#### lob.Country.list
```python
  # Returns a list of Country objects
  lob.Country.list()
```

### lob.State

#### lob.State.list
```python
  # Returns a list of State objects
  lob.State.list()
```

### lob.Object

#### lob.Object.list

```python
# Returns a list of Object objects
lob.Object.list()

# Can specify count and offset
lob.Object.list(count=4, offset=2)
```

#### lob.Object.retrieve

```python
#Retrieve a specifc object
lob.Object.retrieve(<id>)
```

#### lob.Object.create

```python
#Create an Object using a URL
lob.Object.create(
    name='Joe Smith',
    file='https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    setting='201',
    quantity=1,
    double_sided=1
)

#Create an Object using a local file
lob.Object.create(
    name='Local File Object',
    file=open('/path/to/local/file', 'rb'),
    setting='100',
    quantity=1,
    double_sided=0
)

#Create an Object using a file-like object.
from StringIO import StringIO
lob.Object.create(
    name='File-Like Object',
    file=StringIO(compute_pdf_data()),
    setting='100',
    quantity=1,
    double_sided=0
)
```

#### lob.Object.delete

```python
# Delete an object via it's ID
lob.Object.delete(<id>)
```

### lob.Setting

#### lob.Setting.list

```python
#List All Settings
lob.Setting.list()
```

#### lob.Setting.retrieve

```python
#Retrieve a Setting
print lob.Setting.retrieve(id=100)

#or another way
print lob.Setting.retrieve(100)
```

### lob.Service

#### lob.Service.list

```python
#List All Services
lob.Service.list()
```

## Simple Postcard Service

### lob.Postcard

#### lob.Postcard.list

```python
# Returns a list of Postcard objects
lob.Postcard.list()

# Can specify count and offset as well
lob.Postcard.list(count=5, offset=1)
```

#### lob.Postcard.retrieve
```python
#Retrieve a specific postcard by id
lob.Postcard.retrieve(<id>)
```

#### lob.Postcard.create
```python
#Create a Postcard Using IDs for Address
lob.Postcard.create(
    to_address=<address_id>,
    from_address=<address_id>,
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf'
)

#Create a Postcard Using Lob Python Objects
addresses = lob.Address.list(count=2).data
to_addr = addresses[0]
from_addr = addresses[1]
lob.Postcard.create(
    to_address = to_addr,
    from_address = from_addr,
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf'
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
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/test.pdf'
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

## Simple Check Service

### lob.Check

#### lob.Check.list
```python
# Returns a list of Check objects
lob.Check.list()

# Can specify count and offset as well
lob.Check.list(count=5, offset=1)
```

#### lob.Check.retrieve
```python
#Retrieve a specific Check by id
lob.Check.retrieve(<id>)
```

#### lob.Check.create

```python
#Create Check with Address Id
lob.Check.create(
    name = 'Check Test',
    to_address = <address_id>,
    bank_account = <bank_account_id>,
    amount = 1000,
    memo = 'Services Rendered',
    logo = 'https://s3-us-west-2.amazonaws.com/lob-assets/lob_check_logo.png'
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
    memo = 'Services Rendered',
    logo = 'https://s3-us-west-2.amazonaws.com/lob-assets/lob_check_logo.png'
)
```

### lob.BankAccount

#### lob.BankAccount.list

```python
# Returns a list of BankAccount objects
lob.BankAccount.list()

# Can specify count and offset as well
lob.BankAccount.list(count=5, offset=1)
```

#### lob.BankAccount.retrieve

```python
#Retrieve a specific BankAccount by id
lob.BankAccount.retrieve(<id>)
```

#### lob.BankAccount.create

```python
#Create Bank Account Using Address Ids
lob.BankAccount.create(
    routing_number = '123456789',
    account_number = '1234564789',
    signatory = 'John Doe',
    bank_address = <address_id>,
    account_address = <address_id>
)

#Create Bank Account with Inline Addresses
lob.BankAccount.create(
    routing_number = '123456789',
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
```

#### lob.BankAccount.delete

```python
#Delete a specific BankAccount by id
lob.BankAccount.delete(<id>)
```


## Simple Area Mail

### lob.Area

#### lob.Area.list

```python
#List areas
lob.Area.list()

#List Areas with Count and Offset
lob.Area.list(count=5, offset=2)
```

#### lob.Area.retrieve

```python
# You can query an area with its `ID`
lob.Area.retrieve(id=<id>)

#or another way
lob.Area.retrieve(<id>)
```

#### lob.Area.create

```python
#Basic Area Create with Zip Codes
lob.Area.create(
    name='Lob',
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/areafront.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/areaback.pdf',
    routes = ['94158','60031'],
    target_type = 'all',
    full_bleed = '1'
)

#Basic Area Create with Routes Object
var routes = lob.Route.list(zip_codes=[94158,60031])
lob.Area.create(
    name='Lob',
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/areafront.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/areaback.pdf',
    routes = routes,
    target_type = 'all',
    full_bleed = '1'
)

#Create Area with Optional Parameters
lob.Area.create(
    front = 'https://s3-us-west-2.amazonaws.com/lob-assets/areafront.pdf',
    back = 'https://s3-us-west-2.amazonaws.com/lob-assets/areaback.pdf',
    routes = '94158',
)
```

### lob.Route

#### lob.Route.list

```python
#Retrieve routes for given zip codes
lob.Route.list(zip_codes=[94158,60031])
```

## Address Verification

###  lob.Verification

#### lob.Verification.create
```python
#You can verify an address using the following code:
print lob.Verification.create(
    name='Lob',
    address_line1='185 Berry Street',
    address_line2='Suite 1510',
    address_city='San Francisco',
    address_state='CA',
    address_zip='94107',
    address_country='US'
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

## Testing

Install all requirements with `pip install -r requirements.txt`.

You can run all tests with the command `nosetests` in the main directory.
