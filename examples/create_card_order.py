from __future__ import print_function

import sys
import os

# Load lob-python root directory into the import path so you can use the lob package without having to install it through pip.
sys.path.insert(0, os.path.abspath(__file__+'../../..'))
import lob

# Replace this API key with your own.
lob.api_key = 'YOUR_API_KEY'

# Replace this with the Card ID you'd like to place the order for
card_id = 'YOUR_CARD_ID'

# The minimum order size is 10,000 cards
example_card_order = lob.CardOrder.create(card_id,
  quantity_ordered="10000"
)

print("Card Response")
print("\n")
print("=======================================================")
print("\n")
print(example_card_order)
print("\n")
print("=======================================================")
print("\n")
