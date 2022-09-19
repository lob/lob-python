# Upload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UplId**](UplId.md) |  | 
**account_id** | **str** | Account ID that made the request | 
**campaign_id** | [**CmpId**](CmpId.md) |  | 
**column_mapping** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The mapping of column headers in your file to Lob-required fields for the resource created. See our &lt;a href&#x3D;\&quot;https://help.lob.com/best-practices/campaign-audience-guide\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Campaign Audience Guide&lt;/a&gt; for additional details. | 
**mode** | **str** | The environment in which the mailpieces were created. Today, will only be &#x60;live&#x60;. | 
**state** | [**UploadState**](UploadState.md) |  | 
**total_mailpieces** | **int** | Total number of recipients for the campaign | 
**failed_mailpieces** | **int** | Number of mailpieces that failed to create | 
**validated_mailpieces** | **int** | Number of mailpieces that were successfully created | 
**bytes_processed** | **int** | Number of bytes processed in your CSV | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the upload was created | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the upload was last modified | 
**failures_url** | **str** | Url where your campaign mailpiece failures can be retrieved | [optional] 
**original_filename** | **str** | Filename of the upload | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


