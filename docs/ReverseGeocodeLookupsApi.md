# lob_python.ReverseGeocodeLookupsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup**](ReverseGeocodeLookupsApi.md#lookup) | **POST** /us_reverse_geocode_lookups | lookup


# **lookup**
> ReverseGeocode lookup(location)

lookup

Reverse geocode a valid US location with a live API key.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import reverse_geocode_lookups_api
from lob_python.model.location import Location
from lob_python.model.reverse_geocode import ReverseGeocode
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
    api_instance = reverse_geocode_lookups_api.ReverseGeocodeLookupsApi(api_client)
    location = Location(
        latitude=-90,
        longitude=-180,
    ) # Location | 
    size = 5 # int | Determines the number of locations returned. Possible values are between 1 and 50 and any number higher will be rounded down to 50. Default size is a list of 5 reverse geocoded locations. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # lookup
        api_response = api_instance.lookup(location)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ReverseGeocodeLookupsApi->lookup: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # lookup
        api_response = api_instance.lookup(location, size=size)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ReverseGeocodeLookupsApi->lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**Location**](Location.md)|  |
 **size** | **int**| Determines the number of locations returned. Possible values are between 1 and 50 and any number higher will be rounded down to 50. Default size is a list of 5 reverse geocoded locations. | [optional] if omitted the server will use the default value of 5

### Return type

[**ReverseGeocode**](ReverseGeocode.md)

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

