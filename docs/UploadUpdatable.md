# UploadUpdatable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_mapping** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The mapping of column headers in your file to Lob-required fields for the resource created. See our &lt;a href&#x3D;\&quot;https://help.lob.com/best-practices/campaign-audience-guide\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Campaign Audience Guide&lt;/a&gt; for additional details. | [optional] 
**state** | [**UploadState**](UploadState.md) |  | [optional] 
**original_filename** | **str** | Original filename provided when the upload is created. | [optional] 
**overwrite_column_mapping** | **bool** | Properties in &#x60;columnMapping&#x60; will be appended to the existing &#x60;columnMapping&#x60; object if set to &#x60;false&#x60;. If set to &#x60;true&#x60;, the existing &#x60;columnMapping&#x60; object will be overwritten with the data supplied in &#x60;columnMapping&#x60; property.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


