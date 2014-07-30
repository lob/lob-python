from lob import api_requestor
from lob import error
import json

def lob_format(resp):
    types = {
        'address': Address,
        'area': Area,
        'bank_account': BankAccount,
        'check': Check,
        'job': Job,
        'object': Object,
        'postcard': Postcard
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
        if 'object' in resp and isinstance(resp['object'], basestring):
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
        for k, v in values.iteritems():
            instance[k] = lob_format(v)
        return instance

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError, err:
            raise AttributeError(k) #pragma: no cover

    def __setattr__(self, k, v):
        self[k] = v

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), basestring):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), basestring): #pragma: no cover
            ident_parts.append('id=%s' % (self.get('id'),)) #pragma: no cover

        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts), hex(id(self)), str(self))

        return unicode_repr

    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2)

class APIResource(LobObject):
    @classmethod
    def retrieve(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s' % (cls.url, id), params)
        return lob_format(response)

# API Operations
class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.url, params)
        return lob_format(response)

class DeleteableAPIResource(APIResource):
    @classmethod
    def delete(cls, id):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('delete', '%s/%s' % (cls.url, id))
        return lob_format(response)

class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('post', cls.url, params)
        return lob_format(response)

class Address(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/addresses'

class Area(ListableAPIResource, CreateableAPIResource):
    url = '/areas'
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

class BankAccount(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/bank_accounts'

class Check(ListableAPIResource, CreateableAPIResource):
    url = '/checks'
    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Check, cls).create(**params)


class Country(ListableAPIResource):
    url = '/countries'

class Job(ListableAPIResource, CreateableAPIResource):
    url = '/jobs'
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

class Object(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/objects'

class Postcard(ListableAPIResource, CreateableAPIResource):
    url = '/postcards'
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


class Packaging(ListableAPIResource):
    url='/packagings'

class Route(ListableAPIResource):
    url='/routes'

class Service(ListableAPIResource):
    url = '/services'

class Setting(ListableAPIResource):
    url = '/settings'

class State(ListableAPIResource):
    url = '/states'

class Verification(CreateableAPIResource):
    url = '/verify'
