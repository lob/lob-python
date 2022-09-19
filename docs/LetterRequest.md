# LetterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **bool, date, datetime, dict, float, int, list, str, none_type** | Must either be an address ID or an inline object with correct address parameters. | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**resource_type** | **str** | Mailpiece type for the creative | [optional]  if omitted the server will use the default value of "letter"
**campaign_id** | [**CmpId**](CmpId.md) |  | [optional] 
**details** | [**LetterDetailsWritable**](LetterDetailsWritable.md) |  | [optional] 
**file** | **str** | PDF file containing the letter&#39;s formatting. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


