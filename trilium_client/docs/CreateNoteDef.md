# CreateNoteDef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_note_id** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**mime** | **str** | this needs to be specified only for note types &#39;code&#39;, &#39;file&#39;, &#39;image&#39;. | [optional] 
**content** | **str** |  | 
**note_position** | **int** | Position of the note in the parent. Normal ordering is 10, 20, 30 ...  So if you want to create a note on the first position, use e.g. 5, for second position 15, for last e.g. 1000000  | [optional] 
**prefix** | **str** | Prefix is branch (placement) specific title prefix for the note.  Let&#39;s say you have your note placed into two different places in the tree,  but you want to change the title a bit in one of the placements. For this you can use prefix.  | [optional] 
**is_expanded** | **bool** | true if this note (as a folder) should appear expanded | [optional] 
**note_id** | **str** |  | [optional] 
**branch_id** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**utc_date_created** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.create_note_def import CreateNoteDef

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNoteDef from a JSON string
create_note_def_instance = CreateNoteDef.from_json(json)
# print the JSON string representation of the object
print(CreateNoteDef.to_json())

# convert the object into a dict
create_note_def_dict = create_note_def_instance.to_dict()
# create an instance of CreateNoteDef from a dict
create_note_def_from_dict = CreateNoteDef.from_dict(create_note_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


