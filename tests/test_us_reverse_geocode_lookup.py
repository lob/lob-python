import unittest
import os
import lob


class TestUSReverseGeocodeLookupFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_us_zip_lookup(self):
        reverse_geocode_lookup = lob.USReverseGeocodeLookup.create(
            latitude=37.777456,
            longitude=-122.393039
        )

        self.assertTrue(reverse_geocode_lookup.addresses[0].components.zip_code =='94102' or reverse_geocode_lookup.addresses[0].components.zip_code =='94103')
