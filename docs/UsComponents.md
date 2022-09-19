# UsComponents

A nested object containing a breakdown of each component of an address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_number** | **str** | The numeric or alphanumeric part of an address preceding the street name. Often the house, building, or PO Box number. | 
**street_predirection** | **str** | Geographic direction preceding a street name (&#x60;N&#x60;, &#x60;S&#x60;, &#x60;E&#x60;, &#x60;W&#x60;, &#x60;NE&#x60;, &#x60;SW&#x60;, &#x60;SE&#x60;, &#x60;NW&#x60;).  | 
**street_name** | **str** | The name of the street. | 
**street_suffix** | **str** | The standard USPS abbreviation for the street suffix (&#x60;ST&#x60;, &#x60;AVE&#x60;, &#x60;BLVD&#x60;, etc).  | 
**street_postdirection** | **str** | Geographic direction following a street name (&#x60;N&#x60;, &#x60;S&#x60;, &#x60;E&#x60;, &#x60;W&#x60;, &#x60;NE&#x60;, &#x60;SW&#x60;, &#x60;SE&#x60;, &#x60;NW&#x60;).  | 
**secondary_designator** | **str** | The standard USPS abbreviation describing the &#x60;components[secondary_number]&#x60; (&#x60;STE&#x60;, &#x60;APT&#x60;, &#x60;BLDG&#x60;, etc).  | 
**secondary_number** | **str** | Number of the apartment/unit/etc.  | 
**pmb_designator** | **str** | Designator of a [CMRA-authorized](https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency) private mailbox.  | 
**pmb_number** | **str** | Number of a [CMRA-authorized](https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency) private mailbox.  | 
**extra_secondary_designator** | **str** | An extra (often unnecessary) secondary designator provided with the input address.  | 
**extra_secondary_number** | **str** | An extra (often unnecessary) secondary number provided with the input address.  | 
**city** | [**City**](City.md) |  | 
**state** | [**State**](State.md) |  | 
**zip_code** | **str** | The 5-digit ZIP code | 
**zip_code_plus_4** | [**ZipCodePlus4**](ZipCodePlus4.md) |  | 
**zip_code_type** | [**ZipCodeType**](ZipCodeType.md) |  | 
**delivery_point_barcode** | **str** | A 12-digit identifier that uniquely identifies a delivery point (location where mail can be sent and received). It consists of the 5-digit ZIP code (&#x60;zip_code&#x60;), 4-digit ZIP+4 add-on (&#x60;zip_code_plus_4&#x60;), 2-digit delivery point, and 1-digit delivery point check digit.  | 
**address_type** | **str** | Uses USPS&#39;s [Residential Delivery Indicator (RDI)](https://www.usps.com/nationalpremieraccounts/rdi.htm) to identify whether an address is classified as residential or business. Possible values are: * &#x60;residential&#x60; –– The address is residential or a PO Box. * &#x60;commercial&#x60; –– The address is commercial. * &#x60;&#39;&#39;&#x60; –– Not enough information provided to be determined.  | 
**record_type** | **str** | A description of the type of address. Populated if a DPV match is made (&#x60;deliverability_analysis[dpv_confirmation]&#x60; is &#x60;Y&#x60;, &#x60;S&#x60;, or &#x60;D&#x60;). For more detailed information about each record type, see [US Verification Details](#tag/US-Verification-Types).  | 
**default_building_address** | **bool** | Designates whether or not the address is the default address for a building containing multiple delivery points.  | 
**county** | **str** | County name of the address city. | 
**county_fips** | **str** | A 5-digit [FIPS county code](https://en.wikipedia.org/wiki/FIPS_county_code) which uniquely identifies &#x60;components[county]&#x60;. It consists of a 2-digit state code and a 3-digit county code.  | 
**carrier_route** | **str** | A 4-character code assigned to a mail delivery route within a ZIP code.  | 
**carrier_route_type** | **str** | The type of &#x60;components[carrier_route]&#x60;. For more detailed information about each carrier route type, see [US Verification Details](#tag/US-Verification-Types).  | 
**latitude** | **float, none_type** | A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be used with &#x60;longitude&#x60; to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is &#x60;AA&#x60;, &#x60;AE&#x60;, or &#x60;AP&#x60;).  | [optional] 
**longitude** | **float, none_type** | A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be used with &#x60;latitude&#x60; to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is &#x60;AA&#x60;, &#x60;AE&#x60;, or &#x60;AP&#x60;).  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


