# Letter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**Address**](Address.md) |  | 
**_from** | [**Address**](Address.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**id** | [**LtrId**](LtrId.md) |  | 
**return_envelope** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**object** | **str** |  | defaults to "letter"
**carrier** | **str** |  | [optional]  if omitted the server will use the default value of "USPS"
**thumbnails** | [**[Thumbnail]**](Thumbnail.md) |  | [optional] 
**expected_delivery_date** | **date** | A date in YYYY-MM-DD format of the mailpiece&#39;s expected delivery date based on its &#x60;send_date&#x60;. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**template_id** | [**TmplId**](TmplId.md) |  | [optional] 
**template_version_id** | [**VrsnId**](VrsnId.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**merge_variables** | [**MergeVariables**](MergeVariables.md) |  | [optional] 
**send_date** | **datetime** | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the &#x60;send_date&#x60; has passed, the mailpiece can be canceled. If a date in the format &#x60;2017-11-01&#x60; is passed, it will evaluate to midnight UTC of that date (&#x60;2017-11-01T00:00:00.000Z&#x60;). If a datetime is passed, that exact time will be used. A &#x60;send_date&#x60; passed with no time zone will default to UTC, while a &#x60;send_date&#x60; passed with a time zone will be converted to UTC. | [optional] 
**extra_service** | **str** | Add an extra service to your letter. See [pricing](https://www.lob.com/pricing/print-mail#compare) for extra costs incurred. | [optional] 
**tracking_number** | **str, none_type** | The tracking number, if applicable, will appear here when it becomes available. Dummy tracking numbers are not created in test mode. | [optional] 
**tracking_events** | [**[TrackingEventNormal]**](TrackingEventNormal.md) | Tracking events are not populated for registered or regular (no extra service) letters. | [optional] 
**return_address** | **str** | Specifies the address the return envelope will be sent back to. This is an optional argument that is available if an account is signed up for the return envelope tracking beta, and has &#x60;return_envelope&#x60;, and &#x60;perforated_page&#x60; fields populated in the API request. | [optional] 
**mail_type** | [**MailType**](MailType.md) |  | [optional] 
**color** | **bool** | Set this key to &#x60;true&#x60; if you would like to print in color. Set to &#x60;false&#x60; if you would like to print in black and white. | [optional] 
**double_sided** | **bool** | Set this attribute to &#x60;true&#x60; for double sided printing, or &#x60;false&#x60; for for single sided printing. Defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**address_placement** | **str** | Specifies the location of the address information that will show through the double-window envelope.  | [optional]  if omitted the server will use the default value of "top_first_page"
**perforated_page** | **int, none_type** | Required if &#x60;return_envelope&#x60; is &#x60;true&#x60;. The number of the page that should be perforated for use with the return envelope. Must be greater than or equal to &#x60;1&#x60;. The blank page added by &#x60;address_placement&#x3D;insert_blank_page&#x60; will be ignored when considering the perforated page number. To see how perforation will impact your letter design, view our [perforation guide](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf). | [optional] 
**custom_envelope** | [**LetterCustomEnvelope**](LetterCustomEnvelope.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


