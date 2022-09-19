# CardDeletion

Lob uses RESTful HTTP response codes to indicate success or failure of an API request. In general, 2xx indicates success, 4xx indicate an input error, and 5xx indicates an error on Lob's end.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CardId**](CardId.md) |  | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**object** | **str** | Value is type of resource. | [optional]  if omitted the server will use the default value of "card_deleted"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


