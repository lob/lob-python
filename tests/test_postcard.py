import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class PostcardFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
        self.addr = lob.Address.list(count=1).data[0]

    def test_list_postcards(self):
        postcards = lob.Postcard.list()
        self.assertTrue(isinstance(postcards.data[0], lob.Postcard))
        self.assertEqual(postcards.object, 'list')

    def test_list_postcards_limit(self):
        postcards = lob.Postcard.list(count=2)
        self.assertTrue(isinstance(postcards.data[0], lob.Postcard))
        self.assertEqual(len(postcards.data), 2)

    def test_list_postcards_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.list, count=1000)

    def test_create_postcard(self):
        postcard = lob.Postcard.create(
            to_address = self.addr.id,
            from_address = self.addr.id,
            front = 'https://www.lob.com/test.pdf',
            back = 'https://www.lob.com/test.pdf'
        )
        self.assertEqual(postcard.to_address.id, self.addr.id)
        self.assertEqual(postcard.from_address.id, self.addr.id)
        self.assertTrue(isinstance(postcard, lob.Postcard))


    def test_create_postcard_lob_obj(self):
        postcard = lob.Postcard.create(
            to_address = self.addr,
            from_address = self.addr,
            front = 'https://www.lob.com/test.pdf',
            back = 'https://www.lob.com/test.pdf'
        )
        self.assertEqual(postcard.to_address.id, self.addr.id)
        self.assertEqual(postcard.from_address.id, self.addr.id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_inline(self):
        postcard = lob.Postcard.create(
            to_address = {
                'name': 'Lob1',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            from_address = {
                'name': 'Lob2',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            front = 'https://www.lob.com/test.pdf',
            message = 'Hello'
        )
        self.assertEqual(postcard.to_address.name, 'Lob1')
        self.assertEqual(postcard.from_address.name, 'Lob2')
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_local_file(self):
        postcard = lob.Postcard.create(
            to_address = self.addr.id,
            from_address = self.addr.id,
            front = open('tests/pc.pdf', 'rb'),
            back = open('tests/pc.pdf', 'rb')
        )
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.create)

    def test_retrieve_postcard(self):
        postcard = lob.Postcard.retrieve(id=lob.Postcard.list().data[0].id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_retrieve_postcard_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.retrieve, id='test')
