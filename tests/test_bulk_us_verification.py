import unittest
import os
import lob


class TestBulkUSVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_bulk_us_verification(self):
        response = lob.BulkUSVerification.create(
            addresses=[
                {
                    'primary_line': 'deliverable',
                    'city': 'San Francisco',
                    'state': 'CA',
                    'zip_code': '94107'
                }
            ]
        )

        addresses = response.addresses
        addr = addresses[0]

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '1 TELEGRAPH HILL BLVD')

    def test_bulk_us_verification_format(self):
        responses = lob.BulkUSVerification.create(
            addresses=[ 
                {
                    'primary_line': 'deliverable',
                    'city': 'San Francisco',
                    'state': 'CA',
                    'zip_code': '94107'
                }
            ],
            query={
                'case': 'proper'
            }
        )

        addresses = responses.addresses
        addr = addresses[0]

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '1 Telegraph Hill Blvd')
