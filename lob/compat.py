import sys


if sys.version_info[0] == 3:  # pragma: no cover
    string_type = str
    from io import BytesIO
else:  # pragma: no cover
    string_type = basestring
    from StringIO import StringIO as BytesIO
