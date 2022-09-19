# Check


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ChkId**](ChkId.md) |  | 
**to** | [**Address**](Address.md) |  | 
**amount** | **float** | The payment amount to be sent in US dollars. | 
**bank_account** | [**BankAccount**](BankAccount.md) |  | 
**url** | [**SignedLink**](SignedLink.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**carrier** | **str** |  | defaults to "USPS"
**object** | **str** |  | defaults to "check"
**_from** | [**Address**](Address.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**merge_variables** | [**MergeVariables**](MergeVariables.md) |  | [optional] 
**send_date** | **datetime** | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the &#x60;send_date&#x60; has passed, the mailpiece can be canceled. If a date in the format &#x60;2017-11-01&#x60; is passed, it will evaluate to midnight UTC of that date (&#x60;2017-11-01T00:00:00.000Z&#x60;). If a datetime is passed, that exact time will be used. A &#x60;send_date&#x60; passed with no time zone will default to UTC, while a &#x60;send_date&#x60; passed with a time zone will be converted to UTC. | [optional] 
**mail_type** | **str** | Checks must be sent &#x60;usps_first_class&#x60; | [optional]  if omitted the server will use the default value of "usps_first_class"
**memo** | **str, none_type** | Text to include on the memo line of the check. | [optional] 
**check_number** | **int** | An integer that designates the check number. If &#x60;check_number&#x60; is not provided, checks created from a new &#x60;bank_account&#x60; will start at &#x60;10000&#x60; and increment with each check created with the &#x60;bank_account&#x60;. A provided &#x60;check_number&#x60; overrides the defaults. Subsequent checks created with the same &#x60;bank_account&#x60; will increment from the provided check number. | [optional] 
**message** | **str** | Max of 400 characters to be included at the bottom of the check page. | [optional] 
**check_bottom_template_id** | [**TmplId**](TmplId.md) |  | [optional] 
**attachment_template_id** | [**TmplId**](TmplId.md) |  | [optional] 
**check_bottom_template_version_id** | [**VrsnId**](VrsnId.md) |  | [optional] 
**attachment_template_version_id** | [**VrsnId**](VrsnId.md) |  | [optional] 
**thumbnails** | [**[Thumbnail]**](Thumbnail.md) |  | [optional] 
**expected_delivery_date** | **date** | A date in YYYY-MM-DD format of the mailpiece&#39;s expected delivery date based on its &#x60;send_date&#x60;. | [optional] 
**tracking_events** | [**[TrackingEventNormal], none_type**](TrackingEventNormal.md) | An array of tracking_event objects ordered by ascending &#x60;time&#x60;. Will not be populated for checks created in test mode. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


