# lob_python.IntlVerificationsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyBulk**](IntlVerificationsApi.md#verifyBulk) | **POST** /bulk/intl_verifications | verifyBulk
[**verifySingle**](IntlVerificationsApi.md#verifySingle) | **POST** /intl_verifications | verifySingle


# **verifyBulk**
> IntlVerifications verifyBulk(intl_verifications_payload)

verifyBulk

Verify a list of international (except US or US territories) address with a live API key.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import intl_verifications_api
from lob_python.model.intl_verifications_payload import IntlVerificationsPayload
from lob_python.model.lob_error import LobError
from lob_python.model.intl_verifications import IntlVerifications
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
    api_instance = intl_verifications_api.IntlVerificationsApi(api_client)
    intl_verifications_payload = IntlVerificationsPayload(
        addresses=[
            MultipleComponentsIntl(
                recipient=Recipient("recipient_example"),
                primary_line="primary_line_example",
                secondary_line=SecondaryLine("secondary_line_example"),
                city=City("city_example"),
                state="state_example",
                postal_code=PostalCode("postal_code_example"),
                country=CountryExtended("AD"),
            ),
        ],
    ) # IntlVerificationsPayload | 

    # example passing only required values which don't have defaults set
    try:
        # verifyBulk
        api_response = api_instance.verifyBulk(intl_verifications_payload)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IntlVerificationsApi->verifyBulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intl_verifications_payload** | [**IntlVerificationsPayload**](IntlVerificationsPayload.md)|  |

### Return type

[**IntlVerifications**](IntlVerifications.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of international verification objects. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifySingle**
> IntlVerification verifySingle(intl_verification_writable)

verifySingle

Verify an international (except US or US territories) address with a live API key.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import intl_verifications_api
from lob_python.model.intl_verification import IntlVerification
from lob_python.model.intl_verification_writable import IntlVerificationWritable
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
    api_instance = intl_verifications_api.IntlVerificationsApi(api_client)
    intl_verification_writable = IntlVerificationWritable(
        recipient=Recipient("recipient_example"),
        primary_line="primary_line_example",
        secondary_line=SecondaryLine("secondary_line_example"),
        city=City("city_example"),
        state="state_example",
        postal_code=PostalCode("postal_code_example"),
        country=CountryExtended("AD"),
        address="address_example",
    ) # IntlVerificationWritable | 
    x_lang_output = "native" # str | * `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # verifySingle
        api_response = api_instance.verifySingle(intl_verification_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IntlVerificationsApi->verifySingle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # verifySingle
        api_response = api_instance.verifySingle(intl_verification_writable, x_lang_output=x_lang_output)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IntlVerificationsApi->verifySingle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intl_verification_writable** | [**IntlVerificationWritable**](IntlVerificationWritable.md)|  |
 **x_lang_output** | **str**| * &#x60;native&#x60; - Translate response to the native language of the country in the request * &#x60;match&#x60; - match the response to the language in the request  Default response is in English.  | [optional]

### Return type

[**IntlVerification**](IntlVerification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an international verification object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

