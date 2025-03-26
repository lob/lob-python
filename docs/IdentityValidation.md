# IdentityValidation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**IdentityValidationId**](IdentityValidationId.md) |  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**primary_line** | [**PrimaryLineUs**](PrimaryLineUs.md) |  | [optional] 
**secondary_line** | [**SecondaryLine**](SecondaryLine.md) |  | [optional] 
**urbanization** | [**Urbanization**](Urbanization.md) |  | [optional] 
**last_line** | **str** | Combination of the following applicable &#x60;components&#x60;: * City (&#x60;city&#x60;) * State (&#x60;state&#x60;) * ZIP code (&#x60;zip_code&#x60;) * ZIP+4 (&#x60;zip_code_plus_4&#x60;)  | [optional] 
**score** | **float, none_type** | A numerical score between 0 and 100 that represents the likelihood the provided name is associated with a physical address.  | [optional] 
**confidence** | **str** | Indicates the likelihood the recipient name and address match based on our custom internal calculation. Possible values are: - &#x60;high&#x60; — Has a Lob confidence score greater than 70. - &#x60;medium&#x60; — Has a Lob confidence score between 40 and 70. - &#x60;low&#x60; — Has a Lob confidence score less than 40. - &#x60;\&quot;\&quot;&#x60; — No tracking data exists for this address.  | [optional] 
**object** | **str** | Value is resource type. | [optional]  if omitted the server will use the default value of "id_validation"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


