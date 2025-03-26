# UploadState

The `state` property on the `upload` object. As the file is processed, the `state` will change from `Ready for Validation` to `Validating` and then will be either `Scheduled` (successfully processed) or `Errored` (Unsuccessfully processed).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The &#x60;state&#x60; property on the &#x60;upload&#x60; object. As the file is processed, the &#x60;state&#x60; will change from &#x60;Ready for Validation&#x60; to &#x60;Validating&#x60; and then will be either &#x60;Scheduled&#x60; (successfully processed) or &#x60;Errored&#x60; (Unsuccessfully processed). | defaults to "Draft",  must be one of ["Preprocessing", "Draft", "Ready for Validation", "Validating", "Scheduled", "Cancelled", "Errored", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


