# lob_python.IdentityValidationApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate**](IdentityValidationApi.md#validate) | **POST** /identity_validation | validate


# **validate**
> IdentityValidation validate(multi_line_address)

validate

Validates whether a given name is associated with an address.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import identity_validation_api
from lob_python.model.multi_line_address import MultiLineAddress
from lob_python.model.identity_validation import IdentityValidation
from lob_python.model.lob_error import LobError
from pprint import pprint
# Defining the host is optional and defaults to https://api.lob.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lob_python.Configuration(
    host = "https://api.lob.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = lob_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with lob_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = identity_validation_api.IdentityValidationApi(api_client)
    multi_line_address = MultiLineAddress(
        recipient=Recipient("recipient_example"),
        company=Company("company_example"),
        primary_line=PrimaryLineUs("primary_line_example"),
        secondary_line=SecondaryLine("secondary_line_example"),
        urbanization=Urbanization("urbanization_example"),
        city=City("city_example"),
        state="state_example",
        zip_code=ZipCode("04807"),
    ) # MultiLineAddress | 

    # example passing only required values which don't have defaults set
    try:
        # validate
        api_response = api_instance.validate(multi_line_address)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IdentityValidationApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_line_address** | [**MultiLineAddress**](MultiLineAddress.md)|  |

### Return type

[**IdentityValidation**](IdentityValidation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the likelihood a given name is associated with an address. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

