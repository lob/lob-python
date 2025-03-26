# Zip


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ZipId**](ZipId.md) |  | 
**cities** | [**[ZipLookupCity]**](ZipLookupCity.md) | An array of city objects containing valid cities for the &#x60;zip_code&#x60;. Multiple cities will be returned if more than one city is associated with the input ZIP code.  | 
**zip_code_type** | [**ZipCodeType**](ZipCodeType.md) |  | 
**object** | **str** |  | defaults to "us_zip_lookup"
**zip_code** | **str** | A 5-digit ZIP code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


