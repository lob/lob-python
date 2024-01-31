# UsVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UsVerId**](UsVerId.md) |  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**primary_line** | [**PrimaryLineUs**](PrimaryLineUs.md) |  | [optional] 
**secondary_line** | [**SecondaryLine**](SecondaryLine.md) |  | [optional] 
**urbanization** | [**Urbanization**](Urbanization.md) |  | [optional] 
**last_line** | **str** | Combination of the following applicable &#x60;components&#x60;: * City (&#x60;city&#x60;) * State (&#x60;state&#x60;) * ZIP code (&#x60;zip_code&#x60;) * ZIP+4 (&#x60;zip_code_plus_4&#x60;)  | [optional] 
**deliverability** | **str** | Summarizes the deliverability of the &#x60;us_verification&#x60; object. For full details, see the &#x60;deliverability_analysis&#x60; field. Possible values are: * &#x60;deliverable&#x60; – The address is deliverable by the USPS. * &#x60;deliverable_unnecessary_unit&#x60; – The address is deliverable, but the secondary unit information is unnecessary. * &#x60;deliverable_incorrect_unit&#x60; – The address is deliverable to the building&#39;s default address but the secondary unit provided may not exist. There is a chance the mail will not reach the intended recipient. * &#x60;deliverable_missing_unit&#x60; – The address is deliverable to the building&#39;s default address but is missing secondary unit information. There is a chance the mail will not reach the intended recipient. * &#x60;undeliverable&#x60; – The address is not deliverable according to the USPS.  | [optional] 
**valid_address** | **bool** | This field indicates whether an address was found in a more comprehensive address dataset that includes sources from the USPS, open source mapping data, and our proprietary mail delivery data. This field can be interpreted as a representation of whether an address is a real location or not. Additionally a valid address may contradict the deliverability field since an address can be a real valid location but the USPS may not deliver to that address.  | [optional] 
**components** | [**UsComponents**](UsComponents.md) |  | [optional] 
**deliverability_analysis** | [**DeliverabilityAnalysis**](DeliverabilityAnalysis.md) |  | [optional] 
**lob_confidence_score** | [**LobConfidenceScore**](LobConfidenceScore.md) |  | [optional] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "us_verification"
**transient_id** | **str** | ID that is returned in the response body for the verification  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


