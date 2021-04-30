import unittest
import os
import lob


class PostcardFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')
        self.addr = lob.Address.list(limit=1).data[0]

    def test_list_postcards(self):
        postcards = lob.Postcard.list()
        self.assertTrue(isinstance(postcards.data[0], lob.Postcard))
        self.assertEqual(postcards.object, 'list')

    def test_list_postcards_limit(self):
        postcards = lob.Postcard.list(limit=2)
        self.assertTrue(isinstance(postcards.data[0], lob.Postcard))
        self.assertEqual(len(postcards.data), 2)

    def test_list_postcards_metadata(self):
        postcards = lob.Postcard.list(metadata={'campagin': 'LOB2015'})
        self.assertTrue(isinstance(postcards.data[0], lob.Postcard))
        self.assertEqual(len(postcards.data), 1)

    def test_list_postcards_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.list, limit=1000)

    def test_create_postcard(self):
        postcard = lob.Postcard.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            front='<h1>{{front_name}}</h1>',
            back='<h1>{{back_name}}</h1>',
            merge_variables={
                'front_name': 'Peter',
                'back_name': 'Otto'
            }
        )
        self.assertEqual(postcard.to_address.id, self.addr.id)
        self.assertEqual(postcard.from_address.id, self.addr.id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_idempotent_postcards(self):
        idempotency_key = "Test_Idempotency_Key"
        postcard_one = lob.Postcard.create(
            to_address=self.addr.id,
            front='<h1>Front</h1>',
            back='<h1>Back</h1>',
            headers={
                'Idempotency-Key': idempotency_key
            }
        )

        postcard_two = lob.Postcard.create(
            to_address=self.addr.id,
            front='<h1>Front</h1>',
            back='<h1>Back</h1>',
            headers={
                'Idempotency-Key': idempotency_key
            }
        )

        self.assertEqual(postcard_one.id, postcard_two.id)
        self.assertTrue(isinstance(postcard_one, lob.Postcard))

    def test_create_postcard_lob_obj(self):
        postcard = lob.Postcard.create(
            to_address=self.addr,
            from_address=self.addr,
            front='<h1>{{front_name}}</h1>',
            back='<h1>{{back_name}}</h1>',
            merge_variables={
                'front_name': 'Peter',
                'back_name': 'Otto'
            }
        )
        self.assertEqual(postcard.to_address.id, self.addr.id)
        self.assertEqual(postcard.from_address.id, self.addr.id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_inline(self):
        postcard = lob.Postcard.create(
            to_address={
                'name': 'Lob1',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA',
                'metadata': {
                    'department': 'marketing'
                }
            },
            from_address={
                'name': 'Lob2',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            front='<h1>{{front_name}}</h1>',
            back='<h1>{{back_name}}</h1>',
            merge_variables={
                'front_name': 'Peter',
                'back_name': 'Otto'
            }
        )
        self.assertEqual(postcard.to_address.name, 'LOB1')
        self.assertEqual(postcard.from_address.name, 'LOB2')
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_local_file(self):
        postcard = lob.Postcard.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            front=open('tests/pdfs/pc.pdf', 'rb'),
            back=open('tests/pdfs/pc.pdf', 'rb')
        )
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_create_postcard_with_merge_variable_list(self):
        postcard = lob.Postcard.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            front='<html>{{#list}} {{name}} {{/list}}</html>',
            back='<html>{{#list}} {{name}} {{/list}}</html>',
            merge_variables={
                'list': [
                    { 'name': 'Larissa' },
                    { 'name': 'Larry' }
                ]
            }
        )
        self.assertEqual(postcard.to_address.id, self.addr.id)
        self.assertEqual(postcard.from_address.id, self.addr.id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_delete_postcard(self):
        postcard = lob.Postcard.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            front=open('tests/pdfs/pc.pdf', 'rb'),
            back=open('tests/pdfs/pc.pdf', 'rb')
        )
        deleted_response = lob.Postcard.delete(postcard.id)
        self.assertTrue(deleted_response.deleted)

    def test_create_postcard_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.create)

    def test_retrieve_postcard(self):
        postcard = lob.Postcard.retrieve(id=lob.Postcard.list().data[0].id)
        self.assertTrue(isinstance(postcard, lob.Postcard))

    def test_retrieve_postcard_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Postcard.retrieve, id='test')
