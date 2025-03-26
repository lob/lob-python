# lob_python.SnapPacksApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SnapPacksApi.md#create) | **POST** /snap_packs | create
[**delete**](SnapPacksApi.md#delete) | **DELETE** /snap_packs/{snp_id} | delete
[**get**](SnapPacksApi.md#get) | **GET** /snap_packs/{snp_id} | get
[**list**](SnapPacksApi.md#list) | **GET** /snap_packs | list


# **create**
> SnapPack create(snap_pack_editable)

create

Creates a new snap_pack given information

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import snap_packs_api
from lob_python.model.snap_pack import SnapPack
from lob_python.model.snap_pack_editable import SnapPackEditable
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
    api_instance = snap_packs_api.SnapPacksApi(api_client)
    snap_pack_editable = SnapPackEditable(
        to=None,
        _from=None,
        size=SnapPackSize("6x18_bifold"),
        description=ResourceDescription("description_example"),
        metadata=MetadataModel(
            key="key_example",
        ),
        mail_type=MailType("usps_first_class"),
        merge_variables=MergeVariables(),
        send_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        inside="inside_example",
        outside="outside_example",
        billing_group_id="billing_group_id_example",
        use_type=SnpUseType("marketing"),
    ) # SnapPackEditable | 
    idempotency_key = "Idempotency-Key_example" # str | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our [implementation guide](https://www.lob.com/guides#idempotent_request).  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(snap_pack_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling SnapPacksApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(snap_pack_editable, idempotency_key=idempotency_key)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling SnapPacksApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snap_pack_editable** | [**SnapPackEditable**](SnapPackEditable.md)|  |
 **idempotency_key** | **str**| A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our [implementation guide](https://www.lob.com/guides#idempotent_request).  | [optional]

### Return type

[**SnapPack**](SnapPack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a snap_pack object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SnapPackDeletion delete(snp_id)

delete

Completely removes a snap pack from production. This can only be done if the snap pack's `send_date` has not yet passed.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import snap_packs_api
from lob_python.model.snp_id import SnpId
from lob_python.model.snap_pack_deletion import SnapPackDeletion
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
    api_instance = snap_packs_api.SnapPacksApi(api_client)
    snp_id = SnpId("ord_C") # SnpId | id of the snap_pack

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_response = api_instance.delete(snp_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling SnapPacksApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snp_id** | **SnpId**| id of the snap_pack |

### Return type

[**SnapPackDeletion**](SnapPackDeletion.md)

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
> SnapPack get(snp_id)

get

Retrieves the details of an existing snap_pack. You need only supply the unique snap_pack identifier that was returned upon snap_pack creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import snap_packs_api
from lob_python.model.snap_pack import SnapPack
from lob_python.model.snp_id import SnpId
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
    api_instance = snap_packs_api.SnapPacksApi(api_client)
    snp_id = SnpId("ord_C") # SnpId | id of the snap_pack

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(snp_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling SnapPacksApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snp_id** | **SnpId**| id of the snap_pack |

### Return type

[**SnapPack**](SnapPack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a snap_pack object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> SnapPackList list()

list

Returns a list of your Snap Packs. The snap packs are returned sorted by creation date, with the most recently created snap packs appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import snap_packs_api
from lob_python.model.include_model import IncludeModel
from lob_python.model.sort_by4 import SortBy4
from lob_python.model.snap_pack_size import SnapPackSize
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.snap_pack_list import SnapPackList
from lob_python.model.lob_error import LobError
from lob_python.model.mail_type import MailType
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
    api_instance = snap_packs_api.SnapPacksApi(api_client)
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
    size = [
        SnapPackSize("6x18_bifold"),
    ] # [SnapPackSize] | The Snap Pack sizes to be returned. (optional)
    scheduled = True # bool | * `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created`  (optional)
    send_date = {
        "key": "key_example",
    } # {str: (str,)} | Filter by date sent. (optional)
    mail_type = MailType("usps_first_class") # MailType | A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a [cheaper option](https://lob.com/pricing/print-mail#compare) which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States.  (optional)
    sort_by = {
        date_created="asc",
        send_date="asc",
    } # SortBy4 | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, before=before, after=after, include=include, date_created=date_created, metadata=metadata, size=size, scheduled=scheduled, send_date=send_date, mail_type=mail_type, sort_by=sort_by)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling SnapPacksApi->list: %s\n" % e)
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
 **size** | [**[SnapPackSize]**](SnapPackSize.md)| The Snap Pack sizes to be returned. | [optional]
 **scheduled** | **bool**| * &#x60;true&#x60; - only return orders (past or future) where &#x60;send_date&#x60; is greater than &#x60;date_created&#x60; * &#x60;false&#x60; - only return orders where &#x60;send_date&#x60; is equal to &#x60;date_created&#x60;  | [optional]
 **send_date** | **{str: (str,)}**| Filter by date sent. | [optional]
 **mail_type** | **MailType**| A string designating the mail postage type: * &#x60;usps_first_class&#x60; - (default) * &#x60;usps_standard&#x60; - a [cheaper option](https://lob.com/pricing/print-mail#compare) which is less predictable and takes longer to deliver. &#x60;usps_standard&#x60; cannot be used with &#x60;4x6&#x60; postcards or for any postcards sent outside of the United States.  | [optional]
 **sort_by** | **SortBy4**| Sorts items by ascending or descending dates. Use either &#x60;date_created&#x60; or &#x60;send_date&#x60;, not both.  | [optional]

### Return type

[**SnapPackList**](SnapPackList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; snap_packs. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

