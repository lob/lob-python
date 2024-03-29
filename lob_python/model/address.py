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

from lob_python.model.adr_id import AdrId
from lob_python.model.company import Company
from lob_python.model.country_extended_expanded import CountryExtendedExpanded
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.resource_description import ResourceDescription
globals()['AdrId'] = AdrId
globals()['Company'] = Company
globals()['CountryExtendedExpanded'] = CountryExtendedExpanded
globals()['MetadataModel'] = MetadataModel
globals()['ResourceDescription'] = ResourceDescription


class Address(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('object',): {
            'ADDRESS': "address",
        },
    }

    validations = {
        ('name',): {
            'max_length': 40,
        },
        ('phone',): {
            'max_length': 40,
        },
        ('email',): {
            'max_length': 100,
        },
        ('address_line1',): {
            'max_length': 64,
        },
        ('address_line2',): {
            'max_length': 64,
        },
        ('address_city',): {
            'max_length': 200,
        },
        ('address_state',): {
            'regex': {
                'pattern': r'^[a-zA-Z]{2}$',  # noqa: E501
            },
        },
        ('address_zip',): {
            'regex': {
                'pattern': r'^\d{5}(-\d{4})?$',  # noqa: E501
            },
        },
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
            'id': (str, type(None)),  # noqa: E501
            'description': (str, type(None)),  # noqa: E501
            'name': (str, type(None)),  # noqa: E501
            'company': (str, type(None)),  # noqa: E501
            'phone': (str, type(None)),  # noqa: E501
            'email': (str, type(None)),  # noqa: E501
            'metadata': (MetadataModel, type(None)),  # noqa: E501
            'address_line1': (str, type(None)),  # noqa: E501
            'address_line2': (str, type(None)),  # noqa: E501
            'address_city': (str, type(None)),  # noqa: E501
            'address_state': (str, type(None)),  # noqa: E501
            'address_zip': (str, type(None)),  # noqa: E501
            'address_country': (CountryExtendedExpanded, type(None)),  # noqa: E501
            'object': (str, type(None)),  # noqa: E501
            'date_created': (datetime, type(None)),  # noqa: E501
            'date_modified': (datetime, type(None)),  # noqa: E501
            'deleted': (bool, type(None)),  # noqa: E501
            'recipient_moved': (bool, type(None)),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'description': 'description',  # noqa: E501
        'name': 'name',  # noqa: E501
        'company': 'company',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'email': 'email',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'address_line1': 'address_line1',  # noqa: E501
        'address_line2': 'address_line2',  # noqa: E501
        'address_city': 'address_city',  # noqa: E501
        'address_state': 'address_state',  # noqa: E501
        'address_zip': 'address_zip',  # noqa: E501
        'address_country': 'address_country',  # noqa: E501
        'object': 'object',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_modified': 'date_modified',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'recipient_moved': 'recipient_moved',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Address - a model defined in OpenAPI

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
            id (str, type(None)): [optional] # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            name (str, type(None)): name associated with address. [optional] # noqa: E501
            company (str, type(None)): [optional] # noqa: E501
            phone (str, type(None)): Must be no longer than 40 characters.. [optional] # noqa: E501
            email (str, type(None)): Must be no longer than 100 characters.. [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            address_line1 (str, type(None)): [optional] # noqa: E501
            address_line2 (str, type(None)): [optional] # noqa: E501
            address_city (str, type(None)): [optional] # noqa: E501
            address_state (str, type(None)): 2 letter state short-name code. [optional] # noqa: E501
            address_zip (str, type(None)): Must follow the ZIP format of `12345` or ZIP+4 format of `12345-1234`. . [optional] # noqa: E501
            address_country (CountryExtendedExpanded, type(None)): [optional] # noqa: E501
            object (str, type(None)): [optional] if omitted the server will use the default value of "address" # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            recipient_moved (bool, type(None)): Only returned for accounts on certain <a href=\"https://dashboard.lob.com/#/settings/editions\">Print &amp; Mail Editions</a>. Value is `true` if the address was altered because the recipient filed for a <a href=\"#ncoa\">National Change of Address (NCOA)</a>, `false` if the NCOA check was run but no altered address was found, and `null` if the NCOA check was not run. The NCOA check does not happen for non-US addresses, for non-deliverable US addresses, or for addresses created before the NCOA feature was added to your account. . [optional] # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Address - a model defined in OpenAPI

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
            id (str, type(None)): [optional] # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            name (str, type(None)): name associated with address. [optional] # noqa: E501
            company (str, type(None)): [optional] # noqa: E501
            phone (str, type(None)): Must be no longer than 40 characters.. [optional] # noqa: E501
            email (str, type(None)): Must be no longer than 100 characters.. [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            address_line1 (str, type(None)): [optional] # noqa: E501
            address_line2 (str, type(None)): [optional] # noqa: E501
            address_city (str, type(None)): [optional] # noqa: E501
            address_state (str, type(None)): 2 letter state short-name code. [optional] # noqa: E501
            address_zip (str, type(None)): Must follow the ZIP format of `12345` or ZIP+4 format of `12345-1234`. . [optional] # noqa: E501
            address_country (CountryExtendedExpanded, type(None)): [optional] # noqa: E501
            object (str, type(None)): [optional] if omitted the server will use the default value of "address" # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            recipient_moved (bool, type(None)): Only returned for accounts on certain <a href=\"https://dashboard.lob.com/#/settings/editions\">Print &amp; Mail Editions</a>. Value is `true` if the address was altered because the recipient filed for a <a href=\"#ncoa\">National Change of Address (NCOA)</a>, `false` if the NCOA check was run but no altered address was found, and `null` if the NCOA check was not run. The NCOA check does not happen for non-US addresses, for non-deliverable US addresses, or for addresses created before the NCOA feature was added to your account. . [optional] # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
