import unittest

import lob
from lob.compat import BytesIO
# Setting the API key
lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'


class ObjectFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'
        self.obj = lob.Object.list(count=1).data[0]

    def test_list_objects(self):
        objects = lob.Object.list()
        self.assertTrue(isinstance(objects.data[0], lob.Object))
        self.assertEqual(objects.object, 'list')

    def test_list_objects_limit(self):
        objects = lob.Object.list(count=2)
        self.assertTrue(isinstance(objects.data[0], lob.Object))
        self.assertEqual(len(objects.data), 2)

    def test_list_objects_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Object.list, count=1000)

    def test_create_object_remote(self):
        object = lob.Object.create(
            description = 'Test Object',
            file = 'https://lob.com/postcardfront.pdf',
            setting = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.description, 'Test Object')

    def test_create_object_stringio(self):
        object = lob.Object.create(
            description = 'Test Object BytesIO',
            file = BytesIO(open('tests/pc.pdf', 'rb').read()),
            setting = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.description, 'Test Object BytesIO')

    def test_create_object_local(self):
        object = lob.Object.create(
            description = 'Test Object Inline',
            file = open('tests/pc.pdf', 'rb'),
            setting = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.description, 'Test Object Inline')
        self.assertRaises(AttributeError, lambda: object.nonexistent_key)

        object.description = "something new"
        self.assertEqual(object.description, "something new")

    def test_create_directly_specify_files(self):
        object = lob.Object.create(
            description = 'Test Object Direct Specify',
            files = {'file': open('tests/pc.pdf', 'rb').read()},
            setting = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.description, 'Test Object Direct Specify')

    def test_create_object_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Object.create)

    def test_retrieve_job(self):
        job = lob.Object.retrieve(id=lob.Object.list().data[0].id)
        self.assertTrue(isinstance(job, lob.Object))

    def test_retrieve_job_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Object.retrieve, id='test')
