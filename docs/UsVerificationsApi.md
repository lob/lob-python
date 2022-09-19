# lob_python.UsVerificationsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyBulk**](UsVerificationsApi.md#verifyBulk) | **POST** /bulk/us_verifications | verifyBulk
[**verifySingle**](UsVerificationsApi.md#verifySingle) | **POST** /us_verifications | verifySingle


# **verifyBulk**
> UsVerifications verifyBulk(multiple_components_list)

verifyBulk

Verify a list of US or US territory addresses with a live API key.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import us_verifications_api
from lob_python.model.multiple_components_list import MultipleComponentsList
from lob_python.model.us_verifications import UsVerifications
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
    api_instance = us_verifications_api.UsVerificationsApi(api_client)
    multiple_components_list = MultipleComponentsList(
        addresses=[
            MultipleComponents(
                recipient=Recipient("recipient_example"),
                primary_line=PrimaryLineUs("primary_line_example"),
                secondary_line=SecondaryLine("secondary_line_example"),
                urbanization=Urbanization("urbanization_example"),
                city=City("city_example"),
                state="state_example",
                zip_code=ZipCode("04807"),
            ),
        ],
    ) # MultipleComponentsList | 
    case = "upper" # str | Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. \"PO BOX\") and proper-cased (e.g. \"PO Box\"), respectively. (optional) if omitted the server will use the default value of "upper"

    # example passing only required values which don't have defaults set
    try:
        # verifyBulk
        api_response = api_instance.verifyBulk(multiple_components_list)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UsVerificationsApi->verifyBulk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # verifyBulk
        api_response = api_instance.verifyBulk(multiple_components_list, case=case)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UsVerificationsApi->verifyBulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_components_list** | [**MultipleComponentsList**](MultipleComponentsList.md)|  |
 **case** | **str**| Casing of the verified address. Possible values are &#x60;upper&#x60; and &#x60;proper&#x60; for uppercased (e.g. \&quot;PO BOX\&quot;) and proper-cased (e.g. \&quot;PO Box\&quot;), respectively. | [optional] if omitted the server will use the default value of "upper"

### Return type

[**UsVerifications**](UsVerifications.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of US verification objects. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifySingle**
> UsVerification verifySingle(us_verifications_writable)

verifySingle

Verify a US or US territory address with a live API key.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import us_verifications_api
from lob_python.model.us_verification import UsVerification
from lob_python.model.us_verifications_writable import UsVerificationsWritable
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
    api_instance = us_verifications_api.UsVerificationsApi(api_client)
    us_verifications_writable = UsVerificationsWritable(
        address="address_example",
        recipient=Recipient("recipient_example"),
        primary_line=PrimaryLineUs("primary_line_example"),
        secondary_line=SecondaryLine("secondary_line_example"),
        urbanization=Urbanization("urbanization_example"),
        city=City("city_example"),
        state="state_example",
        zip_code=ZipCode("04807"),
    ) # UsVerificationsWritable | 
    case = "upper" # str | Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. \"PO BOX\") and proper-cased (e.g. \"PO Box\"), respectively. (optional) if omitted the server will use the default value of "upper"

    # example passing only required values which don't have defaults set
    try:
        # verifySingle
        api_response = api_instance.verifySingle(us_verifications_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UsVerificationsApi->verifySingle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # verifySingle
        api_response = api_instance.verifySingle(us_verifications_writable, case=case)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UsVerificationsApi->verifySingle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **us_verifications_writable** | [**UsVerificationsWritable**](UsVerificationsWritable.md)|  |
 **case** | **str**| Casing of the verified address. Possible values are &#x60;upper&#x60; and &#x60;proper&#x60; for uppercased (e.g. \&quot;PO BOX\&quot;) and proper-cased (e.g. \&quot;PO Box\&quot;), respectively. | [optional] if omitted the server will use the default value of "upper"

### Return type

[**UsVerification**](UsVerification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a US verification object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

