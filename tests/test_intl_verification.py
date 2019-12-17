import unittest
import os
import lob


class TestIntlVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_intl_verification(self):
        lob.IntlVerification.create(
            primary_line='deliverable',
            country='CA'
        )

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '370 WATER ST')
