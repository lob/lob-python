# UsVerificationsWritable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The entire address in one string (e.g., \&quot;2261 Market Street 94114\&quot;). _Does not support a recipient and will error when other payload parameters are provided._  | [optional] 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**primary_line** | [**PrimaryLineUs**](PrimaryLineUs.md) |  | [optional] 
**secondary_line** | [**SecondaryLine**](SecondaryLine.md) |  | [optional] 
**urbanization** | [**Urbanization**](Urbanization.md) |  | [optional] 
**city** | [**City**](City.md) |  | [optional] 
**state** | **str** | The [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:US) two letter code or subdivision name for the state. &#x60;city&#x60; and &#x60;state&#x60; are required if no &#x60;zip_code&#x60; is passed. | [optional] 
**zip_code** | [**ZipCode**](ZipCode.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


