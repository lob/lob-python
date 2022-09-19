# lob_python.ZipLookupsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup**](ZipLookupsApi.md#lookup) | **POST** /us_zip_lookups | lookup


# **lookup**
> Zip lookup(zip_editable)

lookup

Returns information about a ZIP code

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import zip_lookups_api
from lob_python.model.zip import Zip
from lob_python.model.zip_editable import ZipEditable
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
    api_instance = zip_lookups_api.ZipLookupsApi(api_client)
    zip_editable = ZipEditable(
        zip_code="04807",
    ) # ZipEditable | 

    # example passing only required values which don't have defaults set
    try:
        # lookup
        api_response = api_instance.lookup(zip_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ZipLookupsApi->lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_editable** | [**ZipEditable**](ZipEditable.md)|  |

### Return type

[**Zip**](Zip.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a zip lookup object if a valid zip was provided. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

