# IntlVerificationOrError

A model used to represent an entry in a result list where the entry can either be a intl_verification or an Error. The SDK will perform necessary casting into the correct corresponding type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**IntlVerId**](IntlVerId.md) |  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**primary_line** | **str** |  | [optional] 
**secondary_line** | [**SecondaryLine**](SecondaryLine.md) |  | [optional] 
**last_line** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**coverage** | **str** |  | [optional] 
**deliverability** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**components** | [**IntlComponents**](IntlComponents.md) |  | [optional] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "intl_verification"
**error** | [**BulkError**](BulkError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


