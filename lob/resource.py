from __future__ import unicode_literals

import json

from lob import api_requestor
from lob.compat import string_type


def lob_format(resp):
    types = {
        'address': Address,
        'bank_account': BankAccount,
        'card': Card,
        'card_order': CardOrder,
        'check': Check,
        'letter': Letter,
        'postcard': Postcard,
        'self_mailer': SelfMailer
    }

    # Change Keys for To/From
    if isinstance(resp, dict) and 'to' in resp:
        resp['to_address'] = resp['to']
        resp.pop('to', None)
    if isinstance(resp, dict) and 'from' in resp:
        resp['from_address'] = resp['from']
        resp.pop('from', None)

    # Recursively Set Objects for Lists
    if isinstance(resp, dict) and 'object' in resp and resp['object'] == 'list':
        resp['data'] = [lob_format(i) for i in resp['data']]
        return LobObject.construct_from(resp)
    if isinstance(resp, dict) and not isinstance(resp, LobObject):
        resp = resp.copy()
        if 'object' in resp and isinstance(resp['object'], string_type):
            klass = types.get(resp['object'], LobObject)
        else:
            klass = LobObject

        # Check For Arrays
        for key in resp:
            if isinstance(resp[key], list):
                resp[key] = [lob_format(i) for i in resp[key]]
        return klass.construct_from(resp)
    else:
        return resp


class LobObject(dict):

    def __init__(self, id=None, **params):
        super(LobObject, self).__init__()
        if id:
            self['id'] = id

    @classmethod
    def construct_from(cls, values):
        instance = cls(values.get('id'))
        for k, v in values.items():
            instance[k] = lob_format(v)
        return instance

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)  # pragma: no cover

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), string_type):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), string_type):
            ident_parts.append('id=%s' % (self.get('id'),))

        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts), hex(id(self)), str(self))

        return unicode_repr

    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2)


class APIResource(LobObject):
    @classmethod
    def retrieve(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s' % (cls.endpoint, id), params)
        return lob_format(response)


# API Operations
class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        for key, value in params.copy().items():
            if isinstance(params[key], dict):
                for subKey in value:
                    params[str(key) + '[' + subKey + ']'] = value[subKey]
                del params[key]
            elif isinstance(params[key], list):
                params[str(key) + '[]'] = params[key]
                del params[key]
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return lob_format(response)


class DeleteableAPIResource(APIResource):
    @classmethod
    def delete(cls, id):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('delete', '%s/%s' % (cls.endpoint, id))
        return lob_format(response)


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('post', cls.endpoint, params)
        return lob_format(response)


class VerifiableAPIResource(APIResource):
    @classmethod
    def verify(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('post', '%s/%s/verify' % (cls.endpoint, id), params)
        return lob_format(response)


class Address(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    endpoint = '/addresses'


class BankAccount(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource, VerifiableAPIResource):
    endpoint = '/bank_accounts'

class BulkIntlVerification(CreateableAPIResource):
    endpoint = '/bulk/intl_verifications'

class BulkUSVerification(CreateableAPIResource):
    endpoint = '/bulk/us_verifications'

class Card(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    endpoint = '/cards'

class CardOrder(ListableAPIResource, CreateableAPIResource):
    endpoint = '/cards/%s/orders'

    @classmethod
    def create(cls, card_id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('post', cls.endpoint % card_id, params)
        return lob_format(response)

    @classmethod
    def list(cls, card_id, **params):
        for key, value in params.copy().items():
            if isinstance(params[key], dict):
                for subKey in value:
                    params[str(key) + '[' + subKey + ']'] = value[subKey]
                del params[key]
            elif isinstance(params[key], list):
                params[str(key) + '[]'] = params[key]
                del params[key]
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint % card_id, params)
        return lob_format(response)


class Check(ListableAPIResource, CreateableAPIResource, DeleteableAPIResource):
    endpoint = '/checks'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
        return super(Check, cls).create(**params)


class Letter(ListableAPIResource, CreateableAPIResource, DeleteableAPIResource):
    endpoint = '/letters'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Letter, cls).create(**params)


class Postcard(ListableAPIResource, CreateableAPIResource, DeleteableAPIResource):
    endpoint = '/postcards'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Postcard, cls).create(**params)

class SelfMailer(ListableAPIResource, CreateableAPIResource, DeleteableAPIResource):
    endpoint = '/self_mailers'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(SelfMailer, cls).create(**params)


class USAutocompletion(CreateableAPIResource):
    endpoint = '/us_autocompletions'

class USReverseGeocodeLookup(CreateableAPIResource):
    endpoint = '/us_reverse_geocode_lookups'

class USVerification(CreateableAPIResource):
    endpoint = '/us_verifications'


class USZipLookup(CreateableAPIResource):
    endpoint = '/us_zip_lookups'


class IntlVerification(CreateableAPIResource):
    endpoint = '/intl_verifications'
