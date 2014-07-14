# Lob Python Library

__version__ = '1.0'
__author__ = 'Siddharth Saha (sidchilling@gmail.com)'

# Imports
import logging
import importer
import types
from exceptions import (
    APIError, APIConnectionError,
    InvalidRequestError, AuthenticationError
    )

json = importer.import_json()
_httplib, httplib = importer.import_requests()

log = logging.getLogger('lob')

# Could be set globally
api_key = None

# Resources
from lob.resource import (Address,BankAccount,Object,Check,Postcard,Job,Packaging,
  Service,Setting,State,Country,Verification)

from lob.version import VERSION
