import unittest
import lob

class AreaFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'
        self.route = lob.Route.list(zip_codes=94158)

    def test_create_area_with_zip(self):
        area = lob.Area.create(
            description = 'area_test_zip',
            front = '<h1>Hi</h1>',
            back = '<h1>Goodbye</h1>',
            routes = ['94158','60031'],
            target_type = 'all'
        )
        self.assertTrue(isinstance(area, lob.Area))


    def test_create_area_with_route(self):
        area = lob.Area.create(
            description = 'area_test_route',
            front = '<h1>Hi</h1>',
            back = '<h1>Goodbye</h1>',
            routes = self.route,
            target_type = 'all'
        )
        self.assertTrue(isinstance(area, lob.Area))


    def test_create_area_local_file(self):
        area = lob.Area.create(
            description = 'area_local_file',
            front = open('tests/areafront.pdf', 'rb'),
            back = open('tests/areaback.pdf', 'rb'),
            routes = self.route,
            target_type = 'all'
        )
        self.assertTrue(isinstance(area, lob.Area))

    def test_create_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.create)

    def test_list_areas(self):
        areas = lob.Area.list()
        self.assertTrue(isinstance(areas.data[0], lob.Area))
        self.assertEqual(areas.object, 'list')

    def test_list_areas_limit(self):
        areas = lob.Area.list(limit=2)
        self.assertTrue(isinstance(areas.data[0], lob.Area))
        self.assertEqual(len(areas.data), 2)

    def test_list_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.list, limit=1000)

    def test_retrieve_area(self):
        area = lob.Area.retrieve(id=lob.Area.list().data[0].id)
        self.assertTrue(isinstance(area, lob.Area))

    def test_retrieve_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.retrieve, id='test')
