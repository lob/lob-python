# lob_python.UploadsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_export**](UploadsApi.md#get_export) | **GET** /uploads/{upl_id}/exports/{ex_id} | get_export
[**create_upload**](UploadsApi.md#create_upload) | **POST** /uploads | create_upload
[**delete_upload**](UploadsApi.md#delete_upload) | **DELETE** /uploads/{upl_id} | delete_upload
[**create_export**](UploadsApi.md#create_export) | **POST** /uploads/{upl_id}/exports | create_export
[**get_upload**](UploadsApi.md#get_upload) | **GET** /uploads/{upl_id} | get_upload
[**update_upload**](UploadsApi.md#update_upload) | **PATCH** /uploads/{upl_id} | update_upload
[**list_upload**](UploadsApi.md#list_upload) | **GET** /uploads | list_upload


# **get_export**
> Export get_export(upl_id, ex_id)

get_export

Retrieves the details of an existing export. You need only supply the unique export identifier that was returned upon export creation. If you try retrieving an export immediately after creating one (i.e., before we're done processing the export), you will get back an export object with `state = in_progress`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.export import Export
from lob_python.model.upl_id import UplId
from lob_python.model.ex_id import ExId
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
    api_instance = uploads_api.UploadsApi(api_client)
    upl_id = UplId("upl_C") # UplId | ID of the upload
    ex_id = ExId("ex_C") # ExId | ID of the export

    # example passing only required values which don't have defaults set
    try:
        # get_export
        api_response = api_instance.get_export(upl_id, ex_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->get_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| ID of the upload |
 **ex_id** | **ExId**| ID of the export |

### Return type

[**Export**](Export.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an export object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> Upload create_upload(upload_writable)

create_upload

Creates a new upload with the provided properties.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upload import Upload
from lob_python.model.upload_writable import UploadWritable
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
    api_instance = uploads_api.UploadsApi(api_client)
    upload_writable = UploadWritable(
        campaign_id=CmpId("cmp_C"),
        column_mapping={},
    ) # UploadWritable | 

    # example passing only required values which don't have defaults set
    try:
        # create_upload
        api_response = api_instance.create_upload(upload_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_writable** | [**UploadWritable**](UploadWritable.md)|  |

### Return type

[**Upload**](Upload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Upload created successfully |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upload**
> delete_upload(upl_id)

delete_upload

Delete an existing upload. You need only supply the unique identifier that was returned upon upload creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upl_id import UplId
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
    api_instance = uploads_api.UploadsApi(api_client)
    upl_id = UplId("upl_C") # UplId | id of the upload

    # example passing only required values which don't have defaults set
    try:
        # delete_upload
        api_instance.delete_upload(upl_id)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->delete_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| id of the upload |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_export**
> UploadCreateExport create_export(upl_id, export_model)

create_export

Campaign Exports can help you understand exactly which records in a campaign could not be created. By initiating and retrieving an export, you will get row-by-row errors for your campaign. For a step-by-step walkthrough of creating a campaign and exporting failures, see our [Campaigns Guide](https://help.lob.com/best-practices/launching-your-first-campaign).  Create an export file associated with an upload.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upload_create_export import UploadCreateExport
from lob_python.model.export_model import ExportModel
from lob_python.model.upl_id import UplId
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
    api_instance = uploads_api.UploadsApi(api_client)
    upl_id = UplId("upl_C") # UplId | ID of the upload
    export_model = ExportModel(
        type="all",
    ) # ExportModel | 

    # example passing only required values which don't have defaults set
    try:
        # create_export
        api_response = api_instance.create_export(upl_id, export_model)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->create_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| ID of the upload |
 **export_model** | [**ExportModel**](ExportModel.md)|  |

### Return type

[**UploadCreateExport**](UploadCreateExport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload**
> Upload get_upload(upl_id)

get_upload

Retrieves the details of an existing upload. You need only supply the unique upload identifier that was returned upon upload creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upload import Upload
from lob_python.model.upl_id import UplId
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
    api_instance = uploads_api.UploadsApi(api_client)
    upl_id = UplId("upl_C") # UplId | id of the upload

    # example passing only required values which don't have defaults set
    try:
        # get_upload
        api_response = api_instance.get_upload(upl_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->get_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| id of the upload |

### Return type

[**Upload**](Upload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an upload object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_upload**
> Upload update_upload(upl_id, upload_updatable)

update_upload

Update the details of an existing upload. You need only supply the unique identifier that was returned upon upload creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upload import Upload
from lob_python.model.upload_updatable import UploadUpdatable
from lob_python.model.upl_id import UplId
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
    api_instance = uploads_api.UploadsApi(api_client)
    upl_id = UplId("upl_C") # UplId | id of the upload
    upload_updatable = UploadUpdatable(
        column_mapping={},
        state=UploadState("Draft"),
        original_filename="original_filename_example",
        overwrite_column_mapping=True,
    ) # UploadUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update_upload
        api_response = api_instance.update_upload(upl_id, upload_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->update_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| id of the upload |
 **upload_updatable** | [**UploadUpdatable**](UploadUpdatable.md)|  |

### Return type

[**Upload**](Upload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an upload object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_upload**
> UploadList list_upload()

list_upload

Returns a list of your uploads. Optionally, filter uploads by campaign.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.cmp_id import CmpId
from lob_python.model.upload_list import UploadList
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
    api_instance = uploads_api.UploadsApi(api_client)
    campaign_id = CmpId("cmp_C") # CmpId | id of the campaign (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list_upload
        api_response = api_instance.list_upload(campaign_id=campaign_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->list_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **CmpId**| id of the campaign | [optional]

### Return type

[**UploadList**](UploadList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of matching uploads. Each entry in the array is a separate upload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

