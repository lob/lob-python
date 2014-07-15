from lob import api_requestor
import json

def lob_format(resp):
    types = {
        'address': Address,
        'bank_account': BankAccount,
        'check': Check,
        'job': Job,
        'object': Object,
        'postcard': Postcard
    }

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
            raise AttributeError(k)

    def __setattr__(self, k, v):
        self[k] = v

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), basestring):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), basestring):
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

class BankAccount(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/bank_accounts'

class Object(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/objects'

class Check(ListableAPIResource, CreateableAPIResource):
    url = '/checks'

class Postcard(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/postcards'

class Job(ListableAPIResource, DeleteableAPIResource, CreateableAPIResource):
    url = '/jobs'
    @classmethod
    def create(cls, **params):
        if not isinstance(params['objects'], list):
            params['objects'] = [params['objects']]
        i = 1
        for obj in params['objects']:
            params['object' + str(i)] = obj
            i = i + 1
        params.pop('objects', None)
        return super(Job, cls).create(**params)

class Packaging(ListableAPIResource):
    url='/packagings'

class Service(ListableAPIResource):
    url = '/services'

class Setting(ListableAPIResource):
    url = '/settings'

class State(ListableAPIResource):
    url = '/states'

class Country(ListableAPIResource):
    url = '/countries'

class Verification(CreateableAPIResource):
    url = '/verify'
