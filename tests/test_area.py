import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class AreaFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
        self.route = lob.Route.list(zip_codes=94158)

    def test_create_area_with_zip(self):
        area = lob.Area.create(
            name = 'area_test_zip',
            front = 'https://www.lob.com/areafront.pdf',
            back = 'https://www.lob.com/areaback.pdf',
            routes = ['94158','60031'],
            target_type = 'all',
            full_bleed = '1'
        )
        self.assertTrue(isinstance(area, lob.Area))


    def test_create_area_with_route(self):
        area = lob.Area.create(
            name = 'area_test_route',
            front = 'https://www.lob.com/areafront.pdf',
            back = 'https://www.lob.com/areaback.pdf',
            routes = self.route,
            target_type = 'all',
            full_bleed = '1'
        )
        self.assertTrue(isinstance(area, lob.Area))


    def test_create_area_local_file(self):
        area = lob.Area.create(
            name = 'area_local_file',
            front = open('tests/areafront.pdf', 'rb'),
            back = open('tests/areaback.pdf', 'rb'),
            routes = self.route,
            target_type = 'all',
            full_bleed = '1'
        )
        self.assertTrue(isinstance(area, lob.Area))

    def test_create_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.create)

    def test_list_areas(self):
        areas = lob.Area.list()
        self.assertTrue(isinstance(areas.data[0], lob.Area))
        self.assertEqual(areas.object, 'list')

    def test_list_areas_limit(self):
        areas = lob.Area.list(count=2)
        self.assertTrue(isinstance(areas.data[0], lob.Area))
        self.assertEqual(len(areas.data), 2)

    def test_list_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.list, count=1000)

    def test_retrieve_area(self):
        area = lob.Area.retrieve(id=lob.Area.list().data[0].id)
        self.assertTrue(isinstance(area, lob.Area))

    def test_retrieve_area_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Area.retrieve, id='test')
