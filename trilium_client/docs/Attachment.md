# Attachment

Attachment is owned by a note, has title and content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**mime** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**blob_id** | **str** | ID of the blob object which effectively serves as a content hash | [optional] 
**date_modified** | **str** |  | [optional] 
**utc_date_modified** | **str** |  | [optional] 
**utc_date_scheduled_for_erasure_since** | **str** |  | [optional] 
**content_length** | **int** |  | [optional] 

## Example

```python
from trilium_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


