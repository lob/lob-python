# lob_python.BuckslipsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BuckslipsApi.md#create) | **POST** /buckslips | create
[**delete**](BuckslipsApi.md#delete) | **DELETE** /buckslips/{buckslip_id} | delete
[**get**](BuckslipsApi.md#get) | **GET** /buckslips/{buckslip_id} | get
[**update**](BuckslipsApi.md#update) | **PATCH** /buckslips/{buckslip_id} | update
[**List**](BuckslipsApi.md#List) | **GET** /buckslips | List


# **create**
> Buckslip create(buckslip_editable)

create

Creates a new buckslip given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslips_api
from lob_python.model.buckslip import Buckslip
from lob_python.model.lob_error import LobError
from lob_python.model.str_bool_date_datetime_dict_float_int_list_str_none_type import StrBoolDateDatetimeDictFloatIntListStrNoneType
from lob_python.model.buckslip_editable import BuckslipEditable
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
    api_instance = buckslips_api.BuckslipsApi(api_client)
    buckslip_editable = BuckslipEditable(
        front="front_example",
        back="back_example",
        description=BuckslipDescription("description_example"),
        size="8.75x3.75",
    ) # BuckslipEditable | 
    front = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | An optional file upload as either a byte array or file type.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(buckslip_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(buckslip_editable, front=front)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_editable** | [**BuckslipEditable**](BuckslipEditable.md)|  |
 **front** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| An optional file upload as either a byte array or file type.  | [optional]

### Return type

[**Buckslip**](Buckslip.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Buckslip created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> BuckslipDeletion delete(buckslip_id)

delete

Delete an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslips_api
from lob_python.model.buckslip_deletion import BuckslipDeletion
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
    api_instance = buckslips_api.BuckslipsApi(api_client)
    buckslip_id = BuckslipId("bck_C") # BuckslipId | id of the buckslip

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(buckslip_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_id** | **BuckslipId**| id of the buckslip |

### Return type

[**BuckslipDeletion**](BuckslipDeletion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted the buckslip |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Buckslip get(buckslip_id)

get

Retrieves the details of an existing buckslip. You need only supply the unique customer identifier that was returned upon buckslip creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslips_api
from lob_python.model.buckslip import Buckslip
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
    api_instance = buckslips_api.BuckslipsApi(api_client)
    buckslip_id = BuckslipId("bck_C") # BuckslipId | id of the buckslip

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(buckslip_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_id** | **BuckslipId**| id of the buckslip |

### Return type

[**Buckslip**](Buckslip.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a buckslip object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Buckslip update(buckslip_id, buckslip_updatable)

update

Update the details of an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslips_api
from lob_python.model.buckslip import Buckslip
from lob_python.model.buckslip_id import BuckslipId
from lob_python.model.buckslip_updatable import BuckslipUpdatable
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
    api_instance = buckslips_api.BuckslipsApi(api_client)
    buckslip_id = BuckslipId("bck_C") # BuckslipId | id of the buckslip
    buckslip_updatable = BuckslipUpdatable(
        description=BuckslipDescription("description_example"),
        auto_reorder=True,
        reorder_quantity=5000,
    ) # BuckslipUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(buckslip_id, buckslip_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buckslip_id** | **BuckslipId**| id of the buckslip |
 **buckslip_updatable** | [**BuckslipUpdatable**](BuckslipUpdatable.md)|  |

### Return type

[**Buckslip**](Buckslip.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a buckslip object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **List**
> BuckslipsList List()

List

Returns a list of your buckslips. The buckslips are returned sorted by creation date, with the most recently created buckslips appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import buckslips_api
from lob_python.model.buckslips_list import BuckslipsList
from lob_python.model.include_model import IncludeModel
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
    api_instance = buckslips_api.BuckslipsApi(api_client)
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    before = "before_example" # str | A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response.  (optional)
    after = "after_example" # str | A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response.  (optional)
    include = IncludeModel([
        "include_example",
    ]) # IncludeModel | Request that the response include the total count by specifying `include[]=total_count`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List
        api_response = api_instance.List(limit=limit, before=before, after=after, include=include)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling BuckslipsApi->List: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **before** | **str**| A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the &#x60;previous_url&#x60; field in the return response.  | [optional]
 **after** | **str**| A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the &#x60;next_url&#x60; field in the return response.  | [optional]
 **include** | **IncludeModel**| Request that the response include the total count by specifying &#x60;include[]&#x3D;total_count&#x60;.  | [optional]

### Return type

[**BuckslipsList**](BuckslipsList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description: Returns a list of buckslip objects |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

