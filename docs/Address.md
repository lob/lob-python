# Address


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AdrId**](AdrId.md) |  | [optional] 
**description** | [**ResourceDescription**](ResourceDescription.md) |  | [optional] 
**name** | **str, none_type** | name associated with address | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**phone** | **str, none_type** | Must be no longer than 40 characters. | [optional] 
**email** | **str, none_type** | Must be no longer than 100 characters. | [optional] 
**metadata** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str, none_type** |  | [optional] 
**address_city** | **str** |  | [optional] 
**address_state** | **str** | 2 letter state short-name code | [optional] 
**address_zip** | **str** | Must follow the ZIP format of &#x60;12345&#x60; or ZIP+4 format of &#x60;12345-1234&#x60;.  | [optional] 
**address_country** | [**CountryExtendedExpanded**](CountryExtendedExpanded.md) |  | [optional] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "address"
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | [optional] 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | [optional] 
**deleted** | **bool** | Only returned if the resource has been successfully deleted. | [optional] 
**recipient_moved** | **bool, none_type** | Only returned for accounts on certain &lt;a href&#x3D;\&quot;https://dashboard.lob.com/#/settings/editions\&quot;&gt;Print &amp;amp; Mail Editions&lt;/a&gt;. Value is &#x60;true&#x60; if the address was altered because the recipient filed for a &lt;a href&#x3D;\&quot;#ncoa\&quot;&gt;National Change of Address (NCOA)&lt;/a&gt;, &#x60;false&#x60; if the NCOA check was run but no altered address was found, and &#x60;null&#x60; if the NCOA check was not run. The NCOA check does not happen for non-US addresses, for non-deliverable US addresses, or for addresses created before the NCOA feature was added to your account.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


