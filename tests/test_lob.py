# Various API calls demonstrated

import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

# Create an address

def test_address():
    address = lob.Address.create(name = 'Siddharth Saha', address_line1 = '104, Printing Boulevard',
        address_city = 'Boston', address_state = 'MA', address_country = 'USA',
        address_zip = '12345')
    print address.to_dict()


def test_address_other_parameters():
    """Can also pass other parameters while creating an address"""
    address = lob.Address.create(name = 'Siddharth Saha', address_line1 = '104, Printing Boulevard',
        address_line2 = 'Sunset Town', email = 'sidchilling@gmail.com', 
        address_city = 'Boston', address_state = 'MA', address_country = 'USA',
        address_zip = '12345')
    print address.to_dict()


def test_list_addresses():
    print lob.Address.list()


def test_list_addresses_count_offset():
    # Can also pass count and offset
    print lob.Address.list(count = 5, offset = 2)


def test_find_address():
    print lob.Address.get(id = lob.Address.list(count = 1)[0].id).to_dict()


def test_delete_address():
    print lob.Address.delete(id = lob.Address.list(count = 1)[0].id).to_dict()


def test_address_verification():
    print lob.AddressVerify.verify(name = 'Siddharth Saha', email = 'sidchilling@gmail.com',
        address_line1 = '220 William T Morrissey', address_city = 'Boston', 
        address_state = 'MA', address_zip = '02125', address_country = 'USA').to_dict()


def test_settings():
    print lob.Setting.list()


def test_find_setting():
    print lob.Setting.get(id = lob.Setting.list()[0].id).to_dict()


def test_list_all_services():
    print lob.Service.list()


def test_packaging_list():
    print lob.Packaging.list()


def test_list_objects():
    print lob.Object.list()


def test_list_objects_count_offset():
    print lob.Object.list(count = 1)[0].to_dict()


def test_find_object():
    print lob.Object.get(id = lob.Object.list(count = 1)[0].id).to_dict()


def test_delete_object():
    print lob.Object.delete(id = lob.Object.list(count = 1)[0].id).to_dict()

def test_create_object():
    print lob.Object.create(name = 'Siddharth Object', file = 'https://www.lob.com/goblue.pdf',
            setting_id = lob.Setting.list()[0].id, quantity = 1).to_dict()

def test_job_list():
    print lob.Job.list()


def test_job_list_count_offset():
    print lob.Job.list(count = 5, offset = 1)


def test_find_job():
    print lob.Job.get(id = lob.Job.list(count = 1)[0].id).to_dict()


def test_create_job():
    print lob.Job.create(name = 'Siddharth First Job', to = lob.Address.list(count = 1)[0].id,
            objects = lob.Object.list()[0].id, from_address = lob.Address.list(count = 1, 
            offset = 5)[0].id).to_dict()


def test_create_job_with_multiple_objects():
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


def test_list_postcards():
    print lob.Postcard.list()


def test_list_postcards_offset_count():
    print lob.Postcard.list(offset = 2, count = 1)[0].to_dict()


def test_find_postcard():
    print lob.Postcard.get(id = lob.Postcard.list(count = 1)[0].id)

def test_create_postcard():
    print lob.Postcard.create(name = 'Siddharth Test Postcard', to = lob.Address.list(count = 1)[0].id,
        message = 'This is a standard test message', front = 'https://www.lob.com/postcardfront.pdf',
        from_address = lob.Address.list(count = 1, offset = 4)[0].id).to_dict()

def test_create_postcard_parameters():
    from_address = {
        'name' : 'Siddharth Saha',
        'address_line1' : '220 William T Morrissey',
        'address_line2' : 'Sunset Town',
        'address_city' : 'Boston',
        'address_state' : 'MA',
        'address_country' : 'USA',
        'address_zip' : '02125'
    }

    print lob.Postcard.create(name = 'Siddharth New Test Postcard', 
        to = lob.Address.list(count = 1)[0].id, front = 'https://www.lob.com/postcardfront.pdf',
        back = 'https://www.lob.com/postcardback.pdf',
        from_address = from_address).to_dict()
