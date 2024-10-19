# AppInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_version** | **str** | Trilium version | [optional] 
**db_version** | **int** | DB version | [optional] 
**sync_version** | **int** | Sync protocol version | [optional] 
**build_date** | **datetime** | build date | [optional] 
**build_revision** | **str** | git build revision | [optional] 
**data_directory** | **str** | data directory where Trilium stores files | [optional] 
**clipper_protocol_version** | **str** | version of the supported Trilium Web Clipper protocol | [optional] 
**utc_date_time** | **str** | current UTC date time | [optional] 

## Example

```python
from trilium_client.models.app_info import AppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfo from a JSON string
app_info_instance = AppInfo.from_json(json)
# print the JSON string representation of the object
print(AppInfo.to_json())

# convert the object into a dict
app_info_dict = app_info_instance.to_dict()
# create an instance of AppInfo from a dict
app_info_from_dict = AppInfo.from_dict(app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


