# lob_python.UploadsApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_export**](UploadsApi.md#get_export) | **GET** /uploads/{upl_id}/exports/{ex_id} | get_export
[**get**](UploadsApi.md#get) | **GET** /uploads/{upl_id} | get
[**create**](UploadsApi.md#create) | **POST** /uploads | create
[**delete**](UploadsApi.md#delete) | **DELETE** /uploads/{upl_id} | delete
[**create_export**](UploadsApi.md#create_export) | **POST** /uploads/{upl_id}/exports | create_export
[**upload_file**](UploadsApi.md#upload_file) | **POST** /uploads/{upl_id}/file | upload_file
[**update**](UploadsApi.md#update) | **PATCH** /uploads/{upl_id} | update
[**list**](UploadsApi.md#list) | **GET** /uploads | list


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

# **get**
> Upload get(upl_id)

get

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
        # get
        api_response = api_instance.get(upl_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->get: %s\n" % e)
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

# **create**
> Upload create(upload_writable)

create

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
        campaign_id=,
        required_address_column_mapping=RequiredAddressColumnMapping(
            name="null",
            address_line1="null",
            address_city="null",
            address_state="null",
            address_zip="null",
        ),
        optional_address_column_mapping=OptionalAddressColumnMapping(
            address_line2="null",
            company="null",
            address_country="null",
        ),
        metadata=UploadsMetadata(
            columns=[],
        ),
        merge_variable_column_mapping={},
    ) # UploadWritable | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(upload_writable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->create: %s\n" % e)
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

# **delete**
> delete(upl_id)

delete

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
        # delete
        api_instance.delete(upl_id)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->delete: %s\n" % e)
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

# **upload_file**
> UploadFile upload_file(upl_id, file)

upload_file

Upload an [audience file](https://help.lob.com/best-practices/campaign-audience-guide) and associate it with an upload.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import uploads_api
from lob_python.model.upload_file import UploadFile
from lob_python.model.http_validation_error import HTTPValidationError
from lob_python.model.upl_id import UplId
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
    file = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # upload_file
        api_response = api_instance.upload_file(upl_id, file)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upl_id** | **UplId**| ID of the upload |
 **file** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**UploadFile**](UploadFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Upload update(upl_id, upload_updatable)

update

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
        original_filename="original_filename_example",
        required_address_column_mapping=RequiredAddressColumnMapping(
            name="null",
            address_line1="null",
            address_city="null",
            address_state="null",
            address_zip="null",
        ),
        optional_address_column_mapping=OptionalAddressColumnMapping(
            address_line2="null",
            company="null",
            address_country="null",
        ),
        metadata=UploadsMetadata(
            columns=[],
        ),
        merge_variable_column_mapping={},
    ) # UploadUpdatable | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(upl_id, upload_updatable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->update: %s\n" % e)
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

# **list**
> UploadList list()

list

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
        # list
        api_response = api_instance.list(campaign_id=campaign_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling UploadsApi->list: %s\n" % e)
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

