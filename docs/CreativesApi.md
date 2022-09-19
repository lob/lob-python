# lob_python.CreativesApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CreativesApi.md#create) | **POST** /creatives | create
[**get**](CreativesApi.md#get) | **GET** /creatives/{crv_id} | get
[**update**](CreativesApi.md#update) | **PATCH** /creatives/{crv_id} | update


# **create**
> CreativeResponse create(creative_writable)

create

Creates a new creative with the provided properties

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import creatives_api
from lob_python.model.creative_writable import CreativeWritable
from lob_python.model.creative_response import CreativeResponse
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
    api_instance = creatives_api.CreativesApi(api_client)
    creative_writable = CreativeWritable(
        _from=None,
        description=ResourceDescription("description_example"),
        metadata=MetadataModel(
            key="key_example",
        ),
        resource_type="letter",
        campaign_id=CmpId("cmp_C"),
        details=None,
        file="file_example",
        front="front_example",
        back="back_example",
    ) # CreativeWritable | 
    x_lang_output = "native" # str | * `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(creative_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CreativesApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(creative_writable, x_lang_output=x_lang_output)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CreativesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creative_writable** | [**CreativeWritable**](CreativeWritable.md)|  |
 **x_lang_output** | **str**| * &#x60;native&#x60; - Translate response to the native language of the country in the request * &#x60;match&#x60; - match the response to the language in the request  Default response is in English.  | [optional]

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creative created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CreativeResponse get(crv_id)

get

Retrieves the details of an existing creative. You need only supply the unique creative identifier that was returned upon creative creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import creatives_api
from lob_python.model.crv_id import CrvId
from lob_python.model.creative_response import CreativeResponse
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
    api_instance = creatives_api.CreativesApi(api_client)
    crv_id = CrvId("crv_C") # CrvId | id of the creative

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(crv_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CreativesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crv_id** | **CrvId**| id of the creative |

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a creative object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CreativeResponse update(crv_id, creative_patch)

update

Update the details of an existing creative. You need only supply the unique identifier that was returned upon creative creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import creatives_api
from lob_python.model.crv_id import CrvId
from lob_python.model.creative_patch import CreativePatch
from lob_python.model.creative_response import CreativeResponse
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
    api_instance = creatives_api.CreativesApi(api_client)
    crv_id = CrvId("crv_C") # CrvId | id of the creative
    creative_patch = CreativePatch(
        _from=None,
        description=ResourceDescription("description_example"),
        metadata=MetadataModel(
            key="key_example",
        ),
    ) # CreativePatch | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(crv_id, creative_patch)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CreativesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crv_id** | **CrvId**| id of the creative |
 **creative_patch** | [**CreativePatch**](CreativePatch.md)|  |

### Return type

[**CreativeResponse**](CreativeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a creative object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

