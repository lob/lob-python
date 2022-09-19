# lob_python.CardOrdersApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CardOrdersApi.md#create) | **POST** /cards/{card_id}/orders | create
[**get**](CardOrdersApi.md#get) | **GET** /cards/{card_id}/orders | get


# **create**
> CardOrder create(card_id, card_order_editable)

create

Creates a new card order given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import card_orders_api
from lob_python.model.card_order_editable import CardOrderEditable
from lob_python.model.card_id import CardId
from lob_python.model.card_order import CardOrder
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
    api_instance = card_orders_api.CardOrdersApi(api_client)
    card_id = CardId("card_C") # CardId | The ID of the card to which the card orders belong.
    card_order_editable = CardOrderEditable(
        quantity=10000,
    ) # CardOrderEditable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(card_id, card_order_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardOrdersApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **CardId**| The ID of the card to which the card orders belong. |
 **card_order_editable** | [**CardOrderEditable**](CardOrderEditable.md)|  |

### Return type

[**CardOrder**](CardOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Card order created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CardOrderList get(card_id)

get

Retrieves the card orders associated with the given card id.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import card_orders_api
from lob_python.model.card_order_list import CardOrderList
from lob_python.model.card_id import CardId
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
    api_instance = card_orders_api.CardOrdersApi(api_client)
    card_id = CardId("card_C") # CardId | The ID of the card to which the card orders belong.
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | An integer that designates the offset at which to begin returning results. Defaults to 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(card_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardOrdersApi->get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get
        api_response = api_instance.get(card_id, limit=limit, offset=offset)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardOrdersApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **CardId**| The ID of the card to which the card orders belong. |
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| An integer that designates the offset at which to begin returning results. Defaults to 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**CardOrderList**](CardOrderList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the card orders associated with the given card id |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

