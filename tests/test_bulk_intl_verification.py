import unittest
import os
import lob


class TestBulkIntlVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_bulk_intl_verification(self):
        response = lob.BulkIntlVerification.create(
            addresses=[
                {
                    'primary_line': 'deliverable',
                    'country': 'CA'
                }
            ]
        )

        addresses = response.addresses
        addr = addresses[0]
        print(addr)
        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '370 WATER ST')
