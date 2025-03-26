# AddressEditable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The building number, street name, street suffix, and any street directionals. For US addresses, the max length is 64 characters. | [optional] 
**address_line2** | **str, none_type** | The suite or apartment number of the recipient address, if applicable. For US addresses, the max length is 64 characters. | [optional] 
**address_city** | **str, none_type** |  | [optional] 
**address_state** | **str, none_type** |  | [optional] 
**address_zip** | **str, none_type** | Optional postal code. For US addresses, must be either 5 or 9 digits. | [optional] 
**address_country** | [**CountryExtended**](CountryExtended.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**name** | **str, none_type** | name associated with address. | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**phone** | **str, none_type** | Must be no longer than 40 characters. | [optional] 
**email** | **str, none_type** | Must be no longer than 100 characters. | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


