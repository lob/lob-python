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

from lob_python.model.bank_id import BankId
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.resource_description import ResourceDescription
globals()['BankId'] = BankId
globals()['MetadataModel'] = MetadataModel
globals()['ResourceDescription'] = ResourceDescription


class BankAccount(ModelNormal):
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
        ('account_type',): {
            'COMPANY': "company",
            'INDIVIDUAL': "individual",
        },
        ('object',): {
            'BANK_ACCOUNT': "bank_account",
        },
    }

    validations = {
        ('routing_number',): {
            'max_length': 9,
            'min_length': 9,
        },
        ('account_number',): {
            'max_length': 17,
        },
        ('signatory',): {
            'max_length': 30,
        },
        ('signature_url',): {
            'regex': {
                'pattern': r'^https:\/\/lob-assets.com\/(letters|postcards|bank-accounts|checks|self-mailers|cards)\/[a-z]{3,4}_[a-z0-9]{15,16}(''|_signature)(.pdf|_thumb_[a-z]+_[0-9]+.png|.png)\?(version=[a-z0-9]*&)expires=[0-9]{10}&signature=[a-zA-Z0-9-_]+',  # noqa: E501
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
            'routing_number': (str,),  # noqa: E501
            'account_number': (str,),  # noqa: E501
            'account_type': (str,),  # noqa: E501
            'signatory': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'date_created': (datetime,),  # noqa: E501
            'date_modified': (datetime,),  # noqa: E501
            'object': (str,),  # noqa: E501
            'description': (str, type(None)),  # noqa: E501
            'metadata': (MetadataModel, type(None)),  # noqa: E501
            'signature_url': (str, type(None)),  # noqa: E501
            'bank_name': (str, type(None)),  # noqa: E501
            'verified': (bool, type(None)),  # noqa: E501
            'deleted': (bool, type(None)),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'routing_number': 'routing_number',  # noqa: E501
        'account_number': 'account_number',  # noqa: E501
        'account_type': 'account_type',  # noqa: E501
        'signatory': 'signatory',  # noqa: E501
        'id': 'id',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_modified': 'date_modified',  # noqa: E501
        'object': 'object',  # noqa: E501
        'description': 'description',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'signature_url': 'signature_url',  # noqa: E501
        'bank_name': 'bank_name',  # noqa: E501
        'verified': 'verified',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, routing_number, account_number, account_type, signatory, id, date_created, date_modified, *args, **kwargs):  # noqa: E501
        """BankAccount - a model defined in OpenAPI

        Args:
            routing_number (str): Must be a [valid US routing number](https://www.frbservices.org/index.html).
            account_number (str):
            account_type (str): The type of entity that holds the account.
            signatory (str): The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the [Dashboard](https://dashboard.lob.com/#/login).
            id (str):
            date_created (datetime): A timestamp in ISO 8601 format of the date the resource was created.
            date_modified (datetime): A timestamp in ISO 8601 format of the date the resource was last modified.

        Keyword Args:
            object (str): defaults to "bank_account", must be one of ["bank_account", ]  # noqa: E501
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
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            signature_url (str, type(None)): A signed link to the signature image. will be generated.. [optional] # noqa: E501
            bank_name (str, type(None)): The name of the bank based on the provided routing number, e.g. `JPMORGAN CHASE BANK`.. [optional] # noqa: E501
            verified (bool, type(None)): A bank account must be verified before a check can be created.. [optional] if omitted the server will use the default value of False # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
        """

        object = kwargs.get('object', "bank_account")
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

        self.routing_number = routing_number
        self.account_number = account_number
        self.account_type = account_type
        self.signatory = signatory
        self.id = id
        self.date_created = date_created
        self.date_modified = date_modified
        self.object = object
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
    def __init__(self, routing_number, account_number, account_type, signatory, id, date_created, date_modified, *args, **kwargs):  # noqa: E501
        """BankAccount - a model defined in OpenAPI

        Args:
            routing_number (str): Must be a [valid US routing number](https://www.frbservices.org/index.html).
            account_number (str):
            account_type (str): The type of entity that holds the account.
            signatory (str): The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the [Dashboard](https://dashboard.lob.com/#/login).
            id (BankId):
            date_created (datetime): A timestamp in ISO 8601 format of the date the resource was created.
            date_modified (datetime): A timestamp in ISO 8601 format of the date the resource was last modified.

        Keyword Args:
            object (str): defaults to "bank_account", must be one of ["bank_account", ]  # noqa: E501
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
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            signature_url (str, type(None)): A signed link to the signature image. will be generated.. [optional] # noqa: E501
            bank_name (str, type(None)): The name of the bank based on the provided routing number, e.g. `JPMORGAN CHASE BANK`.. [optional] # noqa: E501
            verified (bool, type(None)): A bank account must be verified before a check can be created.. [optional] if omitted the server will use the default value of False # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
        """

        object = kwargs.get('object', "bank_account")
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

        self.routing_number = routing_number
        self.account_number = account_number
        self.account_type = account_type
        self.signatory = signatory
        self.id = id
        self.date_created = date_created
        self.date_modified = date_modified
        self.object = object
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
