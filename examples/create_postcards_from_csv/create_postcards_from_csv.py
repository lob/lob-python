import sys, os
sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

import lob
import csv
import sys

lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

try:
    sys.argv[1]
except IndexError:
    print "Please provide an input CSV file as an argument."
    sys.exit()

with open(os.path.dirname(__file__) + '/postcard_front.html', 'r') as frontHtmlFile:
    frontHtml = frontHtmlFile.read()
    with open(os.path.dirname(__file__) + '/postcard_back.html', 'r') as backHtmlFile:
        backHtml = backHtmlFile.read()
        with open(sys.argv[1]) as f:
            for row in csv.reader(f):
                postcard = lob.Postcard.create(
                    to_address = {
                        'name': row[5],
                        'address_line1': row[6],
                        'address_line2': row[7],
                        'address_city': row[8],
                        'address_state': row[9],
                        'address_zip': row[10],
                        'address_country': row[11]
                    },
                    from_address = {
                        'name': 'Lob',
                        'address_line1': '123 Main Street',
                        'address_city': 'San Francisco',
                        'address_state': 'CA',
                        'address_zip': '94185',
                        'address_country': 'US'
                    },
                    setting = 1002,
                    front = frontHtml,
                    back = backHtml,
                    data = {
                        'background_image': row[1],
                        'background_color': row[2],
                        'name': row[0],
                        'car': row[3],
                        'mileage': row[4]
                    }
                )
                print postcard.url
