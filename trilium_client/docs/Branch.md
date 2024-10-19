# Branch

Branch places the note into the tree, it represents the relationship between a parent note and child note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** |  | [optional] 
**note_id** | **str** |  | [optional] 
**parent_note_id** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**note_position** | **int** |  | [optional] 
**is_expanded** | **bool** |  | [optional] 
**utc_date_modified** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


