import lob
import unittest
# Setting the API key

class CheckFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_list_checks(self):
        print lob.Check.list()

    def test_create_check(self):
        print lob.Check.create(
                bank_account=lob.BankAccount.list(count=1).data[0].id,
                to=lob.Address.list(count=1).data[0].id,
                amount=100,
                name='Test Check',
                message='Testing Check',
                memo='Testing'
                )

        def test_inline_create_check(self):
            to_address = {
                    'name': 'Ralph Receiver',
                    'address_line1': '1234 E Grant St',
                    'address_line2': None,
                    'address_city': 'Tucson',
                    'address_state': 'AZ',
                    'address_country': 'US',
                    'address_zip': '85712'
                    }

            print lob.Check.create(
                    bank_account=lob.BankAccount.list(count=1).data[0].id,
                    to=to_address,
                    amount=1000.00,
                    name='Demo Check',
                    check_number=None,
                    message='Hi Ralph. Thanks for your work. - Paul',
                    memo='Services rendered.'
                    )

            def test_find_check(self):
                print lob.Check.retrieve(id=lob.Check.list(count=1).data[0].id)
