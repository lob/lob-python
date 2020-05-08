import unittest
import os
import lob


class TestUSVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_us_verification(self):
        addr = lob.USVerification.create(
            primary_line='deliverable',
            city='San Francisco',
            state='CA',
            zip_code='94107'
        )

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '1 TELEGRAPH HILL BLVD')

    def test_us_verification_override_lob_version(self):
        addr = lob.USVerification.create(
            primary_line='deliverable',
            city='San Francisco',
            state='CA',
            zip_code='94107',
            lob_version='2020-02-11'
        )

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '1 TELEGRAPH HILL BLVD')

    def test_us_verification_format(self):
        addr = lob.USVerification.create(
            primary_line='deliverable',
            city='San Francisco',
            state='CA',
            zip_code='94107',
            query={
                'case': 'proper'
            }
        )

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '1 Telegraph Hill Blvd')
