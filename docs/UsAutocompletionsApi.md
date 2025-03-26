# lob_python.UsAutocompletionsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](UsAutocompletionsApi.md#autocomplete) | **POST** /us_autocompletions | autocomplete


# **autocomplete**
> UsAutocompletions autocomplete(us_autocompletions_writable)

autocomplete

Given an address prefix consisting of a partial primary line, as well as optional input of city, state, and zip code, this functionality returns up to 10 full US address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/verification_us).

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import us_autocompletions_api
from lob_python.model.us_autocompletions import UsAutocompletions
from lob_python.model.us_autocompletions_writable import UsAutocompletionsWritable
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
    api_instance = us_autocompletions_api.UsAutocompletionsApi(api_client)
    us_autocompletions_writable = UsAutocompletionsWritable(
        address_prefix="address_prefix_example",
        city="city_example",
        state="state_example",
        zip_code="zip_code_example",
        geo_ip_sort=True,
    ) # UsAutocompletionsWritable | 

    # example passing only required values which don't have defaults set
    try:
        # autocomplete
        api_response = api_instance.autocomplete(us_autocompletions_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UsAutocompletionsApi->autocomplete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **us_autocompletions_writable** | [**UsAutocompletionsWritable**](UsAutocompletionsWritable.md)|  |

### Return type

[**UsAutocompletions**](UsAutocompletions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a US autocompletion object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

