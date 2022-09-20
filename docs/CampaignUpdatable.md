# CampaignUpdatable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**schedule_type** | [**CmpScheduleType**](CmpScheduleType.md) |  | [optional] 
**target_delivery_date** | **datetime** | If &#x60;schedule_type&#x60; is &#x60;target_delivery_date&#x60;, provide a targeted delivery date for mail pieces in this campaign. | [optional] 
**send_date** | **datetime** | If &#x60;schedule_type&#x60; is &#x60;scheduled_send_date&#x60;, provide a date to send this campaign. | [optional] 
**cancel_window_campaign_minutes** | **int** | A window, in minutes, within which the campaign can be canceled. | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**is_draft** | **bool** | Whether or not the campaign is still a draft. | [optional]  if omitted the server will use the default value of True
**use_type** | [**CmpUseType**](CmpUseType.md) |  | [optional] 
**auto_cancel_if_ncoa** | **bool** | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


