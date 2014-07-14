import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
print lob.Packaging.list()

def test_packaging_list():
    print lob.Packaging.list()

