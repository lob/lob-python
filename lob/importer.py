# Imports needed in setup.py and __init__.py

def import_json():
    # Python 2.5 and below do not ship with json
    _json_loaded = None
    try:
        import json
        if hasattr(json, 'loads'):
            return json
        _json_loaded = False
    except ImportError:
        pass

    try:
        import simplejson
        return simplejson
    except ImportError:
        if _json_loaded is None:
            raise ImportError("Lob requires a JSON library, which you do not \
                    appear to have. Please install the simplejson library. \
                    HINT: Try installing the python simplejson library \
                    via 'pip install simplejson' or 'easy_install simplejson'")
        else:
            raise ImportError("Lob required a JSON library with the same \
                    interface as the Python 2.6 'json' library. You appear to \
                    have a 'json' library with a different interface. Please install \
                    the simplejson library. HINT: Try installing the python \
                    simplejson library via 'pip install simplejson' or \
                    'easy_install simplejson'")

def import_requests():
    # This will import the required requests library 
    try:
        import requests
        return ('requests', requests)
    except ImportError:
        raise ImportError('Lob requires the requests package')

