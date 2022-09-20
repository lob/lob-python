# lob_python.AddressesApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AddressesApi.md#create) | **POST** /addresses | create
[**delete**](AddressesApi.md#delete) | **DELETE** /addresses/{adr_id} | delete
[**get**](AddressesApi.md#get) | **GET** /addresses/{adr_id} | get
[**list**](AddressesApi.md#list) | **GET** /addresses | list


# **create**
> Address create(address_editable)

create

Creates a new address given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import addresses_api
from lob_python.model.address import Address
from lob_python.model.address_editable import AddressEditable
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
    api_instance = addresses_api.AddressesApi(api_client)
    address_editable = AddressEditable(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        address_city="address_city_example",
        address_state="address_state_example",
        address_zip="address_zip_example",
        address_country=CountryExtended("AD"),
        description=ResourceDescription("description_example"),
        name="name_example",
        company=Company("company_example"),
        phone="phone_example",
        email="email_example",
        metadata=MetadataModel(
            key="key_example",
        ),
    ) # AddressEditable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(address_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling AddressesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_editable** | [**AddressEditable**](AddressEditable.md)|  |

### Return type

[**Address**](Address.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Echos the writable fields of a newly created address object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AddressDeletion delete(adr_id)

delete

Deletes the details of an existing address.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import addresses_api
from lob_python.model.adr_id import AdrId
from lob_python.model.lob_error import LobError
from lob_python.model.address_deletion import AddressDeletion
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
    api_instance = addresses_api.AddressesApi(api_client)
    adr_id = AdrId("adr_C") # AdrId | id of the address

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(adr_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling AddressesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adr_id** | **AdrId**| id of the address |

### Return type

[**AddressDeletion**](AddressDeletion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Address get(adr_id)

get

Retrieves the details of an existing address.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import addresses_api
from lob_python.model.adr_id import AdrId
from lob_python.model.address import Address
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
    api_instance = addresses_api.AddressesApi(api_client)
    adr_id = AdrId("adr_C") # AdrId | id of the address

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(adr_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling AddressesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adr_id** | **AdrId**| id of the address |

### Return type

[**Address**](Address.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an address object if a valid identifier was provided. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> AddressList list()

list

Returns a list of your addresses.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import addresses_api
from lob_python.model.include_model import IncludeModel
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.lob_error import LobError
from lob_python.model.address_list import AddressList
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
    api_instance = addresses_api.AddressesApi(api_client)
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    before = "before_example" # str | A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response.  (optional)
    after = "after_example" # str | A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response.  (optional)
    include = IncludeModel([
        "include_example",
    ]) # IncludeModel | Request that the response include the total count by specifying `include[]=total_count`.  (optional)
    date_created = {
        "key": dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # {str: (datetime,)} | Filter by date created. (optional)
    metadata = MetadataModel(
        key="key_example",
    ) # MetadataModel | Filter by metadata key-value pair`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, before=before, after=after, include=include, date_created=date_created, metadata=metadata)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling AddressesApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **before** | **str**| A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the &#x60;previous_url&#x60; field in the return response.  | [optional]
 **after** | **str**| A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the &#x60;next_url&#x60; field in the return response.  | [optional]
 **include** | **IncludeModel**| Request that the response include the total count by specifying &#x60;include[]&#x3D;total_count&#x60;.  | [optional]
 **date_created** | **{str: (datetime,)}**| Filter by date created. | [optional]
 **metadata** | **MetadataModel**| Filter by metadata key-value pair&#x60;. | [optional]

### Return type

[**AddressList**](AddressList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; addresses. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

