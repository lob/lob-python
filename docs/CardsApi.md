# lob_python.CardsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CardsApi.md#create) | **POST** /cards | create
[**delete**](CardsApi.md#delete) | **DELETE** /cards/{card_id} | delete
[**get**](CardsApi.md#get) | **GET** /cards/{card_id} | get
[**update**](CardsApi.md#update) | **POST** /cards/{card_id} | update
[**list**](CardsApi.md#list) | **GET** /cards | list


# **create**
> Card create(card_editable)

create

Creates a new card given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import cards_api
from lob_python.model.card_editable import CardEditable
from lob_python.model.card import Card
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
    api_instance = cards_api.CardsApi(api_client)
    card_editable = CardEditable(
        front="front_example",
        back="https://s3.us-west-2.amazonaws.com/public.lob.com/assets/card_blank_horizontal.pdf",
        size="2.125x3.375",
        description=CardDescription("description_example"),
    ) # CardEditable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(card_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_editable** | [**CardEditable**](CardEditable.md)|  |

### Return type

[**Card**](Card.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Card created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> CardDeletion delete(card_id)

delete

Delete an existing card. You need only supply the unique identifier that was returned upon card creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import cards_api
from lob_python.model.card_deletion import CardDeletion
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
    api_instance = cards_api.CardsApi(api_client)
    card_id = CardId("card_C") # CardId | id of the card

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(card_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **CardId**| id of the card |

### Return type

[**CardDeletion**](CardDeletion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted the card |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Card get(card_id)

get

Retrieves the details of an existing card. You need only supply the unique customer identifier that was returned upon card creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import cards_api
from lob_python.model.card_id import CardId
from lob_python.model.card import Card
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
    api_instance = cards_api.CardsApi(api_client)
    card_id = CardId("card_C") # CardId | id of the card

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(card_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **CardId**| id of the card |

### Return type

[**Card**](Card.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a card object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Card update(card_id, card_updatable)

update

Update the details of an existing card. You need only supply the unique identifier that was returned upon card creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import cards_api
from lob_python.model.card_updatable import CardUpdatable
from lob_python.model.card_id import CardId
from lob_python.model.card import Card
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
    api_instance = cards_api.CardsApi(api_client)
    card_id = CardId("card_C") # CardId | id of the card
    card_updatable = CardUpdatable(
        description=CardDescription("description_example"),
        auto_reorder=True,
        reorder_quantity=10000,
    ) # CardUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(card_id, card_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **CardId**| id of the card |
 **card_updatable** | [**CardUpdatable**](CardUpdatable.md)|  |

### Return type

[**Card**](Card.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a card object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> CardList list()

list

Returns a list of your cards. The cards are returned sorted by creation date, with the most recently created addresses appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import cards_api
from lob_python.model.sort_by5 import SortBy5
from lob_python.model.card_list import CardList
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
    api_instance = cards_api.CardsApi(api_client)
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    before = "before_example" # str | A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response.  (optional)
    after = "after_example" # str | A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response.  (optional)
    sort_by = {
        date_created="asc",
        send_date="asc",
    } # SortBy5 | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, before=before, after=after, sort_by=sort_by)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CardsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **before** | **str**| A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the &#x60;previous_url&#x60; field in the return response.  | [optional]
 **after** | **str**| A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the &#x60;next_url&#x60; field in the return response.  | [optional]
 **sort_by** | **SortBy5**| Sorts items by ascending or descending dates. Use either &#x60;date_created&#x60; or &#x60;send_date&#x60;, not both.  | [optional]

### Return type

[**CardList**](CardList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of card objects |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

