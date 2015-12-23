import sys, os
sys.path.insert(0, os.path.abspath(__file__+'../../../..'))

import lob
import csv
import sys

lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

try:
    sys.argv[1]
except IndexError:
    print "Please provide an input CSV file as an argument."
    sys.exit()

with open(os.path.dirname(os.path.abspath(__file__)) + '/postcard_front.html', 'rb') as frontHtmlFile:
    frontHtml = frontHtmlFile.read()
    with open(os.path.dirname(os.path.abspath(__file__)) + '/postcard_back.html', 'rb') as backHtmlFile:
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
                    size: '6x11',
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
