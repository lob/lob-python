"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lob_python.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from lob_python.exceptions import ApiAttributeError



class CountryExtended(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'AD': "AD",
            'AE': "AE",
            'AF': "AF",
            'AG': "AG",
            'AI': "AI",
            'AL': "AL",
            'AN': "AN",
            'AO': "AO",
            'AQ': "AQ",
            'AR': "AR",
            'AT': "AT",
            'AU': "AU",
            'AW': "AW",
            'AZ': "AZ",
            'BA': "BA",
            'BB': "BB",
            'BD': "BD",
            'BE': "BE",
            'BF': "BF",
            'BG': "BG",
            'BH': "BH",
            'BI': "BI",
            'BJ': "BJ",
            'BM': "BM",
            'BN': "BN",
            'BO': "BO",
            'BQ': "BQ",
            'BR': "BR",
            'BS': "BS",
            'BT': "BT",
            'BW': "BW",
            'BY': "BY",
            'BZ': "BZ",
            'CA': "CA",
            'CD': "CD",
            'CG': "CG",
            'CH': "CH",
            'CI': "CI",
            'CK': "CK",
            'CL': "CL",
            'CM': "CM",
            'CN': "CN",
            'CO': "CO",
            'CR': "CR",
            'CS': "CS",
            'CU': "CU",
            'CV': "CV",
            'CW': "CW",
            'CY': "CY",
            'CZ': "CZ",
            'DE': "DE",
            'DJ': "DJ",
            'DK': "DK",
            'DM': "DM",
            'DO': "DO",
            'DZ': "DZ",
            'EC': "EC",
            'EE': "EE",
            'EG': "EG",
            'EH': "EH",
            'ER': "ER",
            'ES': "ES",
            'ET': "ET",
            'FI': "FI",
            'FJ': "FJ",
            'FK': "FK",
            'FO': "FO",
            'FR': "FR",
            'GA': "GA",
            'GB': "GB",
            'GD': "GD",
            'GE': "GE",
            'GH': "GH",
            'GI': "GI",
            'GL': "GL",
            'GM': "GM",
            'GN': "GN",
            'GQ': "GQ",
            'GR': "GR",
            'GS': "GS",
            'GT': "GT",
            'GW': "GW",
            'GY': "GY",
            'HK': "HK",
            'HN': "HN",
            'HR': "HR",
            'HT': "HT",
            'HU': "HU",
            'ID': "ID",
            'IE': "IE",
            'IL': "IL",
            'IN': "IN",
            'IO': "IO",
            'IQ': "IQ",
            'IR': "IR",
            'IS': "IS",
            'IT': "IT",
            'JM': "JM",
            'JO': "JO",
            'JP': "JP",
            'KE': "KE",
            'KG': "KG",
            'KH': "KH",
            'KI': "KI",
            'KM': "KM",
            'KN': "KN",
            'KP': "KP",
            'KR': "KR",
            'KW': "KW",
            'KY': "KY",
            'KZ': "KZ",
            'LA': "LA",
            'LB': "LB",
            'LC': "LC",
            'LI': "LI",
            'LK': "LK",
            'LR': "LR",
            'LS': "LS",
            'LT': "LT",
            'LU': "LU",
            'LV': "LV",
            'LY': "LY",
            'MA': "MA",
            'MC': "MC",
            'MD': "MD",
            'ME': "ME",
            'MG': "MG",
            'MK': "MK",
            'ML': "ML",
            'MM': "MM",
            'MN': "MN",
            'MO': "MO",
            'MR': "MR",
            'MS': "MS",
            'MT': "MT",
            'MU': "MU",
            'MV': "MV",
            'MW': "MW",
            'MX': "MX",
            'MY': "MY",
            'MZ': "MZ",
            'NA': "NA",
            'NE': "NE",
            'NF': "NF",
            'NG': "NG",
            'NI': "NI",
            'NL': "NL",
            'NO': "NO",
            'NP': "NP",
            'NR': "NR",
            'NU': "NU",
            'NZ': "NZ",
            'OM': "OM",
            'PA': "PA",
            'PE': "PE",
            'PG': "PG",
            'PH': "PH",
            'PK': "PK",
            'PL': "PL",
            'PN': "PN",
            'PT': "PT",
            'PY': "PY",
            'QA': "QA",
            'RO': "RO",
            'RS': "RS",
            'RU': "RU",
            'RW': "RW",
            'SA': "SA",
            'SB': "SB",
            'SC': "SC",
            'SD': "SD",
            'SE': "SE",
            'SG': "SG",
            'SH': "SH",
            'SI': "SI",
            'SK': "SK",
            'SL': "SL",
            'SM': "SM",
            'SN': "SN",
            'SO': "SO",
            'SR': "SR",
            'SS': "SS",
            'ST': "ST",
            'SV': "SV",
            'SX': "SX",
            'SY': "SY",
            'SZ': "SZ",
            'TC': "TC",
            'TD': "TD",
            'TG': "TG",
            'TH': "TH",
            'TJ': "TJ",
            'TK': "TK",
            'TL': "TL",
            'TM': "TM",
            'TN': "TN",
            'TO': "TO",
            'TR': "TR",
            'TT': "TT",
            'TV': "TV",
            'TW': "TW",
            'TZ': "TZ",
            'UA': "UA",
            'UG': "UG",
            'US': "US",
            'UY': "UY",
            'UZ': "UZ",
            'VA': "VA",
            'VC': "VC",
            'VE': "VE",
            'VG': "VG",
            'VN': "VN",
            'VU': "VU",
            'WS': "WS",
            'YE': "YE",
            'ZA': "ZA",
            'ZM': "ZM",
            'ZW': "ZW",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """CountryExtended - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Must be a 2 letter country short-name code (ISO 3166).., must be one of ["AD", "AE", "AF", "AG", "AI", "AL", "AN", "AO", "AQ", "AR", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CS", "CU", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FO", "FR", "GA", "GB", "GD", "GE", "GH", "GI", "GL", "GM", "GN", "GQ", "GR", "GS", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IO", "IQ", "IR", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MK", "ML", "MM", "MN", "MO", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PN", "PT", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VN", "VU", "WS", "YE", "ZA", "ZM", "ZW", ]  # noqa: E501
        Keyword Args:
            value (): Must be a 2 letter country short-name code (ISO 3166).., must be one of ["AD", "AE", "AF", "AG", "AI", "AL", "AN", "AO", "AQ", "AR", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CS", "CU", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FO", "FR", "GA", "GB", "GD", "GE", "GH", "GI", "GL", "GM", "GN", "GQ", "GR", "GS", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IO", "IQ", "IR", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MK", "ML", "MM", "MN", "MO", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PN", "PT", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VN", "VU", "WS", "YE", "ZA", "ZM", "ZW", ]  # noqa: E501

            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """CountryExtended - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Must be a 2 letter country short-name code (ISO 3166).., must be one of ["AD", "AE", "AF", "AG", "AI", "AL", "AN", "AO", "AQ", "AR", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CS", "CU", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FO", "FR", "GA", "GB", "GD", "GE", "GH", "GI", "GL", "GM", "GN", "GQ", "GR", "GS", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IO", "IQ", "IR", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MK", "ML", "MM", "MN", "MO", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PN", "PT", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VN", "VU", "WS", "YE", "ZA", "ZM", "ZW", ]  # noqa: E501

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
