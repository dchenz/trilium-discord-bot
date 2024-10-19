# Login201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | [optional] 

## Example

```python
from trilium_client.models.login201_response import Login201Response

# TODO update the JSON string below
json = "{}"
# create an instance of Login201Response from a JSON string
login201_response_instance = Login201Response.from_json(json)
# print the JSON string representation of the object
print(Login201Response.to_json())

# convert the object into a dict
login201_response_dict = login201_response_instance.to_dict()
# create an instance of Login201Response from a dict
login201_response_from_dict = Login201Response.from_dict(login201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


