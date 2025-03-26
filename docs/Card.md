# Card


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CardId**](CardId.md) |  | 
**url** | **str** | The signed link for the card. | 
**thumbnails** | [**[Thumbnail]**](Thumbnail.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**auto_reorder** | **bool** | True if the cards should be auto-reordered. | defaults to False
**available_quantity** | **int** | The available quantity of cards. | defaults to 0
**pending_quantity** | **int** | The pending quantity of cards. | defaults to 0
**object** | **str** | object | defaults to "card"
**size** | **str** | The size of the card | defaults to "2.125x3.375"
**reorder_quantity** | **int, none_type** | The number of cards to be reordered. Only present when auto_reorder is True. | [optional] 
**raw_url** | **str** | The raw URL of the card. | [optional] 
**front_original_url** | **str** | The original URL of the front template. | [optional] 
**back_original_url** | **str** | The original URL of the back template. | [optional] 
**status** | **str** |  | [optional] 
**orientation** | **str** | The orientation of the card. | [optional]  if omitted the server will use the default value of "horizontal"
**threshold_amount** | **int** | The threshold amount of the card | [optional]  if omitted the server will use the default value of 0
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**description** | [**CardDescription**](CardDescription.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


