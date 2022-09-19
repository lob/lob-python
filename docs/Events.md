# Events


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier prefixed with &#x60;evt_&#x60;. | 
**body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The body of the associated resource as they were at the time of the event, i.e. the [postcard object](https://docs.lob.com/#tag/Postcards/operation/postcard_retrieve), [the letter object](https://docs.lob.com/#tag/Letters/operation/letter_retrieve), [the check object](https://docs.lob.com/#tag/Checks/operation/check_retrieve), [the address object](https://docs.lob.com/#tag/Addresses/operation/address_retrieve), or [the bank account object](https://docs.lob.com/#tag/Bank-Accounts/operation/bank_account_retrieve). For &#x60;.deleted&#x60; events, the body matches the response for the corresponding delete endpoint for that resource (e.g. the [postcard cancel response](https://docs.lob.com/#tag/Postcards/operation/postcard_delete)). | 
**reference_id** | **str** | Unique identifier of the related resource for the event. | 
**event_type** | [**EventType**](EventType.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**object** | **str** | Value is resource type. | defaults to "event"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


