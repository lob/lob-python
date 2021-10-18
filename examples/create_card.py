from __future__ import print_function

import sys
import os

# Load lob-python root directory into the import path so you can use the lob package without having to install it through pip.
sys.path.insert(0, os.path.abspath(__file__+'../../..'))
import lob

# Replace this API key with your own.
lob.api_key = 'YOUR_API_KEY'

# Creating a Card

def readPDFFile():
  script_dir = os.path.dirname(__file__)
  path = 'cards/card.pdf'
  abs_path = os.path.join(script_dir, path)

  return open(abs_path, 'rb')

example_card = lob.Card.create(
    front=readPDFFile(),
    back=readPDFFile(),
    description='Card with a blank front and back',
    size='2.125x3.375',
)

print("Card Response")
print("\n")
print("=======================================================")
print("\n")
print(example_card)
print("\n")
print("=======================================================")
print("\n")

# Updating a card
# updatedCard = lob.Card.update(example_card.id, description='This is a new description')

# Deleting a card
# deletedCard = lob.Card.delete(example_card.id)