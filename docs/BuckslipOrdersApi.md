# lob_python.BuckslipOrdersApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BuckslipOrdersApi.md#create) | **POST** /buckslips/{buckslip_id}/orders | create
[**get**](BuckslipOrdersApi.md#get) | **GET** /buckslips/{buckslip_id}/orders | get


# **create**
> BuckslipOrder create(buckslip_id, buckslip_order_editable)

create

Creates a new buckslip order given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslip_orders_api
from lob_python.model.buckslip_order_editable import BuckslipOrderEditable
from lob_python.model.buckslip_id import BuckslipId
from lob_python.model.lob_error import LobError
from lob_python.model.buckslip_order import BuckslipOrder
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
    api_instance = buckslip_orders_api.BuckslipOrdersApi(api_client)
    buckslip_id = BuckslipId("bck_C") # BuckslipId | The ID of the buckslip to which the buckslip orders belong.
    buckslip_order_editable = BuckslipOrderEditable(
        quantity=5000,
    ) # BuckslipOrderEditable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(buckslip_id, buckslip_order_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipOrdersApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_id** | **BuckslipId**| The ID of the buckslip to which the buckslip orders belong. |
 **buckslip_order_editable** | [**BuckslipOrderEditable**](BuckslipOrderEditable.md)|  |

### Return type

[**BuckslipOrder**](BuckslipOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Buckslip order created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> BuckslipOrdersList get(buckslip_id)

get

Retrieves the buckslip orders associated with the given buckslip id.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslip_orders_api
from lob_python.model.buckslip_orders_list import BuckslipOrdersList
from lob_python.model.buckslip_id import BuckslipId
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
    api_instance = buckslip_orders_api.BuckslipOrdersApi(api_client)
    buckslip_id = BuckslipId("bck_C") # BuckslipId | The ID of the buckslip to which the buckslip orders belong.
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | An integer that designates the offset at which to begin returning results. Defaults to 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(buckslip_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipOrdersApi->get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get
        api_response = api_instance.get(buckslip_id, limit=limit, offset=offset)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipOrdersApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_id** | **BuckslipId**| The ID of the buckslip to which the buckslip orders belong. |
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| An integer that designates the offset at which to begin returning results. Defaults to 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**BuckslipOrdersList**](BuckslipOrdersList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the buckslip orders associated with the given buckslip id |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

