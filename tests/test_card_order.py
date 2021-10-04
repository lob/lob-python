import unittest
import os
import lob


class CardOrderFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(CardOrderFunctions, cls).setUpClass()
        lob.api_key = os.environ.get('LOB_API_KEY')
        cls.card = lob.Card.create(
            front=open('tests/pdfs/card.pdf', 'rb'),
            back=open('tests/pdfs/card.pdf', 'rb'),
            description='Card with a blank PDF file',
            size='2.125x3.375'
        )

    def test_create_card_order(self):        
        cardOrder = lob.CardOrder.create(CardOrderFunctions.card.get('id'),
            quantity_ordered='10000'
        )
        self.assertTrue(isinstance(cardOrder, lob.CardOrder))

    def test_list_card_orders(self):
        cardOrders = lob.CardOrder.list(CardOrderFunctions.card.get('id'))
        print(cardOrders)
        self.assertTrue(isinstance(cardOrders.data[0], lob.CardOrder))
        self.assertEqual(cardOrders.object, 'list')
