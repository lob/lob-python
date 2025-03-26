# UploadUpdatable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_filename** | **str** | Original filename provided when the upload is created. | [optional] 
**required_address_column_mapping** | [**RequiredAddressColumnMapping**](RequiredAddressColumnMapping.md) |  | [optional] 
**optional_address_column_mapping** | [**OptionalAddressColumnMapping**](OptionalAddressColumnMapping.md) |  | [optional] 
**metadata** | [**UploadsMetadata**](UploadsMetadata.md) |  | [optional] 
**merge_variable_column_mapping** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The mapping of column headers in your file to the merge variables present in your creative. See our &lt;a href&#x3D;\&quot;https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#step-3-map-merge-variable-data-if-applicable-7\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Campaign Audience Guide&lt;/a&gt; for additional details. &lt;br /&gt;If a merge variable has the same \&quot;name\&quot; as a \&quot;key\&quot; in the &#x60;requiredAddressColumnMapping&#x60; or &#x60;optionalAddressColumnMapping&#x60; objects, then they **CANNOT** have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the &#x60;requiredAddressColumnMapping&#x60; or &#x60;optionalAddressColumnMapping&#x60; objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


