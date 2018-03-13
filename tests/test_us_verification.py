import unittest
import lob


class TestUSVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_us_verification(self):
        addr = lob.USVerification.create(
            primary_line='deliverable',
            city='San Francisco',
            state='CA',
            zip_code='94107'
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
