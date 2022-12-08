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

from lob_python.model.campaign import Campaign
from lob_python.model.crv_id import CrvId
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.resource_description import ResourceDescription
globals()['Campaign'] = Campaign
globals()['CrvId'] = CrvId
globals()['MetadataModel'] = MetadataModel
globals()['ResourceDescription'] = ResourceDescription


class CampaignCreative(ModelNormal):
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
        ('resource_type',): {
            'LETTER': "letter",
            'POSTCARD': "postcard",
        },
        ('object',): {
            'CREATIVE': "creative",
        },
    }

    validations = {
        ('campaigns',): {
            'max_items': 0,
            'min_items': 0,
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
        from lob_python.model.address_editable import AddressEditable
        from lob_python.model.postcard_details_writable import PostcardDetailsWritable
        from lob_python.model.letter_details_writable import LetterDetailsWritable
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
            '_from': (str, AddressEditable, type(None)),  # noqa: E501
            'resource_type': (str, type(None)),  # noqa: E501
            'details': (PostcardDetailsWritable, LetterDetailsWritable, type(None)),  # noqa: E501
            'metadata': (MetadataModel, type(None)),  # noqa: E501
            'template_preview_urls': (dict, type(None)),  # noqa: E501
            'template_previews': (list, type(None)),  # noqa: E501
            'deleted': (bool, type(None)),  # noqa: E501
            'campaigns': (list, type(None)),  # noqa: E501
            'date_created': (datetime, type(None)),  # noqa: E501
            'date_modified': (datetime, type(None)),  # noqa: E501
            'object': (str, type(None)),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'description': 'description',  # noqa: E501
        '_from': 'from',  # noqa: E501
        'resource_type': 'resource_type',  # noqa: E501
        'details': 'details',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'template_preview_urls': 'template_preview_urls',  # noqa: E501
        'template_previews': 'template_previews',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'campaigns': 'campaigns',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_modified': 'date_modified',  # noqa: E501
        'object': 'object',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CampaignCreative - a model defined in OpenAPI

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
            _from (str, AddressEditable, type(None)): Must either be an address ID or an inline object with correct address parameters.. [optional]  # noqa: E501
            resource_type (str, type(None)): Mailpiece type for the creative. [optional] # noqa: E501
            details (PostcardDetailsWritable, LetterDetailsWritable, type(None)): Either PostcardDetailsReturned or LetterDetailsReturned. [optional]  # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            template_preview_urls (dict, type(None)): Preview URLs associated with a creative's artwork asset(s) if the creative uses HTML templates as assets.. [optional] # noqa: E501
            template_previews (list, type(None)): A list of template preview objects if the creative uses HTML template(s) as artwork asset(s).. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            campaigns (list, type(None)): [optional] # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            object (str, type(None)): Value is resource type.. [optional] if omitted the server will use the default value of "creative" # noqa: E501
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
        """CampaignCreative - a model defined in OpenAPI

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
            _from (str, AddressEditable, type(None)): Must either be an address ID or an inline object with correct address parameters.. [optional]  # noqa: E501
            resource_type (str, type(None)): Mailpiece type for the creative. [optional] # noqa: E501
            details (PostcardDetailsWritable, LetterDetailsWritable, type(None)): Either PostcardDetailsReturned or LetterDetailsReturned. [optional]  # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            template_preview_urls (dict, type(None)): Preview URLs associated with a creative's artwork asset(s) if the creative uses HTML templates as assets.. [optional] # noqa: E501
            template_previews (list, type(None)): A list of template preview objects if the creative uses HTML template(s) as artwork asset(s).. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            campaigns (list, type(None)): [optional] # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            object (str, type(None)): Value is resource type.. [optional] if omitted the server will use the default value of "creative" # noqa: E501
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