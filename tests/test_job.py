import unittest
import lob

class JobFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'
        self.obj = lob.Object.list(count=1).data[0]
        self.addr = lob.Address.list(count=1).data[0]

    def test_list_jobs(self):
        jobs = lob.Job.list()
        self.assertTrue(isinstance(jobs.data[0], lob.Job))
        self.assertEqual(jobs.object, 'list')

    def test_list_jobs_limit(self):
        jobs = lob.Job.list(count=2)
        self.assertTrue(isinstance(jobs.data[0], lob.Job))
        self.assertEqual(len(jobs.data), 2)

    def test_list_jobs_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Job.list, count=1000)

    def test_create_job(self):
        job = lob.Job.create(
            to_address = self.addr.id,
            from_address = self.addr.id,
            objects = self.obj.id
        )
        self.assertEqual(job.to_address.id, self.addr.id)
        self.assertEqual(job.from_address.id, self.addr.id)
        self.assertEqual(job.objects[0].id, self.obj.id)
        self.assertTrue(isinstance(job, lob.Job))


    def test_create_job_lob_obj(self):
        job = lob.Job.create(
            to_address = self.addr,
            from_address = self.addr,
            objects = self.obj
        )
        self.assertEqual(job.to_address.id, self.addr.id)
        self.assertEqual(job.from_address.id, self.addr.id)
        self.assertEqual(job.objects[0].id, self.obj.id)
        self.assertTrue(isinstance(job, lob.Job))

    def test_create_job_inline(self):
        job = lob.Job.create(
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
            objects = {
                'description': 'Object1',
                'file': '<h1>{{name}}</h1>',
                'data': {
                    'name': 'Peter'
                },
                'setting': '201'
            }
        )
        self.assertEqual(job.to_address.name, 'Lob1')
        self.assertEqual(job.from_address.name, 'Lob2')
        self.assertEqual(job.objects[0].description, 'Object1')
        self.assertTrue(isinstance(job, lob.Job))

    def test_create_job_multi_object(self):
        job = lob.Job.create(
            to_address = self.addr.id,
            from_address = self.addr.id,
            objects = [
                {
                    'description': 'Test Job',
                    'file': '<h1>{{name}}</h1>',
                    'data': {
                        'name': 'Peter'
                    },
                    'setting': 201,
                    'quantity': 2
                }
            ]
        )
        self.assertEqual(job.to_address.id, self.addr.id)
        self.assertEqual(job.from_address.id, self.addr.id)
        self.assertEqual(job.objects[0].quantity, 2)
        self.assertTrue(isinstance(job, lob.Job))

    def test_create_job_local_file(self):
        job = lob.Job.create(
            to_address = self.addr.id,
            from_address = self.addr.id,
            objects = {
                'description': 'Test Job',
                'file': open('tests/pc.pdf', 'rb'),
                'setting': 201
            }
        )
        self.assertEqual(job.objects[0].description, 'Test Job')
        self.assertTrue(isinstance(job, lob.Job))

    def test_create_job_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Job.create)

    def test_create_job_address_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Job.create,
            to_address = self.addr,
            from_address = {
                'name': 'Test'
            },
            objects = self.obj.id
        )

    def test_retrieve_job(self):
        job = lob.Job.retrieve(id=lob.Job.list().data[0].id)
        self.assertTrue(isinstance(job, lob.Job))

    def test_retrieve_job_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Job.retrieve, id='test')
