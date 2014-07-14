import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

def test_list_objects():
    print lob.Object.list()


def test_list_objects_count_offset():
    print lob.Object.list(count=1).data[0]


def test_find_object():
    print lob.Object.retrieve(id=lob.Object.list(count=1).data[0].id)


def test_delete_object():
    print lob.Object.delete(id=lob.Object.list(count=1).data[0].id)


def test_create_object():
    print lob.Object.create(name='Test Object', file='https://www.lob.com/test.pdf',
                            setting_id=201, quantity=1)

def test_create_object_with_local_file():
    print lob.Object.create(name='Local File Object', file=open('tests/test.pdf','rb'),
                            setting_id=100, quantity=1)

