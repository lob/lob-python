import unittest
import os
import lob


class BillingGroupFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_list_letters(self):
        # Validate the billing group API is set up on test account.
        pass
        '''letters = lob.BillingGroup.list()
        self.assertEqual(letters.object, 'list')'''

    def test_retrieve_letter(self):
        # Validate the billing group API is set up on test account.
        pass

    def test_create_letter(self):
        # Validate the billing group API is set up on test account.
        pass
