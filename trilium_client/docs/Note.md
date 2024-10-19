# Note


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**mime** | **str** |  | [optional] 
**is_protected** | **bool** |  | [optional] [readonly] 
**blob_id** | **str** | ID of the blob object which effectively serves as a content hash | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) |  | [optional] 
**parent_note_ids** | **List[str]** |  | [optional] 
**child_note_ids** | **List[str]** |  | [optional] 
**parent_branch_ids** | **List[str]** |  | [optional] 
**child_branch_ids** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**utc_date_created** | **str** |  | [optional] 
**utc_date_modified** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


