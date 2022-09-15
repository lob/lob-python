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

from lob_python.model.merge_variables import MergeVariables
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.resource_description import ResourceDescription
globals()['MergeVariables'] = MergeVariables
globals()['MetadataModel'] = MetadataModel
globals()['ResourceDescription'] = ResourceDescription


class CheckEditable(ModelNormal):
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
        ('mail_type',): {
            'USPS_FIRST_CLASS': "usps_first_class",
        },
    }

    validations = {
        ('amount',): {
            'inclusive_maximum': 999999.99,
        },
        ('memo',): {
            'max_length': 40,
        },
        ('check_number',): {
            'inclusive_maximum': 500000000,
            'inclusive_minimum': 1,
        },
        ('message',): {
            'max_length': 400,
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
        from lob_python.model.address_domestic import AddressDomestic
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            '_from': (str, AddressDomestic),  # noqa: E501
            'to': (str, AddressDomestic),  # noqa: E501
            'bank_account': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'logo': (str, type(None)),  # noqa: E501
            'check_bottom': (str, type(None)),  # noqa: E501
            'attachment': (str, type(None)),  # noqa: E501
            'description': (str, type(None)),  # noqa: E501
            'metadata': (MetadataModel, type(None)),  # noqa: E501
            'merge_variables': (MergeVariables, type(None)),  # noqa: E501
            'send_date': (datetime, type(None)),  # noqa: E501
            'mail_type': (str, type(None)),  # noqa: E501
            'memo': (str, type(None)),  # noqa: E501
            'check_number': (int, type(None)),  # noqa: E501
            'message': (str, type(None)),  # noqa: E501
            'billing_group_id': (str, type(None)),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        '_from': 'from',  # noqa: E501
        'to': 'to',  # noqa: E501
        'bank_account': 'bank_account',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'logo': 'logo',  # noqa: E501
        'check_bottom': 'check_bottom',  # noqa: E501
        'attachment': 'attachment',  # noqa: E501
        'description': 'description',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'merge_variables': 'merge_variables',  # noqa: E501
        'send_date': 'send_date',  # noqa: E501
        'mail_type': 'mail_type',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'check_number': 'check_number',  # noqa: E501
        'message': 'message',  # noqa: E501
        'billing_group_id': 'billing_group_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, _from, to, bank_account, amount, *args, **kwargs):  # noqa: E501
        """CheckEditable - a model defined in OpenAPI

        Args:
            _from (str, AddressDomestic): Must either be an address ID or an inline object with correct address parameters..
            to (str, AddressDomestic): Must either be an address ID or an inline object with correct address parameters..
            bank_account (str):
            amount (float): The payment amount to be sent in US dollars.

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
            logo (str, type(None)): Accepts a remote URL or local file upload to an image to print (in grayscale) in the upper-left corner of your check.. [optional] # noqa: E501
            check_bottom (str, type(None)): The artwork to use on the bottom of the check page.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 8.5\"x11\" at 300 DPI, while supplied HTML will be rendered and trimmed to fit on a 8.5\"x11\" page. - The check bottom will always be printed in black & white. - Must conform to [this template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_bottom_template.pdf).  Need more help? Consult our [HTML examples](#section/HTML-Examples).. [optional] # noqa: E501
            attachment (str, type(None)): A document to include with the check.. [optional] # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            merge_variables (MergeVariables, type(None)): [optional] # noqa: E501
            send_date (datetime, type(None)): A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the `send_date` has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A `send_date` passed with no time zone will default to UTC, while a `send_date` passed with a time zone will be converted to UTC.. [optional] # noqa: E501
            mail_type (str, type(None)): Checks must be sent `usps_first_class`. [optional] if omitted the server will use the default value of "usps_first_class" # noqa: E501
            memo (str, type(None)): Text to include on the memo line of the check.. [optional] # noqa: E501
            check_number (int, type(None)): An integer that designates the check number.. [optional] # noqa: E501
            message (str, type(None)): Max of 400 characters to be included at the bottom of the check page.. [optional] # noqa: E501
            billing_group_id (str, type(None)): An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See [Billing Group API](https://lob.github.io/lob-openapi/#tag/Billing-Groups) for more information.. [optional] # noqa: E501
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

        self._from = _from
        self.to = to
        self.bank_account = bank_account
        self.amount = amount
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
    def __init__(self, _from, to, bank_account, amount, *args, **kwargs):  # noqa: E501
        """CheckEditable - a model defined in OpenAPI

        Args:
            _from (str): Must either be an address ID or an inline object with correct address parameters.
            to (str): Must either be an address ID or an inline object with correct address parameters.
            bank_account (str, none_type):
            amount (float): The payment amount to be sent in US dollars.

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
            logo (str, type(None)): Accepts a remote URL or local file upload to an image to print (in grayscale) in the upper-left corner of your check.. [optional] # noqa: E501
            check_bottom (str, type(None)): The artwork to use on the bottom of the check page.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 8.5\"x11\" at 300 DPI, while supplied HTML will be rendered and trimmed to fit on a 8.5\"x11\" page. - The check bottom will always be printed in black & white. - Must conform to [this template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_bottom_template.pdf).  Need more help? Consult our [HTML examples](#section/HTML-Examples).. [optional] # noqa: E501
            attachment (str, type(None)): A document to include with the check.. [optional] # noqa: E501
            description (str, type(None)): [optional] # noqa: E501
            metadata (MetadataModel, type(None)): [optional] # noqa: E501
            merge_variables (MergeVariables, type(None)): [optional] # noqa: E501
            send_date (datetime, type(None)): A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the `send_date` has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A `send_date` passed with no time zone will default to UTC, while a `send_date` passed with a time zone will be converted to UTC.. [optional] # noqa: E501
            mail_type (str, type(None)): Checks must be sent `usps_first_class`. [optional] if omitted the server will use the default value of "usps_first_class" # noqa: E501
            memo (str, type(None)): Text to include on the memo line of the check.. [optional] # noqa: E501
            check_number (int, type(None)): An integer that designates the check number.. [optional] # noqa: E501
            message (str, type(None)): Max of 400 characters to be included at the bottom of the check page.. [optional] # noqa: E501
            billing_group_id (str, type(None)): An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See [Billing Group API](https://lob.github.io/lob-openapi/#tag/Billing-Groups) for more information.. [optional] # noqa: E501
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

        self._from = _from
        self.to = to
        self.bank_account = bank_account
        self.amount = amount
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
