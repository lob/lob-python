# Upload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UplId**](UplId.md) |  | 
**account_id** | **str** | Account ID that made the request | 
**mode** | **str** | The environment in which the mailpieces were created. Today, will only be &#x60;live&#x60;. | 
**campaign_id** | **str** | Campaign ID associated with the upload | 
**state** | [**UploadState**](UploadState.md) |  | 
**total_mailpieces** | **int** | Total number of recipients for the campaign | 
**failed_mailpieces** | **int** | Number of mailpieces that failed to create | 
**validated_mailpieces** | **int** | Number of mailpieces that were successfully created | 
**bytes_processed** | **int** | Number of bytes processed in your CSV | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the upload was created | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the upload was last modified | 
**required_address_column_mapping** | [**RequiredAddressColumnMapping**](RequiredAddressColumnMapping.md) |  | 
**optional_address_column_mapping** | [**OptionalAddressColumnMapping**](OptionalAddressColumnMapping.md) |  | 
**metadata** | [**UploadsMetadata**](UploadsMetadata.md) |  | 
**merge_variable_column_mapping** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The mapping of column headers in your file to the merge variables present in your creative. See our &lt;a href&#x3D;\&quot;https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#step-3-map-merge-variable-data-if-applicable-7\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Campaign Audience Guide&lt;/a&gt; for additional details. &lt;br /&gt;If a merge variable has the same \&quot;name\&quot; as a \&quot;key\&quot; in the &#x60;requiredAddressColumnMapping&#x60; or &#x60;optionalAddressColumnMapping&#x60; objects, then they **CANNOT** have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the &#x60;requiredAddressColumnMapping&#x60; or &#x60;optionalAddressColumnMapping&#x60; objects. | 
**failures_url** | **str** | Url where your campaign mailpiece failures can be retrieved | [optional] 
**original_filename** | **str** | Filename of the upload | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


