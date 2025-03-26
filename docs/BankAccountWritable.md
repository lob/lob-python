# BankAccountWritable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | Must be a [valid US routing number](https://www.frbservices.org/index.html). | 
**account_number** | **str** |  | 
**account_type** | [**BankTypeEnum**](BankTypeEnum.md) |  | 
**signatory** | **str** | The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the [Dashboard](https://dashboard.lob.com/#/login). | 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


