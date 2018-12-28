import unittest
import os
import lob


class TestIntlVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_intl_verification(self):
        try:
            lob.IntlVerification.create(
                primary_line='370 Water St',
                city='Summerside',
                state='Prince Edward Island',
                postal_code='C1N 1C4',
                country='CA'
            )
        except Exception as e:
            self.assertEqual(e.http_status, 403)
