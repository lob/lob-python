import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class BankAccountFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_list_bank_accounts(self):
        print lob.BankAccount.list()


    def test_create_bank_account(self):
        print lob.BankAccount.create(
                routing_number='122100024',
                account_number='123456789',
                bank_address=lob.Address.list(count=1, offset=4).data[0].id,
                account_address=lob.Address.list(count=1).data[0].id,
                bank_code=None)

        def test_create_inline_bank_account(self):
            print lob.BankAccount.create(
                    routing_number='122100024',
                    account_number='123456789',
                    bank_address={
                        'name': 'Lob',
                        'address_line1': '185 Berry Street',
                        'address_city': 'San Francisco',
                        'address_state': 'CA',
                        'address_zip': '94107',
                        'address_country': 'US'
                        },
                    account_address={
                        'name': 'Lob',
                        'address_line1': '185 Berry Street',
                        'address_city': 'San Francisco',
                        'address_state': 'CA',
                        'address_zip': '94107',
                        'address_country': 'US'
                        })

        def test_find_bank_account(self):
            print lob.BankAccount.retrieve(id=lob.BankAccount.list(count=1).data[0].id)

        def test_delete_bank_account(self):
            print lob.BankAccount.delete(id=lob.BankAccount.list(count=1).data[0].id)
