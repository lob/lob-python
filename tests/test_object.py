import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class ObjectFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
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
            name = 'Test Object',
            file = 'https://www.lob.com/test.pdf',
            setting_id = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.name, 'Test Object')

    def test_create_object_local(self):
        object = lob.Object.create(
            name = 'Test Object Inline',
            file = open('tests/pc.pdf', 'rb'),
            setting_id = 201
        )

        self.assertTrue(isinstance(object, lob.Object))
        self.assertEqual(object.name, 'Test Object Inline')
        self.assertRaises(KeyError, lambda: object.nonexistent_key)

    def test_create_object_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Object.create)

    def test_retrieve_job(self):
        job = lob.Object.retrieve(id=lob.Object.list().data[0].id)
        self.assertTrue(isinstance(job, lob.Object))

    def test_retrieve_job_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Object.retrieve, id='test')
