# UsVerificationOrError

A model used to represent an entry in a result list where the entry can either be a us_verification or an Error. The SDK will perform necessary casting into the correct corresponding type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UsVerId**](UsVerId.md) |  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**primary_line** | [**PrimaryLineUs**](PrimaryLineUs.md) |  | [optional] 
**secondary_line** | [**SecondaryLine**](SecondaryLine.md) |  | [optional] 
**urbanization** | [**Urbanization**](Urbanization.md) |  | [optional] 
**last_line** | **str** |  | [optional] 
**deliverability** | **str** |  | [optional] 
**components** | [**UsComponents**](UsComponents.md) |  | [optional] 
**deliverability_analysis** | [**DeliverabilityAnalysis**](DeliverabilityAnalysis.md) |  | [optional] 
**lob_confidence_score** | [**LobConfidenceScore**](LobConfidenceScore.md) |  | [optional] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "us_verification"
**transient_id** | **str** | ID that is returned in the response body for the verification  | [optional] 
**error** | [**BulkError**](BulkError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


