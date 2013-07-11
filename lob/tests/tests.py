# Various API calls demonstrated

import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

# Create an address
address = lob.Address.create(name = 'Siddharth Saha', address_line1 = '104, Printing Boulevard',
        address_city = 'Boston', address_state = 'MA', address_country = 'USA',
        address_zip = '12345')
print address.to_dict()
# Can also pass other parameters while creating an address
address = lob.Address.create(name = 'Siddharth Saha', address_line1 = '104, Printing Boulevard',
        address_line2 = 'Sunset Town', email = 'sidchilling@gmail.com', 
        address_city = 'Boston', address_state = 'MA', address_country = 'USA',
        address_zip = '12345')
print address.to_dict()

# List addresses
print lob.Address.list()
# Can also pass count and offset
print lob.Address.list(count = 5, offset = 2)

# Find an address
print lob.Address.get(id = lob.Address.list(count = 1)[0].id).to_dict()

# Deleting an address
print lob.Address.delete(id = lob.Address.list(count = 1)[0].id).to_dict()

# Address Verification
print lob.AddressVerify.verify(name = 'Siddharth Saha', email = 'sidchilling@gmail.com',
        address_line1 = '220 William T Morrissey', address_city = 'Boston', 
        address_state = 'MA', address_zip = '02125').to_dict()

# List Settings
print lob.Setting.list()

# Find a Setting
print lob.Setting.get(id = lob.Setting.list()[0].id).to_dict()

# List all Services
print lob.Service.list()

# List all packagings
print lob.Packaging.list()

# List all objects
print lob.Object.list()
# Can also pass count and offset
print lob.Object.list(count = 1)[0].to_dict()

# Find an object
print lob.Object.get(id = lob.Object.list(count = 1)[0].id).to_dict()

# Delete an object
print lob.Object.delete(id = lob.Object.list(count = 1)[0].id).to_dict()

# Creat an object
print lob.Object.create(name = 'Siddharth Object', file = 'https://www.lob.com/goblue.pdf',
        setting_id = lob.Setting.list()[0].id, quantity = 1).to_dict()

# List all jobs
print lob.Job.list()
# Can also pass count and offset
print lob.Job.list(count = 5, offset = 1)

# Find a job with id
print lob.Job.get(id = lob.Job.list(count = 1)[0].id).to_dict()

# Create a job 
print lob.Job.create(name = 'Siddharth First Job', to = lob.Address.list(count = 1)[0].id,
        objects = lob.Object.list()[0].id, from_address = lob.Address.list(count = 1, 
            offset = 5)[0].id).to_dict()

# Can specify address as parameters instead of ID and can have multiple objects (both id and parameters)
objects = [lob.Object.list()[0].id, {
    'name' : 'Siddharth Job Object',
    'file' : 'https://www.lob.com/goblue.pdf',
    'setting_id' : lob.Setting.list()[0].id,
    'quantity' : 1
    }]
from_address = {
        'name' : 'Siddharth Saha',
        'address_line1' : '220 William T Morrissey',
        'address_line2' : 'Sunset Town',
        'address_city' : 'Boston',
        'address_state' : 'MA',
        'address_country' : 'USA',
        'address_zip' : '02125'
        }

print lob.Job.create(name = 'Siddharth Second Job', to = lob.Address.list(count = 1)[0].id,
        objects = objects, from_address = from_address,
        packaging_id = lob.Packaging.list()[0].id,
        service_id = lob.Service.list()[0].id).to_dict()
