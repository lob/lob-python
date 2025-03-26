# CreativeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CrvId**](CrvId.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**_from** | **bool, date, datetime, dict, float, int, list, str, none_type** | Must either be an address ID or an inline object with correct address parameters. | [optional] 
**resource_type** | **str** | Mailpiece type for the creative | [optional] 
**details** | **bool, date, datetime, dict, float, int, list, str, none_type** | Either PostcardDetailsReturned or LetterDetailsReturned | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**template_preview_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Preview URLs associated with a creative&#39;s artwork asset(s) if the creative uses HTML templates as assets. | [optional] 
**template_previews** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | A list of template preview objects if the creative uses HTML template(s) as artwork asset(s). | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**campaigns** | [**[Campaign]**](Campaign.md) | Array of campaigns associated with the creative ID | [optional] 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | [optional] 
**object** | **str** | Value is resource type. | [optional]  if omitted the server will use the default value of "creative"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


