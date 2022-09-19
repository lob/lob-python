# CheckEditable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | Must either be an address ID or an inline object with correct address parameters. | 
**to** | **str** | Must either be an address ID or an inline object with correct address parameters. | 
**bank_account** | **str, none_type** |  | 
**amount** | **float** | The payment amount to be sent in US dollars. | 
**logo** | **str** | Accepts a remote URL or local file upload to an image to print (in grayscale) in the upper-left corner of your check. | [optional] 
**check_bottom** | **str** | The artwork to use on the bottom of the check page.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 8.5\&quot;x11\&quot; at 300 DPI, while supplied HTML will be rendered and trimmed to fit on a 8.5\&quot;x11\&quot; page. - The check bottom will always be printed in black &amp; white. - Must conform to [this template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_bottom_template.pdf).  Need more help? Consult our [HTML examples](#section/HTML-Examples). | [optional] 
**attachment** | **str** | A document to include with the check. | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**merge_variables** | [**MergeVariables**](MergeVariables.md) |  | [optional] 
**send_date** | **datetime** | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default [cancellation window](#section/Cancellation-Windows) applied to the mailpiece. Until the &#x60;send_date&#x60; has passed, the mailpiece can be canceled. If a date in the format &#x60;2017-11-01&#x60; is passed, it will evaluate to midnight UTC of that date (&#x60;2017-11-01T00:00:00.000Z&#x60;). If a datetime is passed, that exact time will be used. A &#x60;send_date&#x60; passed with no time zone will default to UTC, while a &#x60;send_date&#x60; passed with a time zone will be converted to UTC. | [optional] 
**mail_type** | **str** | Checks must be sent &#x60;usps_first_class&#x60; | [optional]  if omitted the server will use the default value of "usps_first_class"
**memo** | **str, none_type** | Text to include on the memo line of the check. | [optional] 
**check_number** | **int** | An integer that designates the check number. | [optional] 
**message** | **str** | Max of 400 characters to be included at the bottom of the check page. | [optional] 
**billing_group_id** | **str** | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See [Billing Group API](https://lob.github.io/lob-openapi/#tag/Billing-Groups) for more information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


