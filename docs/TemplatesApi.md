# lob_python.TemplatesApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TemplatesApi.md#create) | **POST** /templates | create
[**delete**](TemplatesApi.md#delete) | **DELETE** /templates/{tmpl_id} | delete
[**get**](TemplatesApi.md#get) | **GET** /templates/{tmpl_id} | get
[**update**](TemplatesApi.md#update) | **POST** /templates/{tmpl_id} | update
[**list**](TemplatesApi.md#list) | **GET** /templates | list


# **create**
> Template create(template_writable)

create

Creates a new template for use with the Print & Mail API. In Live mode, you can only have as many non-deleted templates as allotted in your current [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions). If you attempt to create a template past your limit, you will receive a `403` error. There is no limit in Test mode.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import templates_api
from lob_python.model.template_writable import TemplateWritable
from lob_python.model.template import Template
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
    api_instance = templates_api.TemplatesApi(api_client)
    template_writable = TemplateWritable(
        description=ResourceDescription("description_example"),
        html=TemplateHtml("html_example"),
        metadata=MetadataModel(
            key="key_example",
        ),
        engine=EngineHtml("legacy"),
    ) # TemplateWritable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(template_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplatesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_writable** | [**TemplateWritable**](TemplateWritable.md)|  |

### Return type

[**Template**](Template.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a template object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> TemplateDeletion delete(tmpl_id)

delete

Permanently deletes a template.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import templates_api
from lob_python.model.tmpl_id import TmplId
from lob_python.model.template_deletion import TemplateDeletion
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
    api_instance = templates_api.TemplatesApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | id of the template

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(tmpl_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplatesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| id of the template |

### Return type

[**TemplateDeletion**](TemplateDeletion.md)

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
> Template get(tmpl_id)

get

Retrieves the details of an existing template.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import templates_api
from lob_python.model.tmpl_id import TmplId
from lob_python.model.template import Template
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
    api_instance = templates_api.TemplatesApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | id of the template

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(tmpl_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplatesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| id of the template |

### Return type

[**Template**](Template.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a template object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Template update(tmpl_id, template_update)

update

Updates the description and/or published version of the template with the given id.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import templates_api
from lob_python.model.tmpl_id import TmplId
from lob_python.model.template_update import TemplateUpdate
from lob_python.model.template import Template
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
    api_instance = templates_api.TemplatesApi(api_client)
    tmpl_id = TmplId("tmpl_C") # TmplId | id of the template
    template_update = TemplateUpdate(
        description=ResourceDescription("description_example"),
        published_version=VrsnId("vrsn_C"),
    ) # TemplateUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(tmpl_id, template_update)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling TemplatesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmpl_id** | **TmplId**| id of the template |
 **template_update** | [**TemplateUpdate**](TemplateUpdate.md)|  |

### Return type

[**Template**](Template.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated template object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> TemplateList list()

list

Returns a list of your templates. The templates are returned sorted by creation date, with the most recently created templates appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import templates_api
from lob_python.model.include_model import IncludeModel
from lob_python.model.template_list import TemplateList
from lob_python.model.metadata_model import MetadataModel
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
    api_instance = templates_api.TemplatesApi(api_client)
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
        print("Exception when calling TemplatesApi->list: %s\n" % e)
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

[**TemplateList**](TemplateList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; templates. Each entry in the array is a separate template. The previous and next page of templates can be retrieved by calling the endpoint contained in the &#x60;previous_url&#x60; and &#x60;next_url&#x60; fields in the API response respectively.&lt;br&gt;If no more templates are available beyond the current set of returned results, the &#x60;next_url&#x60; field will be empty. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

