# CardOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**object** | **str** | Value is type of resource. | 
**id** | [**CoId**](CoId.md) |  | [optional] 
**card_id** | [**CardId**](CardId.md) |  | [optional] 
**status** | **str** | The status of the card order. | [optional] 
**inventory** | **float** | The inventory of the card order. | [optional]  if omitted the server will use the default value of 0
**quantity_ordered** | **float** | The quantity of cards ordered | [optional]  if omitted the server will use the default value of 0
**unit_price** | **float** | The unit price for the card order. | [optional]  if omitted the server will use the default value of 0
**cancelled_reason** | **str** | The reason for cancellation. | [optional] 
**availability_date** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**expected_availability_date** | **datetime** | The fixed deadline for the cards to be printed. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


