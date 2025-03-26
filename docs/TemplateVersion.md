# TemplateVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**VrsnId**](VrsnId.md) |  | 
**html** | [**TemplateHtml**](TemplateHtml.md) |  | 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**engine** | [**EngineHtml**](EngineHtml.md) |  | [optional] 
**suggest_json_editor** | **bool** | Used by frontend, true if the template uses advanced features.  | [optional] 
**merge_variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Used by frontend, an object representing the keys of every merge variable present in the template. It has one key named &#39;keys&#39;, and its value is an array of strings.  | [optional] 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**object** | **str** | Value is resource type. | [optional]  if omitted the server will use the default value of "version"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


