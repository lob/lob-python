import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

def test_settings():
    print lob.Setting.list()


def test_find_setting():
    print lob.Setting.retrieve(id=lob.Setting.list().data[0].id)


