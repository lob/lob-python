# CardEditable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**front** | **str** | A PDF template for the front of the card | 
**back** | **str** | A PDF template for the back of the card | [optional]  if omitted the server will use the default value of "https://s3.us-west-2.amazonaws.com/public.lob.com/assets/card_blank_horizontal.pdf"
**size** | **str** | The size of the card | [optional]  if omitted the server will use the default value of "2.125x3.375"
**description** | [**CardDescription**](CardDescription.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


