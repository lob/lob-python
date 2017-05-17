import unittest
import lob

class TestUSVerificationFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_us_verification(self):
        addr = lob.USVerification.create(
            primary_line='185 Berry St Ste 6600',
            city='San Francisco',
            state='CA',
            zip_code='94107'
        )

        self.assertEqual(addr.deliverability, 'deliverable')
        self.assertEqual(addr.primary_line, '185 BERRY ST STE 6600')
