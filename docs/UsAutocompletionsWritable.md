# UsAutocompletionsWritable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_prefix** | **str** | Only accepts numbers and street names in an alphanumeric format.  | 
**city** | **str** | An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations.  | [optional] 
**state** | **str** | An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations.  | [optional] 
**zip_code** | **str** | An optional ZIP Code input used to filter suggestions. Matches partial entries.  | [optional] 
**geo_ip_sort** | **bool** | If &#x60;true&#x60;, sort suggestions by proximity to the IP set in the &#x60;X-Forwarded-For&#x60; header.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


