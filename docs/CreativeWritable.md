# CreativeWritable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **bool, date, datetime, dict, float, int, list, str, none_type** | Must either be an address ID or an inline object with correct address parameters. | 
**resource_type** | **str** | Mailpiece type for the creative | 
**campaign_id** | [**CmpId**](CmpId.md) |  | 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**details** | **bool, date, datetime, dict, float, int, list, str, none_type** | Either PostcardDetailsWritable or LetterDetailsWritable | [optional] 
**file** | **str** | PDF file containing the letter&#39;s formatting. Do not include for resource_type &#x3D; postcard. | [optional] 
**front** | **str** | The artwork to use as the front of your postcard. Do not include for resource_type &#x3D; letter.  | [optional] 
**back** | **str** | The artwork to use as the back of your postcard. Do not include for resource_type &#x3D; letter.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


