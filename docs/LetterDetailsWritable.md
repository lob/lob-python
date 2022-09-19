# LetterDetailsWritable

Properties that the letters in your Creative should have.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**[CardId], none_type**](CardId.md) | A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information. | 
**color** | **bool** | Set this key to &#x60;true&#x60; if you would like to print in color. Set to &#x60;false&#x60; if you would like to print in black and white. | 
**address_placement** | **str** | Specifies the location of the address information that will show through the double-window envelope.  | [optional]  if omitted the server will use the default value of "top_first_page"
**double_sided** | **bool** | Set this attribute to &#x60;true&#x60; for double sided printing, or &#x60;false&#x60; for for single sided printing. Defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**extra_service** | **str** | Add an extra service to your letter. | [optional] 
**mail_type** | [**MailType**](MailType.md) |  | [optional] 
**return_envelope** | **bool** |  | [optional]  if omitted the server will use the default value of False
**custom_envelope** | [**CustomEnvelopeUserProvided**](CustomEnvelopeUserProvided.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


