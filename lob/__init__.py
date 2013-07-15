# Lob Python Library

__version__ = '1.0'
__author__ = 'Siddharth Saha (sidchilling@gmail.com)'

# Imports
import logging
import importer
from exceptions import *

json = importer.import_json()
_httplib, httplib = importer.import_requests()

log = logging.getLogger('lob')

# Could be set globally
api_key = None

class LobRequestor(object):
    _api_base_url = 'https://api.lob.com/v1/'
    _api_key = None
    
    # Define the method function map - TODO: have to do for urlfetch
    _method_fn_map = {
            'GET' : httplib.get,
            'POST' : httplib.post,
            'PUT' : httplib.put,
            'HEAD' : httplib.head,
            'DELETE' : httplib.delete
            }

    def __init__(self):
        self._api_key = api_key

    def _make_requests_request(self, method, url_suffix, data):
        r = self._method_fn_map.get(method)(url = '%s%s' %(self._api_base_url, url_suffix), 
                data = data, auth = (self._api_key, ''))
        content = json.loads(r.content)
        error = content.get('error', content.get('errors', [])) # if any error
        if r.status_code == 200:
            return content
        elif r.status_code in [400, 422]:
            raise InvalidRequestError(error = error, http_body = r.text, 
                    http_status = r.status_code, json_body = content)
        elif r.status_code == 401:
            raise AuthenticationError(error = error, http_body = r.text, 
                    http_status = r.status_code, json_body = content)
        elif r.status_code == 404:
            raise APIConnectionError(error = error, http_body = r.text,
                    http_status = r.status_code, json_body = content)
        else:
            raise APIError(error = error, http_body = r.text,
                    http_status = r.status_code, json_body = content)
            

    def make_request(self, method, url_suffix, data = {}):
        if _httplib == 'requests':
            return self._make_requests_request(method = method, url_suffix = url_suffix, data = data)

def make_lob_object(response):
    '''This function converts the response to a LobObject and returns it
    '''
    types = {
            'service' : Service,
            'address' : Address,
            'packaging' : Packaging,
            'setting' : Setting,
            'object' : Object,
            'job' : Job,
            'postcard' : Postcard
            }
    if not response:
        return None
    if isinstance(response, list):
        return [make_lob_object(response = data) for data in response]
    if not response.get('object', None):
        # object info not present so will make LobObject with constituents objects
        data = {}
        for key in response.keys():
            if isinstance(response[key], dict):
                data[key] = make_lob_object(response = response.get(key))
            else:
                data[key] = response.get(key)
        return LobObject(data)
    if response.get('object') == 'list':
        # list to be returned
        return [make_lob_object(response = data) for data in response.get('data')]
    else:
        return types.get(response.get('object', ''), LobObject)(response)

# API Objects

class LobObject(object):
    # Have to implement the to_dict() method which will convert to dict
    
    def __setattr__(self, k, v):
        self._values.add(k)
        super.__setattr__(self, k, v)

    def __init__(self, data):
        self.__dict__['_values'] = set()
        for key in data:
            # HACK: required for variables named from (as it is a key word)
            attribute_key = key
            if attribute_key == 'from':
                attribute_key = 'from_address'
            if isinstance(data.get(key), dict):
                setattr(self, attribute_key, make_lob_object(data.get(key)))
            elif isinstance(data.get(key), list):
                setattr(self, attribute_key, 
                        [make_lob_object(response = el) for el in data.get(key)])
            else:
                setattr(self, attribute_key, data.get(key))
    
    def to_dict(self):
        def _serialize(o):
            if isinstance(o, LobObject):
                return o.to_dict()
            if isinstance(o, list):
                return [_serialize(i) for i in o]
            return o

        d = {}
        for k in sorted(self._values):
            v = getattr(self, k)
            v = _serialize(v)
            d[k] = v
        return d

    @classmethod
    def make_request(cls, method, url_suffix, data = {}):
        requestor = LobRequestor()
        resp = requestor.make_request(method = method, url_suffix = url_suffix,
                data = data)
        return make_lob_object(response = resp)

class ListableObject(LobObject):
    # Represents an object which is listable

    @classmethod
    def list(cls, **kwargs):
        param_string = ''
        for key in kwargs.keys():
            if '?' in param_string:
                param_string = '%s&%s=%s' %(param_string, key, kwargs.get(key))
            else:
                param_string = '%s?%s=%s' %(param_string, key, kwargs.get(key))
        return cls.make_request(method = 'GET', url_suffix = '%s%s' %(cls._base_url, param_string))

class GettableObject(LobObject):
    # Represents those objects which are fetchable by id
    
    @classmethod
    def get(cls, id):
        return cls.make_request(method = 'GET', url_suffix = '%s/%s' %(cls._base_url,
            id))

class RemovableObject(LobObject):
    # Represents objects which can be deleted

    @classmethod
    def delete(cls, id):
        return cls.make_request(method = 'DELETE', url_suffix = '%s/%s' %(cls._base_url, 
            id))

class CreatableObject(LobObject):
    # Represents objects which can be creared

    @classmethod
    def create(cls, **kwargs):
        return cls.make_request(method = 'POST', url_suffix = cls._base_url,
                data = kwargs)

class Service(ListableObject):
    # Represents a service object

    _base_url = 'services'

class Address(ListableObject, GettableObject, RemovableObject, CreatableObject):
    # Represents an address object

    _base_url = 'addresses'

class AddressVerify(LobObject):
    # Represents an address

    _base_url = 'verify'
    
    @classmethod
    def verify(cls, **kwargs):
        return cls.make_request(method = 'POST', url_suffix = cls._base_url, 
                data = kwargs)

class Packaging(ListableObject):
    # Represents a packaging object

    _base_url = 'packagings'

class Setting(ListableObject, GettableObject):
    # Represents a setting object

    _base_url = 'settings'

class Object(ListableObject, GettableObject, RemovableObject, CreatableObject):
    # Represents an object

    _base_url = 'objects'

class CreatableFormatObject(LobObject):

    @classmethod
    def format_data(cls, data, param_string):
        res = {}
        for key in data:
            res['%s[%s]' %(param_string, key)] = data.get(key)
        return res

class Job(ListableObject, GettableObject, CreatableFormatObject):
    # Represent a job

    _base_url = 'jobs'

    # Defining this separately because 'from' is a keyword
    @classmethod
    def create(cls, name, to, objects, from_address = None, **kwargs):
        data = {
                'name' : name,
            }
        if isinstance(to, dict):
            data.update(cls.format_data(data = to, param_string = 'to'))
        else:
            data['to'] = to
        if from_address and isinstance(from_address, dict):
            data.update(cls.format_data(data = from_address, param_string = 'from'))
        else:
            data['from'] = from_address
        if isinstance(objects, list):
            index = 1
            for obj in objects:
                if isinstance(obj, dict):
                    data.update(cls.format_data(data = obj,
                        param_string = 'object%s' %(index)))
                else:
                    data['object%s' %(index)] = obj
                index = index + 1
        else:
            data['object1'] = objects
        data.update(kwargs)
        return cls.make_request(method = 'POST', url_suffix = cls._base_url,
                data = data)

class Postcard(ListableObject, GettableObject, CreatableFormatObject):
    # Represents a postcard
    
    _base_url = 'postcards'

    @classmethod
    def create(cls, name, to, message = None, back = None, from_address = None, **kwargs):
        data = {
                'name' : name
            }
        if isinstance(to, dict):
            data.update(cls.format_data(data = to, param_string = 'to'))
        else:
            data['to'] = to
        if message: data['message'] = message
        if back: data['back'] = back
        if isinstance(from_address, dict):
            data.update(cls.format_data(data = from_address, param_string = 'from'))
        else:
            data['from'] = from_address
        data.update(**kwargs)
        return cls.make_request(method = 'POST', url_suffix = cls._base_url,
                data = data)
