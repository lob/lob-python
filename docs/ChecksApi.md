# lob_python.ChecksApi

All URIs are relative to *https://api.lob.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](ChecksApi.md#cancel) | **DELETE** /checks/{chk_id} | cancel
[**create**](ChecksApi.md#create) | **POST** /checks | create
[**get**](ChecksApi.md#get) | **GET** /checks/{chk_id} | get
[**list**](ChecksApi.md#list) | **GET** /checks | list


# **cancel**
> CheckDeletion cancel(chk_id)

cancel

Completely removes a check from production. This can only be done if the check has a `send_date` and the `send_date` has not yet passed. If the check is successfully canceled, you will not be charged for it. Read more on [cancellation windows](#section/Cancellation-Windows) and [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation is a premium feature. Upgrade to the appropriate [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions) to gain access.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import checks_api
from lob_python.model.chk_id import ChkId
from lob_python.model.check_deletion import CheckDeletion
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
    api_instance = checks_api.ChecksApi(api_client)
    chk_id = ChkId("chk_C") # ChkId | id of the check

    # example passing only required values which don't have defaults set
    try:
        # cancel
        api_response = api_instance.cancel(chk_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ChecksApi->cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chk_id** | **ChkId**| id of the check |

### Return type

[**CheckDeletion**](CheckDeletion.md)

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

# **create**
> Check create(check_editable)

create

Creates a new check with the provided properties.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import checks_api
from lob_python.model.check_editable import CheckEditable
from lob_python.model.check import Check
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
    api_instance = checks_api.ChecksApi(api_client)
    check_editable = CheckEditable(
        _from="_from_example",
        to="to_example",
        bank_account="bank_account_example",
        amount=3.14,
        logo="logo_example",
        check_bottom="check_bottom_example",
        attachment="attachment_example",
        description=ResourceDescription("description_example"),
        metadata=MetadataModel(
            key="key_example",
        ),
        merge_variables=MergeVariables(),
        send_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        mail_type="usps_first_class",
        memo="memo_example",
        check_number=1,
        message="message_example",
        billing_group_id="billing_group_id_example",
    ) # CheckEditable | 
    idempotency_key = "Idempotency-Key_example" # str | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our [implementation guide](https://www.lob.com/guides#idempotent_request).  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(check_editable)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ChecksApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(check_editable, idempotency_key=idempotency_key)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ChecksApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_editable** | [**CheckEditable**](CheckEditable.md)|  |
 **idempotency_key** | **str**| A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our [implementation guide](https://www.lob.com/guides#idempotent_request).  | [optional]

### Return type

[**Check**](Check.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a check object |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Check get(chk_id)

get

Retrieves the details of an existing check. You need only supply the unique check identifier that was returned upon check creation.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import checks_api
from lob_python.model.check import Check
from lob_python.model.chk_id import ChkId
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
    api_instance = checks_api.ChecksApi(api_client)
    chk_id = ChkId("chk_C") # ChkId | id of the check

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(chk_id)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ChecksApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chk_id** | **ChkId**| id of the check |

### Return type

[**Check**](Check.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a check object |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> CheckList list()

list

Returns a list of your checks. The checks are returned sorted by creation date, with the most recently created checks appearing first.

### Example

* Basic Authentication (basicAuth):

```python
import time
import lob_python
from lob_python.api import checks_api
from lob_python.model.sort_by5 import SortBy5
from lob_python.model.include_model import IncludeModel
from lob_python.model.check_list import CheckList
from lob_python.model.metadata_model import MetadataModel
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
    api_instance = checks_api.ChecksApi(api_client)
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
    scheduled = True # bool | * `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created`  (optional)
    send_date = {
        "key": "key_example",
    } # {str: (str,)} | Filter by date sent. (optional)
    mail_type = MailType("usps_first_class") # MailType | A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a [cheaper option](https://lob.com/pricing/print-mail#compare) which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States.  (optional)
    sort_by = {
        date_created="asc",
        send_date="asc",
    } # SortBy5 | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(limit=limit, before=before, after=after, include=include, date_created=date_created, metadata=metadata, scheduled=scheduled, send_date=send_date, mail_type=mail_type, sort_by=sort_by)
        pprint(api_response)
    except lob_python.ApiException as e:
        print("Exception when calling ChecksApi->list: %s\n" % e)
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
 **scheduled** | **bool**| * &#x60;true&#x60; - only return orders (past or future) where &#x60;send_date&#x60; is greater than &#x60;date_created&#x60; * &#x60;false&#x60; - only return orders where &#x60;send_date&#x60; is equal to &#x60;date_created&#x60;  | [optional]
 **send_date** | **{str: (str,)}**| Filter by date sent. | [optional]
 **mail_type** | **MailType**| A string designating the mail postage type: * &#x60;usps_first_class&#x60; - (default) * &#x60;usps_standard&#x60; - a [cheaper option](https://lob.com/pricing/print-mail#compare) which is less predictable and takes longer to deliver. &#x60;usps_standard&#x60; cannot be used with &#x60;4x6&#x60; postcards or for any postcards sent outside of the United States.  | [optional]
 **sort_by** | **SortBy5**| Sorts items by ascending or descending dates. Use either &#x60;date_created&#x60; or &#x60;send_date&#x60;, not both.  | [optional]

### Return type

[**CheckList**](CheckList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with a data property that contains an array of up to &#x60;limit&#x60; checks. |  -  |
**0** | Lob uses RESTful HTTP response codes to indicate success or failure of an API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

