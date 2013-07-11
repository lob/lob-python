# This file contains all the objects for Lob

class LobObject(object):
    # Have to implement the to_dict() method which will convert to dict
    pass

class Service(LobObject):
    # Represents the service object
    
    _base_url = 'services'
    
    @classmethod
    def list(cls):
        requestor = 
