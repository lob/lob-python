import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

def test_job_list():
    print lob.Job.list()


def test_job_list_count_offset():
    print lob.Job.list(count=5, offset=1)


def test_find_job():
    print lob.Job.retrieve(id=lob.Job.list(count=1).data[0].id)


def test_create_job():
    print lob.Job.create(name='Lob First Job',
                         to=lob.Address.list(count=1).data[0].id,
                         objects=lob.Object.list().data[0].id,
                         from_address=lob.Address.list(count=1,offset=5).data[0].id)

def test_create_job_with_local_file():
    obj = [{
        'name': 'Lcoal File',
        'file': open('tests/test.pdf', 'rb'),
        'setting_id': 100,
        'quantity': 1
    }]

    print lob.Job.create(name='Test',
                         objects=obj,
                         to=lob.Address.list(count=1).data[0].id,
                         from_address=lob.Address.list(count=1).data[0].id
                        )

def test_create_job_with_multiple_objects():
    objects = [{
        'name': 'Job Object1',
        'file': open('tests/pc.pdf', 'rb'),
        'setting_id': 201,
        'quantity': 1
    }, {
        'name': 'Job Object2',
        'file': 'https://www.lob.com/test.pdf',
        'setting_id': 201,
        'quantity': 1
    },
    lob.Object.create(name='Job Object 3',
                      file='https://www.lob.com/test.pdf',
                      setting_id='201').id
    ]

    from_address = {
        'name': 'Lob',
        'address_line1': '185 Berry Street',
        'address_line2': 'Suite 1510',
        'address_city': 'San Francisco',
        'address_state': 'CA',
        'address_country': 'US',
        'address_zip': '94107'
    }

    print lob.Job.create(name='Lob Second Job',
                         to=lob.Address.list(count=1).data[0].id,
                         objects=objects,
                         from_address=from_address
                        )
