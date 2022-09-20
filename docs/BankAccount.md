# BankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | Must be a [valid US routing number](https://www.frbservices.org/index.html). | 
**account_number** | **str** |  | 
**account_type** | **str** | The type of entity that holds the account. | 
**signatory** | **str** | The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the [Dashboard](https://dashboard.lob.com/#/login). | 
**id** | [**BankId**](BankId.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**object** | **str** |  | defaults to "bank_account"
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**signature_url** | **str, none_type** | A signed link to the signature image. will be generated. | [optional] 
**bank_name** | **str** | The name of the bank based on the provided routing number, e.g. &#x60;JPMORGAN CHASE BANK&#x60;. | [optional] 
**verified** | **bool** | A bank account must be verified before a check can be created. | [optional]  if omitted the server will use the default value of False
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


