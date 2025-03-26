# Buckslip


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BuckslipId**](BuckslipId.md) |  | 
**reorder_quantity** | **int, none_type** | The number of buckslips to be reordered. | 
**url** | **str** | The signed link for the buckslip. | 
**raw_url** | **str** | The raw URL of the buckslip. | 
**front_original_url** | **str** | The original URL of the front template. | 
**back_original_url** | **str** | The original URL of the back template. | 
**thumbnails** | [**[Thumbnail]**](Thumbnail.md) |  | 
**buckslip_orders** | [**[BuckslipOrder]**](BuckslipOrder.md) | An array of buckslip orders that are associated with the buckslip. | 
**stock** | **str** |  | 
**finish** | **str** |  | 
**status** | **str** |  | 
**description** | [**BuckslipDescription**](BuckslipDescription.md) |  | 
**auto_reorder** | **bool** | True if the buckslips should be auto-reordered. | defaults to False
**threshold_amount** | **int** | The threshold amount of the buckslip | defaults to 0
**available_quantity** | **float** | The available quantity of buckslips. | defaults to 0
**allocated_quantity** | **float** | The allocated quantity of buckslips. | defaults to 0
**onhand_quantity** | **float** | The onhand quantity of buckslips. | defaults to 0
**pending_quantity** | **float** | The pending quantity of buckslips. | defaults to 0
**projected_quantity** | **float** | The sum of pending and onhand quantities of buckslips. | defaults to 0
**weight** | **str** |  | defaults to "80#"
**object** | **str** | object | defaults to "buckslip"
**size** | **str** | The size of the buckslip | [optional]  if omitted the server will use the default value of "8.75x3.75"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


