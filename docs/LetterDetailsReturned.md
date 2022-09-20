# LetterDetailsReturned

Properties that the letters in your Creative should have.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **bool** | Set this key to &#x60;true&#x60; if you would like to print in color, false for black and white. | 
**cards** | [**[CardId], none_type**](CardId.md) | A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information. | 
**address_placement** | **str** | Specifies the location of the address information that will show through the double-window envelope.  | [optional]  if omitted the server will use the default value of "top_first_page"
**custom_envelope** | [**CustomEnvelopeReturned**](CustomEnvelopeReturned.md) |  | [optional] 
**double_sided** | **bool** | Set this attribute to &#x60;true&#x60; for double sided printing,  &#x60;false&#x60; for for single sided printing. | [optional]  if omitted the server will use the default value of True
**extra_service** | **str** | Add an extra service to your letter. | [optional] 
**mail_type** | [**MailType**](MailType.md) |  | [optional] 
**return_envelope** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**bleed** | **bool** | Allows for letter bleed. Enabled only with specific feature flags. | [optional]  if omitted the server will use the default value of False
**file_original_url** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


