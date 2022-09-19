# lob_python.IntlAutocompletionsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](IntlAutocompletionsApi.md#autocomplete) | **POST** /intl_autocompletions | autocomplete


# **autocomplete**
> IntlAutocompletions autocomplete(intl_autocompletions_writable)

autocomplete

Given an address prefix consisting of a partial primary line and country, as well as optional input of city, state, and zip code, this functionality returns up to 10 full International address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/intl_verification).

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import intl_autocompletions_api
from lob_python.model.intl_autocompletions import IntlAutocompletions
from lob_python.model.intl_autocompletions_writable import IntlAutocompletionsWritable
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
    api_instance = intl_autocompletions_api.IntlAutocompletionsApi(api_client)
    intl_autocompletions_writable = IntlAutocompletionsWritable(
        address_prefix="address_prefix_example",
        city="city_example",
        state="state_example",
        zip_code="zip_code_example",
        country=CountryExtended("AD"),
    ) # IntlAutocompletionsWritable | 
    x_lang_output = "native" # str | * `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # autocomplete
        api_response = api_instance.autocomplete(intl_autocompletions_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IntlAutocompletionsApi->autocomplete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # autocomplete
        api_response = api_instance.autocomplete(intl_autocompletions_writable, x_lang_output=x_lang_output)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling IntlAutocompletionsApi->autocomplete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intl_autocompletions_writable** | [**IntlAutocompletionsWritable**](IntlAutocompletionsWritable.md)|  |
 **x_lang_output** | **str**| * &#x60;native&#x60; - Translate response to the native language of the country in the request * &#x60;match&#x60; - match the response to the language in the request  Default response is in English.  | [optional]

### Return type

[**IntlAutocompletions**](IntlAutocompletions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an international autocompletions object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

