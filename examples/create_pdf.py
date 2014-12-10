import lob
import pdfkit

lob.api_key = "test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc" # Replace this API key with your own.

body = """
    <html>
        <body>
            <div style="text-align: center; color: blue;" />
                <img src="https://s3-us-west-2.amazonaws.com/lob-assets/LobLogoBlueTrans.png" />
                <h1>Print with Lob</h1>
            </div>
        </body>
    </html>
"""

pdfkit.from_string(body, 'out.pdf', {
    'page-height': '6.25in',
    'page-width': '4.25in',
    'quiet': ''
})

example_object = lob.Object.create(
    name='Example Object',
    file=open('out.pdf', 'rb'),
    setting_id=201,
    full_bleed=1
)

print "Check out the created PDF here: " + example_object.url
