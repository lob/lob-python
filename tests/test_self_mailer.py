import unittest
import os
import lob


class SelfMailerFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')
        self.addr = lob.Address.list(limit=1).data[0]

    def test_list_self_mailers(self):
        self_mailers = lob.SelfMailer.list()
        self.assertTrue(isinstance(self_mailers.data[0], lob.SelfMailer))
        self.assertEqual(self_mailers.object, 'list')

    def test_list_self_mailers_limit(self):
        self_mailers = lob.SelfMailer.list(limit=2)
        self.assertTrue(isinstance(self_mailers.data[0], lob.SelfMailer))
        self.assertEqual(len(self_mailers.data), 2)

    def test_list_self_mailers_metadata(self):
        self_mailers = lob.SelfMailer.list(metadata={'campaign': 'LOB-TEST'})
        self.assertTrue(isinstance(self_mailers.data[0], lob.SelfMailer))
        self.assertTrue(len(self_mailers.data) > 0)

    def test_list_self_mailers_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.SelfMailer.list, limit=1000)

    def test_create_self_mailer(self):
        self_mailer = lob.SelfMailer.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            description='Test Self Mailer - Metadata',
            outside='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/6x18_sfm_outside.pdf',
            inside='<h1>Hello, {{inside_name}}</h1>',
            merge_variables={
                'inside_name': 'World'
            }
        )
        self.assertEqual(self_mailer.to_address.id, self.addr.id)
        self.assertEqual(self_mailer.from_address.id, self.addr.id)
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_create_idempotent_self_mailers(self):
        idempotency_key = "Test_Idempotency_Key"
        self_mailer_one = lob.SelfMailer.create(
            to_address=self.addr.id,
            description='Test Self Mailer',
            outside='<h1>Outside</h1>',
            inside='<h1>Inside</h1>',
            headers={
                'Idempotency-Key': idempotency_key
            }
        )

        self_mailer_two = lob.SelfMailer.create(
            to_address=self.addr.id,
            description='Test Self Mailer',
            outside='<h1>Outside</h1>',
            inside='<h1>Inside</h1>',
            headers={
                'Idempotency-Key': idempotency_key
            }
        )

        self.assertEqual(self_mailer_one.id, self_mailer_two.id)
        self.assertTrue(isinstance(self_mailer_one, lob.SelfMailer))

    def test_create_self_mailer_inline_address(self):
        self_mailer = lob.SelfMailer.create(
            description='Test Self Mailer',
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
                'address_state': 'CA',
                'metadata': {
                    'department': 'marketing'
                }
            },
            outside='<h1>{{outside_name}}</h1>',
            inside='<h1>{{inside_name}}</h1>',
            merge_variables={
                'outside_name': 'Peter',
                'inside_name': 'Otto'
            }
        )
        self.assertEqual(self_mailer.to_address.name, 'LOB1')
        self.assertEqual(self_mailer.from_address.name, 'Lob2')
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_create_self_mailer_local_file(self):
        self_mailer = lob.SelfMailer.create(
            description='Test Self Mailer',
            to_address=self.addr.id,
            from_address=self.addr.id,
            outside=open('tests/pdfs/sfm-6x18-outside.pdf', 'rb'),
            inside=open('tests/pdfs/sfm-6x18-inside.pdf', 'rb')
        )
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_create_self_mailer_local_file_12x9_bifold(self):
        self_mailer = lob.SelfMailer.create(
            description='Test Self Mailer',
            to_address=self.addr.id,
            from_address=self.addr.id,
            size='12x9_bifold',
            outside=open('tests/pdfs/sfm-12x9-outside.pdf', 'rb'),
            inside=open('tests/pdfs/sfm-12x9-inside.pdf', 'rb')
        )
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_create_self_mailer_with_merge_variable(self):
        self_mailer = lob.SelfMailer.create(
            description='Test Self Mailer',
            to_address=self.addr.id,
            from_address=self.addr.id,
            outside='<html>{{#list}} {{name}} {{/list}}</html>',
            inside='<html>{{#list}} {{name}} {{/list}}</html>',
            merge_variables={
                'list': [
                    { 'name': 'Larissa' },
                    { 'name': 'Larry' }
                ]
            }
        )
        self.assertEqual(self_mailer.to_address.id, self.addr.id)
        self.assertEqual(self_mailer.from_address.id, self.addr.id)
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_delete_self_mailer(self):
        self_mailer = lob.SelfMailer.create(
            to_address=self.addr.id,
            from_address=self.addr.id,
            outside='<h1>Test outside</h1>',
            inside='<h1>Test inside</h1>'
        )
        deleted_response = lob.SelfMailer.delete(self_mailer.id)
        self.assertTrue(deleted_response.deleted)

    def test_create_self_mailer_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.SelfMailer.create)

    def test_retrieve_self_mailer(self):
        self_mailer = lob.SelfMailer.retrieve(id=lob.SelfMailer.list().data[0].id)
        self.assertTrue(isinstance(self_mailer, lob.SelfMailer))

    def test_retrieve_self_mailer_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.SelfMailer.retrieve, id='test')
