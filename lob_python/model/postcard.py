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

from lob_python.model.address import Address
from lob_python.model.address_domestic_expanded import AddressDomesticExpanded
from lob_python.model.mail_type import MailType
from lob_python.model.merge_variables import MergeVariables
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.postcard_size import PostcardSize
from lob_python.model.psc_id import PscId
from lob_python.model.psc_use_type import PscUseType
from lob_python.model.resource_description import ResourceDescription
from lob_python.model.signed_link import SignedLink
from lob_python.model.thumbnail import Thumbnail
from lob_python.model.tracking_event_normal import TrackingEventNormal
globals()['Address'] = Address
globals()['AddressDomesticExpanded'] = AddressDomesticExpanded
globals()['MailType'] = MailType
globals()['MergeVariables'] = MergeVariables
globals()['MetadataModel'] = MetadataModel
globals()['PostcardSize'] = PostcardSize
globals()['PscId'] = PscId
globals()['PscUseType'] = PscUseType
globals()['ResourceDescription'] = ResourceDescription
globals()['SignedLink'] = SignedLink
globals()['Thumbnail'] = Thumbnail
globals()['TrackingEventNormal'] = TrackingEventNormal


class Postcard(ModelNormal):
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
        ('carrier',): {
            'USPS': "USPS",
        },
        ('object',): {
            'POSTCARD': "postcard",
        },
    }

    validations = {
        ('front_template_id',): {
            'regex': {
                'pattern': r'^tmpl_[a-zA-Z0-9]+$',  # noqa: E501
            },
        },
        ('back_template_id',): {
            'regex': {
                'pattern': r'^tmpl_[a-zA-Z0-9]+$',  # noqa: E501
            },
        },
        ('front_template_version_id',): {
            'regex': {
                'pattern': r'^vrsn_[a-zA-Z0-9]+$',  # noqa: E501
            },
        },
        ('back_template_version_id',): {
            'regex': {
                'pattern': r'^vrsn_[a-zA-Z0-9]+$',  # noqa: E501
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
            'id': (str,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'to': (Address, type(None)),  # noqa: E501
            '_from': (AddressDomesticExpanded, type(None)),  # noqa: E501
            'carrier': (str, type(None)),  # noqa: E501
            'thumbnails': (list, type(None)),  # noqa: E501
            'size': (PostcardSize, type(None)),  # noqa: E501
            'expected_delivery_date': (date, type(None)),  # noqa: E501
            'date_created': (datetime, type(None)),  # noqa: E501
            'date_modified': (datetime, type(None)),  # noqa: E501
            'deleted': (bool, type(None)),  # noqa: E501
            'front_template_id': (str, type(None)),  # noqa: E501
            'back_template_id': (str, type(None)),  # noqa: E501
            'front_template_version_id': (str, type(None)),  # noqa: E501
            'back_template_version_id': (str, type(None)),  # noqa: E501
            'tracking_events': (list, type(None)),  # noqa: E501
            'object': (str, type(None)),  # noqa: E501
            'description': (str, type(None)),  # noqa: E501
            'metadata': (MetadataModel, type(None)),  # noqa: E501
            'mail_type': (MailType, type(None)),  # noqa: E501
            'merge_variables': (MergeVariables, type(None)),  # noqa: E501
            'send_date': (datetime, type(None)),  # noqa: E501
            'use_type': (PscUseType, type(None)),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'url': 'url',  # noqa: E501
        'to': 'to',  # noqa: E501
        '_from': 'from',  # noqa: E501
        'carrier': 'carrier',  # noqa: E501
        'thumbnails': 'thumbnails',  # noqa: E501
        'size': 'size',  # noqa: E501
        'expected_delivery_date': 'expected_delivery_date',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_modified': 'date_modified',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'front_template_id': 'front_template_id',  # noqa: E501
        'back_template_id': 'back_template_id',  # noqa: E501
        'front_template_version_id': 'front_template_version_id',  # noqa: E501
        'back_template_version_id': 'back_template_version_id',  # noqa: E501
        'tracking_events': 'tracking_events',  # noqa: E501
        'object': 'object',  # noqa: E501
        'description': 'description',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'mail_type': 'mail_type',  # noqa: E501
        'merge_variables': 'merge_variables',  # noqa: E501
        'send_date': 'send_date',  # noqa: E501
        'use_type': 'use_type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, url, *args, **kwargs):  # noqa: E501
        """Postcard - a model defined in OpenAPI

        Args:
            id (str):
            url (str):

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
            to (Address, type(None)): [optional] # noqa: E501
            _from (AddressDomesticExpanded, type(None)): [optional] # noqa: E501
            carrier (str, type(None)): [optional] if omitted the server will use the default value of "USPS" # noqa: E501
            thumbnails (list, type(None)): [optional] # noqa: E501
            size (PostcardSize, type(None)): [optional] # noqa: E501
            expected_delivery_date (date, type(None)): A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`.. [optional] # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            front_template_id (str, type(None)): The unique ID of the HTML template used for the front of the postcard.. [optional] # noqa: E501
            back_template_id (str, type(None)): The unique ID of the HTML template used for the back of the postcard.. [optional] # noqa: E501
            front_template_version_id (str, type(None)): The unique ID of the specific version of the HTML template used for the front of the postcard.. [optional] # noqa: E501
            back_template_version_id (str, type(None)): The unique ID of the specific version of the HTML template used for the back of the postcard.. [optional] # noqa: E501
            tracking_events (list, type(None)): An array of tracking_event objects ordered by ascending `time`. Will not be populated for postcards created in test mode.. [optional] # noqa: E501
            object (str, type(None)): [optional] if omitted the server will use the default value of "postcard" # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            mail_type (MailType, type(None)): [optional] # noqa: E501
            merge_variables (MergeVariables, type(None)): [optional] # noqa: E501
            send_date (datetime, type(None)): A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the `send_date` has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A `send_date` passed with no time zone will default to UTC, while a `send_date` passed with a time zone will be converted to UTC.. [optional] # noqa: E501
            use_type (PscUseType, type(None)): [optional] # noqa: E501
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

        self.id = id
        self.url = url
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
    def __init__(self, id, url, *args, **kwargs):  # noqa: E501
        """Postcard - a model defined in OpenAPI

        Args:
            id (PscId):
            url (SignedLink):

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
            to (Address, type(None)): [optional] # noqa: E501
            _from (AddressDomesticExpanded, type(None)): [optional] # noqa: E501
            carrier (str, type(None)): [optional] if omitted the server will use the default value of "USPS" # noqa: E501
            thumbnails (list, type(None)): [optional] # noqa: E501
            size (PostcardSize, type(None)): [optional] # noqa: E501
            expected_delivery_date (date, type(None)): A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`.. [optional] # noqa: E501
            date_created (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was created.. [optional] # noqa: E501
            date_modified (datetime, type(None)): A timestamp in ISO 8601 format of the date the resource was last modified.. [optional] # noqa: E501
            deleted (bool, type(None)): Only returned if the resource has been successfully deleted.. [optional] # noqa: E501
            front_template_id (str, type(None)): The unique ID of the HTML template used for the front of the postcard.. [optional] # noqa: E501
            back_template_id (str, type(None)): The unique ID of the HTML template used for the back of the postcard.. [optional] # noqa: E501
            front_template_version_id (str, type(None)): The unique ID of the specific version of the HTML template used for the front of the postcard.. [optional] # noqa: E501
            back_template_version_id (str, type(None)): The unique ID of the specific version of the HTML template used for the back of the postcard.. [optional] # noqa: E501
            tracking_events (list, type(None)): An array of tracking_event objects ordered by ascending `time`. Will not be populated for postcards created in test mode.. [optional] # noqa: E501
            object (str, type(None)): [optional] if omitted the server will use the default value of "postcard" # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            mail_type (MailType, type(None)): [optional] # noqa: E501
            merge_variables (MergeVariables, type(None)): [optional] # noqa: E501
            send_date (datetime, type(None)): A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the `send_date` has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A `send_date` passed with no time zone will default to UTC, while a `send_date` passed with a time zone will be converted to UTC.. [optional] # noqa: E501
            use_type (PscUseType, type(None)): [optional] # noqa: E501
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

        self.id = id
        self.url = url
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
