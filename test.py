import lob
lob.api_key = 'test_316e28feabd9acf1bb9ccd7c2bdf28b9137'
print lob.Address.get(id=str(lob.Address.list(count=1).data[0].id))
#print lob.Address.list(count=1).data[0].id
# addr = lob.Address.list().data[4]
# ba = lob.BankAccount.create(
#       name='Bank Account',
#       routing_number=123456,
#       account_number=12456,
#       bank_address=addr,
#       account_address={
#         'name':'Peter Nagel',
#         'address_line1':'185 Berry Street',
#         'address_line2':'Suite 1510',
#         'address_city':'San Francisco',
#         'address_zip':'94107',
#         'address_state':'CA'
#       })
#
# ch = lob.Check.create(
#       name='Demo Check',
#       bank_account=ba,
#       to={
#         'name':'Peter Nagel',
#         'address_line1':'185 Berry Street',
#         'address_line2':'Suite 1510',
#         'address_city':'San Francisco',
#         'address_zip':'94107',
#         'address_state':'CA'
#       },
#       amount=30,
#       message='from python'
# )
#
# pc = lob.Postcard.create(
#       name='Demo Postcard',
#       message='Hello',
#       to=addr,
#       front='https://www.lob.com/postcardfront.pdf',
#       from_address={
#         'name':'Amrit Ayalur',
#         'address_line1':'7726 Dada Dr',
#         'address_city':'Gurnee',
#         'address_zip':'60031',
#         'address_state':'IL'
#       })
#
# print lob.Address.get(id=lob.Address.list(count=1).data[0].id).to_dict()
# #print lob.Address.list(count=1).data[0].id
