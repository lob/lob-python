# LobConfidenceScore

Lob Confidence Score is a nested object that provides a numerical value between 0-100 of the likelihood that an address is deliverable based on Lob’s mail delivery data to over half of US households.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float, none_type** | A numerical score between 0 and 100 that represents the percentage of mailpieces Lob has sent to this addresses that have been delivered successfully over the past 2 years. Will be &#x60;null&#x60; if no tracking data exists for this address.  | [optional] 
**level** | **str** | indicates the likelihood that the address is a valid, mail-receiving address. Possible values are:   - &#x60;high&#x60; — Over 70% of mailpieces Lob has sent to this address were delivered successfully and recent mailings were also successful.   - &#x60;medium&#x60; — Between 40% and 70% of mailpieces Lob has sent to this address were delivered successfully.   - &#x60;low&#x60; — Less than 40% of mailpieces Lob has sent to this address were delivered successfully and recent mailings weren&#39;t successful.   - &#x60;\&quot;\&quot;&#x60; — No tracking data exists for this address or lob deliverability was unable to find a corresponding level of mail success.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


