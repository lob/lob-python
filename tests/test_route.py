from __future__ import print_function

import unittest
import lob
# Setting the API key
lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

class RouteTest(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_route_find(self):
        print(lob.Route.list(zip_codes=[94158,60031]))
