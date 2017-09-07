import unittest
import lob

class TestIntlVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_intl_verification(self):
        try:
            addr = lob.IntlVerification.create(
                primary_line='370 Water St',
                city='Summerside',
                state='Prince Edward Island',
                postal_code='C1N 1C4',
                country='CA'
            )
        except Exception as e:
            self.assertEqual(e.http_status, 403)
