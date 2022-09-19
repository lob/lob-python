# lob_python.CampaignsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CampaignsApi.md#create) | **POST** /campaigns | create
[**delete**](CampaignsApi.md#delete) | **DELETE** /campaigns/{cmp_id} | delete
[**get**](CampaignsApi.md#get) | **GET** /campaigns/{cmp_id} | get
[**update**](CampaignsApi.md#update) | **PATCH** /campaigns/{cmp_id} | update
[**list**](CampaignsApi.md#list) | **GET** /campaigns | list


# **create**
> Campaign create(campaign_writable)

create

Creates a new campaign with the provided properties. See how to launch your first campaign [here](https://help.lob.com/best-practices/launching-your-first-campaign).

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import campaigns_api
from lob_python.model.campaign import Campaign
from lob_python.model.campaign_writable import CampaignWritable
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    campaign_writable = CampaignWritable(
        billing_group_id="bg_C",
        name="name_example",
        description=ResourceDescription("description_example"),
        schedule_type=CmpScheduleType("immediate"),
        target_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        send_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        cancel_window_campaign_minutes=1,
        metadata=MetadataModel(
            key="key_example",
        ),
        use_type=CmpUseType("marketing"),
        auto_cancel_if_ncoa=True,
    ) # CampaignWritable | 
    x_lang_output = "native" # str | * `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(campaign_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(campaign_writable, x_lang_output=x_lang_output)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_writable** | [**CampaignWritable**](CampaignWritable.md)|  |
 **x_lang_output** | **str**| * &#x60;native&#x60; - Translate response to the native language of the country in the request * &#x60;match&#x60; - match the response to the language in the request  Default response is in English.  | [optional]

### Return type

[**Campaign**](Campaign.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> dict delete(cmp_id)

delete

Delete an existing campaign. You need only supply the unique identifier that was returned upon campaign creation. Deleting a campaign also deletes any associated mail pieces that have been created but not sent. A campaign's `send_date` matches its associated mail pieces' `send_date`s.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import campaigns_api
from lob_python.model.cmp_id import CmpId
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    cmp_id = CmpId("cmp_C") # CmpId | id of the campaign

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(cmp_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_id** | **CmpId**| id of the campaign |

### Return type

**dict**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted the campaign. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Campaign get(cmp_id)

get

Retrieves the details of an existing campaign. You need only supply the unique campaign identifier that was returned upon campaign creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import campaigns_api
from lob_python.model.campaign import Campaign
from lob_python.model.cmp_id import CmpId
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    cmp_id = CmpId("cmp_C") # CmpId | id of the campaign

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(cmp_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_id** | **CmpId**| id of the campaign |

### Return type

[**Campaign**](Campaign.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a campaign object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Campaign update(cmp_id, campaign_updatable)

update

Update the details of an existing campaign. You need only supply the unique identifier that was returned upon campaign creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import campaigns_api
from lob_python.model.campaign import Campaign
from lob_python.model.cmp_id import CmpId
from lob_python.model.campaign_updatable import CampaignUpdatable
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    cmp_id = CmpId("cmp_C") # CmpId | id of the campaign
    campaign_updatable = CampaignUpdatable(
        name="name_example",
        description=ResourceDescription("description_example"),
        schedule_type=CmpScheduleType("immediate"),
        target_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        send_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        cancel_window_campaign_minutes=1,
        metadata=MetadataModel(
            key="key_example",
        ),
        is_draft=True,
        use_type=CmpUseType("marketing"),
        auto_cancel_if_ncoa=True,
    ) # CampaignUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(cmp_id, campaign_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_id** | **CmpId**| id of the campaign |
 **campaign_updatable** | [**CampaignUpdatable**](CampaignUpdatable.md)|  |

### Return type

[**Campaign**](Campaign.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a campaign object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> CampaignsList list()

list

Returns a list of your campaigns. The campaigns are returned sorted by creation date, with the most recently created campaigns appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import campaigns_api
from lob_python.model.include_model import IncludeModel
from lob_python.model.campaigns_list import CampaignsList
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    include = IncludeModel([
        "include_example",
    ]) # IncludeModel | Request that the response include the total count by specifying `include[]=total_count`.  (optional)
    before = "before_example" # str | A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response.  (optional)
    after = "after_example" # str | A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, include=include, before=before, after=after)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling CampaignsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **include** | **IncludeModel**| Request that the response include the total count by specifying &#x60;include[]&#x3D;total_count&#x60;.  | [optional]
 **before** | **str**| A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the &#x60;previous_url&#x60; field in the return response.  | [optional]
 **after** | **str**| A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the &#x60;next_url&#x60; field in the return response.  | [optional]

### Return type

[**CampaignsList**](CampaignsList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; campaigns. Each entry in the array is a separate letter. The previous and next page of campaigns can be retrieved by calling the endpoint contained in the &#x60;previous_url&#x60; and &#x60;next_url&#x60; fields in the API response respectively. If no more campaigns are available beyond the current set of returned results, the &#x60;next_url&#x60; field will be empty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

