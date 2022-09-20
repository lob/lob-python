# Postcard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PscId**](PscId.md) |  | 
**url** | [**SignedLink**](SignedLink.md) |  | 
**to** | [**Address**](Address.md) |  | [optional] 
**_from** | [**AddressDomesticExpanded**](AddressDomesticExpanded.md) |  | [optional] 
**carrier** | **str** |  | [optional]  if omitted the server will use the default value of "USPS"
**thumbnails** | [**[Thumbnail]**](Thumbnail.md) |  | [optional] 
**size** | [**PostcardSize**](PostcardSize.md) |  | [optional] 
**expected_delivery_date** | **date** | A date in YYYY-MM-DD format of the mailpiece&#39;s expected delivery date based on its &#x60;send_date&#x60;. | [optional] 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**front_template_id** | **str, none_type** | The unique ID of the HTML template used for the front of the postcard. | [optional] 
**back_template_id** | **str, none_type** | The unique ID of the HTML template used for the back of the postcard. | [optional] 
**front_template_version_id** | **str, none_type** | The unique ID of the specific version of the HTML template used for the front of the postcard. | [optional] 
**back_template_version_id** | **str, none_type** | The unique ID of the specific version of the HTML template used for the back of the postcard. | [optional] 
**tracking_events** | [**[TrackingEventNormal], none_type**](TrackingEventNormal.md) | An array of tracking_event objects ordered by ascending &#x60;time&#x60;. Will not be populated for postcards created in test mode. | [optional] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "postcard"
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**mail_type** | [**MailType**](MailType.md) |  | [optional] 
**merge_variables** | [**MergeVariables**](MergeVariables.md) |  | [optional] 
**send_date** | **datetime** | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the &#x60;send_date&#x60; has passed, the mailpiece can be canceled. If a date in the format &#x60;2017-11-01&#x60; is passed, it will evaluate to midnight UTC of that date (&#x60;2017-11-01T00:00:00.000Z&#x60;). If a datetime is passed, that exact time will be used. A &#x60;send_date&#x60; passed with no time zone will default to UTC, while a &#x60;send_date&#x60; passed with a time zone will be converted to UTC. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


