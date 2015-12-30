from __future__ import unicode_literals

import json

from lob import api_requestor
from lob import error
from lob.compat import string_type


def lob_format(resp):
    types = {
        'address': Address,
        'area': Area,
        'bank_account': BankAccount,
        'check': Check,
        'country': Country,
        'job': Job,
        'letter' : Letter,
        'object': Object,
        'postcard': Postcard,
        'state': State
    }

    #Change Keys for To/From
    if isinstance(resp, dict) and 'to' in resp:
        resp['to_address'] = resp['to']
        resp.pop('to', None)
    if isinstance(resp, dict) and 'from' in resp:
        resp['from_address'] = resp['from']
        resp.pop('from', None)

    #Recursively Set Objects for Lists
    if isinstance(resp, dict) and 'object' in resp and resp['object'] == 'list':
        resp['data'] = [lob_format(i) for i in resp['data']]
        return LobObject.construct_from(resp)
    if isinstance(resp, dict) and not isinstance(resp, LobObject):
        resp = resp.copy()
        if 'object' in resp and isinstance(resp['object'], string_type):
            klass = types.get(resp['object'], LobObject)
        else:
            klass = LobObject

        #Check For Arrays
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
            raise AttributeError(k) #pragma: no cover

    def __setattr__(self, k, v):
        self[k] = v

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
        for key, value in params.items():
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

class Area(ListableAPIResource, CreateableAPIResource):
    endpoint = '/areas'
    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'routes' in params:
                if isinstance(params['routes'], LobObject):
                    routes = []
                    for r in params['routes'].data[0]['routes']:
                        routes.append(params['routes'].data[0]['zip_code'] + '-' + r["route"])
                    params['routes'] = routes
        return super(Area, cls).create(**params)

class BankAccount(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource, VerifiableAPIResource):
    endpoint = '/bank_accounts'

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


class Country(ListableAPIResource):
    endpoint = '/countries'

class Job(ListableAPIResource, CreateableAPIResource):
    endpoint = '/jobs'
    @classmethod
    def create(cls, **params):
        if 'from_address' not in params or 'to_address' not in params or 'objects' not in params:
            raise error.InvalidRequestError('from_address, to_address, and objects are required')
        params['from'] = params['from_address']
        params.pop('from_address')
        params['to'] = params['to_address']
        params.pop('to_address')
        if not isinstance(params['objects'], list):
            params['objects'] = [params['objects']]
        i = 1
        for obj in params['objects']:
            params['object' + str(i)] = obj
            i = i + 1
        params.pop('objects', None)
        return super(Job, cls).create(**params)

class Letter(ListableAPIResource, CreateableAPIResource):
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

class Object(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    endpoint = '/objects'

class Postcard(ListableAPIResource, CreateableAPIResource):
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

class Route(ListableAPIResource):
    endpoint = '/routes'

class Setting(ListableAPIResource):
    endpoint = '/settings'

class State(ListableAPIResource):
    endpoint = '/states'

class Verification(CreateableAPIResource):
    endpoint = '/verify'
