# lob_python.TemplateVersionsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TemplateVersionsApi.md#create) | **POST** /templates/{tmpl_id}/versions | create
[**delete**](TemplateVersionsApi.md#delete) | **DELETE** /templates/{tmpl_id}/versions/{vrsn_id} | delete
[**get**](TemplateVersionsApi.md#get) | **GET** /templates/{tmpl_id}/versions/{vrsn_id} | get
[**update**](TemplateVersionsApi.md#update) | **POST** /templates/{tmpl_id}/versions/{vrsn_id} | update
[**list**](TemplateVersionsApi.md#list) | **GET** /templates/{tmpl_id}/versions | list


# **create**
> TemplateVersion create(tmpl_id, template_version_writable)

create

Creates a new template version attached to the specified template.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import template_versions_api
from lob_python.model.template_version import TemplateVersion
from lob_python.model.tmpl_id import TmplId
from lob_python.model.template_version_writable import TemplateVersionWritable
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
    api_instance = template_versions_api.TemplateVersionsApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | The ID of the template the new version will be attached to
    template_version_writable = TemplateVersionWritable(
        description=ResourceDescription("description_example"),
        html=TemplateHtml("html_example"),
        engine=EngineHtml("legacy"),
    ) # TemplateVersionWritable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(tmpl_id, template_version_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| The ID of the template the new version will be attached to |
 **template_version_writable** | [**TemplateVersionWritable**](TemplateVersionWritable.md)|  |

### Return type

[**TemplateVersion**](TemplateVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the template version with the given template and version ids. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> TemplateVersionDeletion delete(tmpl_id, vrsn_id)

delete

Permanently deletes a template version. A template's `published_version` can not be deleted.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import template_versions_api
from lob_python.model.template_version_deletion import TemplateVersionDeletion
from lob_python.model.tmpl_id import TmplId
from lob_python.model.vrsn_id import VrsnId
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
    api_instance = template_versions_api.TemplateVersionsApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | The ID of the template to which the version belongs.
    vrsn_id = VrsnId("vrsn_C") # VrsnId | id of the template_version

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(tmpl_id, vrsn_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| The ID of the template to which the version belongs. |
 **vrsn_id** | **VrsnId**| id of the template_version |

### Return type

[**TemplateVersionDeletion**](TemplateVersionDeletion.md)

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
> TemplateVersion get(tmpl_id, vrsn_id)

get

Retrieves the template version with the given template and version ids.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import template_versions_api
from lob_python.model.template_version import TemplateVersion
from lob_python.model.tmpl_id import TmplId
from lob_python.model.vrsn_id import VrsnId
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
    api_instance = template_versions_api.TemplateVersionsApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | The ID of the template to which the version belongs.
    vrsn_id = VrsnId("vrsn_C") # VrsnId | id of the template_version

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(tmpl_id, vrsn_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| The ID of the template to which the version belongs. |
 **vrsn_id** | **VrsnId**| id of the template_version |

### Return type

[**TemplateVersion**](TemplateVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the template version with the given template and version ids. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> TemplateVersion update(tmpl_id, vrsn_id, template_version_updatable)

update

Updates the template version with the given template and version ids.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import template_versions_api
from lob_python.model.template_version import TemplateVersion
from lob_python.model.tmpl_id import TmplId
from lob_python.model.template_version_updatable import TemplateVersionUpdatable
from lob_python.model.vrsn_id import VrsnId
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
    api_instance = template_versions_api.TemplateVersionsApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | The ID of the template to which the version belongs.
    vrsn_id = VrsnId("vrsn_C") # VrsnId | id of the template_version
    template_version_updatable = TemplateVersionUpdatable(
        description=ResourceDescription("description_example"),
        engine=EngineHtml("legacy"),
    ) # TemplateVersionUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(tmpl_id, vrsn_id, template_version_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| The ID of the template to which the version belongs. |
 **vrsn_id** | **VrsnId**| id of the template_version |
 **template_version_updatable** | [**TemplateVersionUpdatable**](TemplateVersionUpdatable.md)|  |

### Return type

[**TemplateVersion**](TemplateVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the template version with the given template and version ids. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> TemplateVersionList list(tmpl_id)

list

Returns a list of template versions for the given template ID. The template versions are sorted by creation date, with the most recently created appearing first. 

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import template_versions_api
from lob_python.model.template_version_list import TemplateVersionList
from lob_python.model.include_model import IncludeModel
from lob_python.model.tmpl_id import TmplId
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
    api_instance = template_versions_api.TemplateVersionsApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | The ID of the template associated with the retrieved versions
    limit = 10 # int | How many results to return. (optional) if omitted the server will use the default value of 10
    before = "before_example" # str | A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response.  (optional)
    after = "after_example" # str | A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response.  (optional)
    include = IncludeModel([
        "include_example",
    ]) # IncludeModel | Request that the response include the total count by specifying `include[]=total_count`.  (optional)
    date_created = {
        "key": dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # {str: (datetime,)} | Filter by date created. (optional)

    # example passing only required values which don't have defaults set
    try:
        # list
        api_response = api_instance.list(tmpl_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(tmpl_id, limit=limit, before=before, after=after, include=include, date_created=date_created)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplateVersionsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| The ID of the template associated with the retrieved versions |
 **limit** | **int**| How many results to return. | [optional] if omitted the server will use the default value of 10
 **before** | **str**| A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the &#x60;previous_url&#x60; field in the return response.  | [optional]
 **after** | **str**| A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the &#x60;next_url&#x60; field in the return response.  | [optional]
 **include** | **IncludeModel**| Request that the response include the total count by specifying &#x60;include[]&#x3D;total_count&#x60;.  | [optional]
 **date_created** | **{str: (datetime,)}**| Filter by date created. | [optional]

### Return type

[**TemplateVersionList**](TemplateVersionList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; template versions. Each entry in the array is a separate template version object. The previous and next page of template versions can be retrieved by calling the endpoint contained in the &#x60;previous_url&#x60; and &#x60;next_url&#x60; fields in the API response respectively.&lt;br&gt;If no more template versions are available beyond the current set of returned results, the &#x60;next_url&#x60; field will be empty. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

