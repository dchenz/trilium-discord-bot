# CreateAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**mime** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from trilium_client.models.create_attachment import CreateAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttachment from a JSON string
create_attachment_instance = CreateAttachment.from_json(json)
# print the JSON string representation of the object
print(CreateAttachment.to_json())

# convert the object into a dict
create_attachment_dict = create_attachment_instance.to_dict()
# create an instance of CreateAttachment from a dict
create_attachment_from_dict = CreateAttachment.from_dict(create_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


