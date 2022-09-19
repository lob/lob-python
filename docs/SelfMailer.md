# SelfMailer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**SfmId**](SfmId.md) |  | 
**to** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**url** | [**SignedLink**](SignedLink.md) |  | 
**_from** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**size** | [**SelfMailerSize**](SelfMailerSize.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**mail_type** | [**MailType**](MailType.md) |  | [optional] 
**merge_variables** | [**MergeVariables**](MergeVariables.md) |  | [optional] 
**send_date** | **datetime** | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the &#x60;send_date&#x60; has passed, the mailpiece can be canceled. If a date in the format &#x60;2017-11-01&#x60; is passed, it will evaluate to midnight UTC of that date (&#x60;2017-11-01T00:00:00.000Z&#x60;). If a datetime is passed, that exact time will be used. A &#x60;send_date&#x60; passed with no time zone will default to UTC, while a &#x60;send_date&#x60; passed with a time zone will be converted to UTC. | [optional] 
**outside_template_id** | **str, none_type** | The unique ID of the HTML template used for the outside of the self mailer. | [optional] 
**inside_template_id** | **str, none_type** | The unique ID of the HTML template used for the inside of the self mailer. | [optional] 
**outside_template_version_id** | **str, none_type** | The unique ID of the specific version of the HTML template used for the outside of the self mailer. | [optional] 
**inside_template_version_id** | **str, none_type** | The unique ID of the specific version of the HTML template used for the inside of the self mailer. | [optional] 
**object** | **str** | Value is resource type. | [optional]  if omitted the server will use the default value of "self_mailer"
**tracking_events** | [**[TrackingEventCertified]**](TrackingEventCertified.md) | An array of certified tracking events ordered by ascending &#x60;time&#x60;. Not populated in test mode. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


