# lob_python.BillingGroupsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BillingGroupsApi.md#create) | **POST** /billing_groups | create
[**get**](BillingGroupsApi.md#get) | **GET** /billing_groups/{bg_id} | get
[**update**](BillingGroupsApi.md#update) | **POST** /billing_groups/{bg_id} | update
[**list**](BillingGroupsApi.md#list) | **GET** /billing_groups | list


# **create**
> BillingGroup create(billing_group_editable)

create

Creates a new billing_group with the provided properties.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import billing_groups_api
from lob_python.model.billing_group_editable import BillingGroupEditable
from lob_python.model.billing_group import BillingGroup
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
    api_instance = billing_groups_api.BillingGroupsApi(api_client)
    billing_group_editable = BillingGroupEditable(
        description=BgDescription("description_example"),
        name=Name("name_example"),
    ) # BillingGroupEditable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(billing_group_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BillingGroupsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_group_editable** | [**BillingGroupEditable**](BillingGroupEditable.md)|  |

### Return type

[**BillingGroup**](BillingGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a billing group object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> BillingGroup get(bg_id)

get

Retrieves the details of an existing billing_group. You need only supply the unique billing_group identifier that was returned upon billing_group creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import billing_groups_api
from lob_python.model.billing_group import BillingGroup
from lob_python.model.bg_id import BgId
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
    api_instance = billing_groups_api.BillingGroupsApi(api_client)
    bg_id = BgId("bg_C") # BgId | id of the billing_group

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(bg_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BillingGroupsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bg_id** | **BgId**| id of the billing_group |

### Return type

[**BillingGroup**](BillingGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a billing_group object. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> BillingGroup update(bg_id, billing_group_editable)

update

Updates all editable attributes of the billing_group with the given id.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import billing_groups_api
from lob_python.model.billing_group_editable import BillingGroupEditable
from lob_python.model.billing_group import BillingGroup
from lob_python.model.bg_id import BgId
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
    api_instance = billing_groups_api.BillingGroupsApi(api_client)
    bg_id = BgId("bg_C") # BgId | id of the billing_group
    billing_group_editable = BillingGroupEditable(
        description=BgDescription("description_example"),
        name=Name("name_example"),
    ) # BillingGroupEditable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(bg_id, billing_group_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BillingGroupsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bg_id** | **BgId**| id of the billing_group |
 **billing_group_editable** | [**BillingGroupEditable**](BillingGroupEditable.md)|  |

### Return type

[**BillingGroup**](BillingGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a billing group object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> BillingGroupList list()

list

Returns a list of your billing_groups. The billing_groups are returned sorted by creation date, with the most recently created billing_groups appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import billing_groups_api
from lob_python.model.sort_by5 import SortBy5
from lob_python.model.include_model import IncludeModel
from lob_python.model.billing_group_list import BillingGroupList
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
    api_instance = billing_groups_api.BillingGroupsApi(api_client)
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | An integer that designates the offset at which to begin returning results. Defaults to 0. (optional) if omitted the server will use the default value of 0
    include = IncludeModel([
        "include_example",
    ]) # IncludeModel | Request that the response include the total count by specifying `include[]=total_count`.  (optional)
    date_created = {
        "key": dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # {str: (datetime,)} | Filter by date created. (optional)
    date_modified = {
        "key": "key_example",
    } # {str: (str,)} | Filter by date modified. (optional)
    sort_by = {
        date_created="asc",
        send_date="asc",
    } # SortBy5 | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, offset=offset, include=include, date_created=date_created, date_modified=date_modified, sort_by=sort_by)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BillingGroupsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| An integer that designates the offset at which to begin returning results. Defaults to 0. | [optional] if omitted the server will use the default value of 0
 **include** | **IncludeModel**| Request that the response include the total count by specifying &#x60;include[]&#x3D;total_count&#x60;.  | [optional]
 **date_created** | **{str: (datetime,)}**| Filter by date created. | [optional]
 **date_modified** | **{str: (str,)}**| Filter by date modified. | [optional]
 **sort_by** | **SortBy5**| Sorts items by ascending or descending dates. Use either &#x60;date_created&#x60; or &#x60;send_date&#x60;, not both.  | [optional]

### Return type

[**BillingGroupList**](BillingGroupList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of billing_groups. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

