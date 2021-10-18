import unittest
import os
import lob


class CardFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_list_cards(self):
        cards = lob.Card.list()
        self.assertTrue(isinstance(cards.data[0], lob.Card))
        self.assertEqual(cards.object, 'list')

    def test_retrieve_card(self):
        card = lob.Card.retrieve(id=lob.Card.list().data[0].id)
        self.assertTrue(isinstance(card, lob.Card))

    def test_create_card(self):
        card = lob.Card.create(
            front=open('tests/pdfs/card.pdf', 'rb'),
            back=open('tests/pdfs/card.pdf', 'rb'),
            description='Card with a blank PDF file'
        )
        self.assertTrue(isinstance(card, lob.Card))

    def test_delete_card(self):
        card = lob.Card.create(
            front=open('tests/pdfs/card.pdf', 'rb'),
            back=open('tests/pdfs/card.pdf', 'rb'),
            description='Card with a blank PDF file'
        )
        deleted_response = lob.Card.delete(card.id)
        self.assertTrue(deleted_response.deleted)

    def test_update_card(self):
        card = lob.Card.create(
            front=open('tests/pdfs/card.pdf', 'rb'),
            back=open('tests/pdfs/card.pdf', 'rb'),
            description='Card with a blank PDF file'
        )
        updatedCard = lob.Card.update(card.id, description='updated description')
        self.assertEqual(updatedCard.description, 'updated description')