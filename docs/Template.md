# Template


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TmplId**](TmplId.md) |  | 
**versions** | [**[TemplateVersion]**](TemplateVersion.md) | An array of all non-deleted [version objects](#tag/Template-Versions) associated with the template. | 
**published_version** | [**TemplateVersion**](TemplateVersion.md) |  | 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**object** | **str** | Value is resource type. | [optional]  if omitted the server will use the default value of "template"
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


