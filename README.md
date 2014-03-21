lob-python
==========

[![Build Status](https://travis-ci.org/lob/lob-python.png?branch=master)](https://travis-ci.org/lob/lob-python)

This is the python wrapper for the lob.com API.

This wrapper works in the object oriented style, that is, to make calls you have to call the method on a class and the
return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

Installation
============

You can use `pip` or `easy_install` for installing the package.

```
pip install lob-python
easy_install lob-python
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

Addresses work with the `Address` class and the objects returned are of this class.

### Create a new address

```python
address = lob.Address.create(name='Joe Smith', address_line1='104, Printing Boulevard',
                             address_city='Boston', address_state='MA', address_country='US',
                             address_zip='12345')
print address.to_dict()
```

You can pass optional parameters as well while creating an address

```python
print lob.Address.create(name='Joe Smith', address_line1='104, Printing Boulevard',
                         address_line2='Sunset Town', email='sidchilling@gmail.com',
                         address_city='Boston', address_state='MA', address_country='US',
                         address_zip='12345').to_dict()
```

### List Addresses

Will return a `list` of `Address` objects

```python
lob.Address.list()
```

You can also pass `count` and `offset` parameters (or either one of them)

```python
lob.Address.list(count=5, offset=2)
```

### Find an Address

Returns an `Address` object

```python
# You can query an address with its `ID`
print lob.Address.get(id='adr_d46c8c8b67f826d5').to_dict()

# or another way
print lob.Address.get(id=lob.Address.list(count=1)[0].id).to_dict()
```

### Delete an Address

You can delete an address with its `ID`

```python
lob.Address.delete(id='adr_d46c8c8b67f826d5')
```

## Address Verification

You can verify an Address - this API will call return a `LobObject` which is
the super-class of all other classes. You can of course do a `to_dict()` and
get the `dict` representation of a `LobObject` as well.

```python
verify = lob.AddressVerify.verify(name='Joe Smith', email='sidchilling@gmail.com',
                                  address_line1='220 William T Morrissey', address_city='Boston',
                                  address_state='MA', address_zip='02125', address_country='US')

print verify.to_dict()
```

## Setting

Works on the `Setting` class.

### List all Settings

This will return a `list` of `Setting` objects.

```python
print lob.Setting.list()
```

### Find a Setting

```python
print lob.Setting.get(id='<setting-id>').to_dict()
print lob.Setting.get(id=lob.Setting.list()[0].id).to_dict()
```

## Services

Works on the `Service` class.

### List all Services

Returns a `list` of `Service` objects

```python
print lob.Service.list()
```

## Packaging

Works on the `Packaging` class.

### List all packagings

Returns a `list` of `Packaging` objects

```python
print lob.Packaging.list()
```

## Objects

Works on the `Object` class.

```python
lob.Object.list() # Returns a list of Object objects
lob.Object.list(count=4, offset=2) # Can specify count and offset
lob.Object.delete(id='obj_145e602887e61dfd') # Delete an object via it's ID
lob.Object.create(name='Joe Smith', file='https://www.lob.com/goblue.pdf',
                         setting_id='100', quantity=1) # Will create an object and return its instance
lob.Object.create(name='Local File Object', file=open('/path/to/local/file', 'rb'),
                         setting_id='100', quantity=1) # Will create an object with a local file and return its instance
```

## Jobs

Works on the `Job` class.

```python
lob.Job.list() # Returns a list of Job objects
lob.Job.list(count=5, offset=1) # Can specify count and offset as well
lob.Job.list(count=5) # Can specify either offset or count as well
lob.Job.get(id='job_52c74737ab41484090df') # Can find a Job based on its ID - Returns a Job instance
```

### Creating Jobs

Will return a `Job` instance if creation is successful

```python
print lob.Job.create(name='Joe First Job', to='adr_fa1b063697e25611',
                     objects=lob.Object.list()[0].id,
                     from_address=lob.Address.list(count=1, offset=5)[0].id).to_dict()
```

As in the above call, you can see `to` and `from_address` are `Address` IDs and `objects` is a `Object` ID. You can specify these differently as well - passsing complete address parameters. Also, `objects` can be a list specifiying multiple `object` IDs or `object` parameters as well. The following code block will show each of these possibilities.

```python
object = [{'name' : 'My Resume Job Object',
                                     'file' : 'https://www.lob.com/goblue.pdf',
                                     'setting_id' : '101',
                                     'quantity' : 1}] # The objects list can contain both object id as well as parameters

from_address = {'name' : 'Joe Smith',
                'address_line1' : '220 William T Morrissey',
                'address_line2' : 'Sunset Town',
                'address_city' : 'Boston',
                'address_state' : 'MA',
                'address_country' : 'US',
                'address_zip' : '02125'}

print lob.Job.create(name='Joe Second Job', to='adr_fa1b063697e25611',
                            objects=objects, from_address='adr_fa1b063697e25611',
                            packaging_id='7').to_dict()
```

The above code block also shows optional parameters that can be passed

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
