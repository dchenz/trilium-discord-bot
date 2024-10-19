# NoteWithBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | [**Note**](Note.md) |  | [optional] 
**branch** | [**Branch**](Branch.md) |  | [optional] 

## Example

```python
from trilium_client.models.note_with_branch import NoteWithBranch

# TODO update the JSON string below
json = "{}"
# create an instance of NoteWithBranch from a JSON string
note_with_branch_instance = NoteWithBranch.from_json(json)
# print the JSON string representation of the object
print(NoteWithBranch.to_json())

# convert the object into a dict
note_with_branch_dict = note_with_branch_instance.to_dict()
# create an instance of NoteWithBranch from a dict
note_with_branch_from_dict = NoteWithBranch.from_dict(note_with_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


