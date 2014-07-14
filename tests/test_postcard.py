import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

def test_list_postcards():
    print lob.Postcard.list()


def test_list_postcards_offset_count():
    print lob.Postcard.list(offset=2, count=1).data[0]


def test_find_postcard():
    print lob.Postcard.retrieve(id=lob.Postcard.list(count=1).data[0].id)


def test_create_postcard():
    print lob.Postcard.create(name='Lob Test Postcard', to=lob.Address.list(count=1).data[0].id,
                              message='This is a standard test message', front='https://www.lob.com/test.pdf',
                              from_address=lob.Address.list(count=1, offset=4).data[0].id)


def test_create_postcard_parameters():
    from_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': '',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_country': 'US',
        'address_zip': '94107'
    }

    print lob.Postcard.create(name='Lob New Test Postcard',
                              to=lob.Address.list(count=1).data[0].id, front='https://www.lob.com/test.pdf',
                              back='https://www.lob.com/test.pdf',
                              from_address=from_address)
