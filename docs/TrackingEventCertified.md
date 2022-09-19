# TrackingEventCertified


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tracking event for Certified letters. Letters sent with USPS Certified Mail are fully tracked by USPS, therefore their tracking events have an additional details object with more detailed information about the tracking event. Some certified tracking event names have multiple meanings, noted in the list here. See the description of the details object for the full set of combined certified tracking event name meanings.    * &#x60;Mailed&#x60; - Package has been accepted into the carrier network for delivery.    * &#x60;In Transit&#x60; - Maps to four distinct stages of transit.    * &#x60;In Local Area&#x60; - Package is at a location near the end destination.    * &#x60;Processed for Delivery&#x60; - Maps to two distinct stages of delivery.    * &#x60;Pickup Available&#x60; - Package is available for pickup at carrier location.    * &#x60;Delivered&#x60; - Package has been delivered.    * &#x60;Re-Routed&#x60; - Package has been forwarded.    * &#x60;Returned to Sender&#x60; - Package is to be returned to sender.    * &#x60;Issue&#x60; - Maps to (at least) 15 possible issues, some of which are actionable.  | 
**id** | [**EvntId**](EvntId.md) |  | 
**date_created** | **datetime** | A timestamp in ISO 8601 format of the date the resource was created. | 
**date_modified** | **datetime** | A timestamp in ISO 8601 format of the date the resource was last modified. | 
**type** | **str** | a Certified letter tracking event | defaults to "certified"
**object** | **str** |  | defaults to "tracking_event"
**details** | [**TrackingEventDetails**](TrackingEventDetails.md) |  | [optional] 
**location** | **str, none_type** | The zip code in which the event occurred if it exists, otherwise will be the name of a Regional Distribution Center if it exists, otherwise will be null.  | [optional] 
**time** | **datetime** | A timestamp in ISO 8601 format of the date USPS registered the event. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


