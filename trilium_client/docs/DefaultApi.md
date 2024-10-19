# trilium_client.DefaultApi

All URIs are relative to *http://localhost:37740/etapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](DefaultApi.md#create_backup) | **PUT** /backup/{backupName} | 
[**create_note**](DefaultApi.md#create_note) | **POST** /create-note | 
[**create_revision**](DefaultApi.md#create_revision) | **POST** /notes/{noteId}/revision | 
[**delete_attachment_by_id**](DefaultApi.md#delete_attachment_by_id) | **DELETE** /attachments/{attachmentId} | 
[**delete_attribute_by_id**](DefaultApi.md#delete_attribute_by_id) | **DELETE** /attributes/{attributeId} | 
[**delete_branch_by_id**](DefaultApi.md#delete_branch_by_id) | **DELETE** /branches/{branchId} | 
[**delete_note_by_id**](DefaultApi.md#delete_note_by_id) | **DELETE** /notes/{noteId} | 
[**export_note_subtree**](DefaultApi.md#export_note_subtree) | **GET** /notes/{noteId}/export | 
[**get_app_info**](DefaultApi.md#get_app_info) | **GET** /app-info | 
[**get_attachment_by_id**](DefaultApi.md#get_attachment_by_id) | **GET** /attachments/{attachmentId} | 
[**get_attachment_content**](DefaultApi.md#get_attachment_content) | **GET** /attachments/{attachmentId}/content | 
[**get_attribute_by_id**](DefaultApi.md#get_attribute_by_id) | **GET** /attributes/{attributeId} | 
[**get_branch_by_id**](DefaultApi.md#get_branch_by_id) | **GET** /branches/{branchId} | 
[**get_day_note**](DefaultApi.md#get_day_note) | **GET** /calendar/days/{date} | 
[**get_inbox_note**](DefaultApi.md#get_inbox_note) | **GET** /inbox/{date} | 
[**get_month_note**](DefaultApi.md#get_month_note) | **GET** /calendar/months/{month} | 
[**get_note_by_id**](DefaultApi.md#get_note_by_id) | **GET** /notes/{noteId} | 
[**get_note_content**](DefaultApi.md#get_note_content) | **GET** /notes/{noteId}/content | 
[**get_week_note**](DefaultApi.md#get_week_note) | **GET** /calendar/weeks/{date} | 
[**get_year_note**](DefaultApi.md#get_year_note) | **GET** /calendar/years/{year} | 
[**import_zip**](DefaultApi.md#import_zip) | **POST** /notes/{noteId}/import | 
[**login**](DefaultApi.md#login) | **POST** /auth/login | 
[**logout**](DefaultApi.md#logout) | **POST** /auth/logout | 
[**patch_attachment_by_id**](DefaultApi.md#patch_attachment_by_id) | **PATCH** /attachments/{attachmentId} | 
[**patch_attribute_by_id**](DefaultApi.md#patch_attribute_by_id) | **PATCH** /attributes/{attributeId} | 
[**patch_branch_by_id**](DefaultApi.md#patch_branch_by_id) | **PATCH** /branches/{branchId} | 
[**patch_note_by_id**](DefaultApi.md#patch_note_by_id) | **PATCH** /notes/{noteId} | 
[**post_attachment**](DefaultApi.md#post_attachment) | **POST** /attachments | 
[**post_attribute**](DefaultApi.md#post_attribute) | **POST** /attributes | 
[**post_branch**](DefaultApi.md#post_branch) | **POST** /branches | 
[**post_refresh_note_ordering**](DefaultApi.md#post_refresh_note_ordering) | **POST** /refresh-note-ordering/{parentNoteId} | 
[**put_attachment_content_by_id**](DefaultApi.md#put_attachment_content_by_id) | **PUT** /attachments/{attachmentId}/content | 
[**put_note_content_by_id**](DefaultApi.md#put_note_content_by_id) | **PUT** /notes/{noteId}/content | 
[**search_notes**](DefaultApi.md#search_notes) | **GET** /notes | 


# **create_backup**
> create_backup(backup_name)



Create a database backup under a given name

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    backup_name = 'backup_name_example' # str | If the backupName is e.g. \"now\", then the backup will be written to \"backup-now.db\" file

    try:
        api_instance.create_backup(backup_name)
    except Exception as e:
        print("Exception when calling DefaultApi->create_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_name** | **str**| If the backupName is e.g. \&quot;now\&quot;, then the backup will be written to \&quot;backup-now.db\&quot; file | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | backup has been created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note**
> NoteWithBranch create_note(create_note_def)



Create a note and place it into the note tree

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.create_note_def import CreateNoteDef
from trilium_client.models.note_with_branch import NoteWithBranch
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    create_note_def = trilium_client.CreateNoteDef() # CreateNoteDef | 

    try:
        api_response = api_instance.create_note(create_note_def)
        print("The response of DefaultApi->create_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_note_def** | [**CreateNoteDef**](CreateNoteDef.md)|  | 

### Return type

[**NoteWithBranch**](NoteWithBranch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | note created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_revision**
> create_revision(note_id, format=format)



Create a note revision for the given note

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 
    format = html # str |  (optional) (default to html)

    try:
        api_instance.create_revision(note_id, format=format)
    except Exception as e:
        print("Exception when calling DefaultApi->create_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to html]

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | revision has been created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment_by_id**
> delete_attachment_by_id(attachment_id)



deletes an attachment based on the attachmentId supplied.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        api_instance.delete_attachment_by_id(attachment_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | attachment deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_by_id**
> delete_attribute_by_id(attribute_id)



deletes an attribute based on the attributeId supplied.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attribute_id = 'attribute_id_example' # str | 

    try:
        api_instance.delete_attribute_by_id(attribute_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | attribute deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_branch_by_id**
> delete_branch_by_id(branch_id)



deletes a branch based on the branchId supplied. If this is the last branch of the (child) note,  then the note is deleted as well. 

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    branch_id = 'branch_id_example' # str | 

    try:
        api_instance.delete_branch_by_id(branch_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_branch_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | branch deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note_by_id**
> delete_note_by_id(note_id)



deletes a single note based on the noteId supplied

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        api_instance.delete_note_by_id(note_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | note deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_note_subtree**
> bytearray export_note_subtree(note_id, format=format)



Exports ZIP file export of a given note subtree. To export whole document, use \"root\" for noteId

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 
    format = html # str |  (optional) (default to html)

    try:
        api_response = api_instance.export_note_subtree(note_id, format=format)
        print("The response of DefaultApi->export_note_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->export_note_subtree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to html]

### Return type

**bytearray**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | export ZIP file |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_info**
> AppInfo get_app_info()



returns information about the running Trilium instance

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.app_info import AppInfo
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_app_info()
        print("The response of DefaultApi->get_app_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_app_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppInfo**](AppInfo.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | app info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_by_id**
> Attachment get_attachment_by_id(attachment_id)



Returns an attachment identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        api_response = api_instance.get_attachment_by_id(attachment_id)
        print("The response of DefaultApi->get_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachment response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_content**
> str get_attachment_content(attachment_id)



Returns attachment content identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attachment_id = 'attachment_id_example' # str | 

    try:
        api_response = api_instance.get_attachment_content(attachment_id)
        print("The response of DefaultApi->get_attachment_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_attachment_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 

### Return type

**str**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachment content response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_by_id**
> Attribute get_attribute_by_id(attribute_id)



Returns an attribute identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attribute_id = 'attribute_id_example' # str | 

    try:
        api_response = api_instance.get_attribute_by_id(attribute_id)
        print("The response of DefaultApi->get_attribute_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attribute response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_by_id**
> Branch get_branch_by_id(branch_id)



Returns a branch identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.branch import Branch
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    branch_id = 'branch_id_example' # str | 

    try:
        api_response = api_instance.get_branch_by_id(branch_id)
        print("The response of DefaultApi->get_branch_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_branch_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**|  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | branch response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_note**
> Note get_day_note(var_date)



returns a day note for a given date. Gets created if doesn't exist.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    var_date = '2022-02-22' # date | 

    try:
        api_response = api_instance.get_day_note(var_date)
        print("The response of DefaultApi->get_day_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_day_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | day note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_note**
> Note get_inbox_note(var_date)



returns an \"inbox\" note, into which note can be created. Date will be used depending on whether the inbox is a fixed note (identified with #inbox label) or a day note in a journal. 

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    var_date = '2022-02-22' # date | 

    try:
        api_response = api_instance.get_inbox_note(var_date)
        print("The response of DefaultApi->get_inbox_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_inbox_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inbox note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_note**
> Note get_month_note(month)



returns a week note for a given date. Gets created if doesn't exist.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    month = '2022-02' # str | 

    try:
        api_response = api_instance.get_month_note(month)
        print("The response of DefaultApi->get_month_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_month_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | month note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_by_id**
> Note get_note_by_id(note_id)



Returns a note identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        api_response = api_instance.get_note_by_id(note_id)
        print("The response of DefaultApi->get_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_content**
> str get_note_content(note_id)



Returns note content identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        api_response = api_instance.get_note_content(note_id)
        print("The response of DefaultApi->get_note_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_note_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

**str**

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note content response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_week_note**
> Note get_week_note(var_date)



returns a week note for a given date. Gets created if doesn't exist.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    var_date = '2022-02-22' # date | 

    try:
        api_response = api_instance.get_week_note(var_date)
        print("The response of DefaultApi->get_week_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_week_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | week note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_year_note**
> Note get_year_note(year)



returns a week note for a given date. Gets created if doesn't exist.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    year = '2022-02' # str | 

    try:
        api_response = api_instance.get_year_note(year)
        print("The response of DefaultApi->get_year_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_year_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | year note |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_zip**
> NoteWithBranch import_zip(note_id)



Imports ZIP file into a given note.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note_with_branch import NoteWithBranch
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 

    try:
        api_response = api_instance.import_zip(note_id)
        print("The response of DefaultApi->import_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->import_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 

### Return type

[**NoteWithBranch**](NoteWithBranch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | note created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Login201Response login(login_request)



get an ETAPI token based on password for further use with ETAPI

### Example


```python
import trilium_client
from trilium_client.models.login201_response import Login201Response
from trilium_client.models.login_request import LoginRequest
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)


# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    login_request = trilium_client.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.login(login_request)
        print("The response of DefaultApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Login201Response**](Login201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | auth token |  -  |
**429** | Client IP has been blacklisted because too many requests (possibly failed authentications) were made within a short time frame, try again later |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()



logout (delete/deactivate) an ETAPI token

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)

    try:
        api_instance.logout()
    except Exception as e:
        print("Exception when calling DefaultApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | logout successful |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attachment_by_id**
> Attachment patch_attachment_by_id(attachment_id, attachment)



patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title, and position are patchable.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attachment_id = 'attachment_id_example' # str | 
    attachment = trilium_client.Attachment() # Attachment | 

    try:
        api_response = api_instance.patch_attachment_by_id(attachment_id, attachment)
        print("The response of DefaultApi->patch_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 
 **attachment** | [**Attachment**](Attachment.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attribute updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attribute_by_id**
> Attribute patch_attribute_by_id(attribute_id, attribute)



patch an attribute identified by the attributeId with changes in the body. For labels, only value and position can be updated. For relations, only position can be updated. If you want to modify other properties, you need to delete the old attribute and create a new one.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attribute_id = 'attribute_id_example' # str | 
    attribute = trilium_client.Attribute() # Attribute | 

    try:
        api_response = api_instance.patch_attribute_by_id(attribute_id, attribute)
        print("The response of DefaultApi->patch_attribute_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**|  | 
 **attribute** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attribute updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_branch_by_id**
> Branch patch_branch_by_id(branch_id, branch)



patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can be updated. If you want to update other properties, you need to delete the old branch and create a new one.

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.branch import Branch
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    branch_id = 'branch_id_example' # str | 
    branch = trilium_client.Branch() # Branch | 

    try:
        api_response = api_instance.patch_branch_by_id(branch_id, branch)
        print("The response of DefaultApi->patch_branch_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_branch_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**|  | 
 **branch** | [**Branch**](Branch.md)|  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | branch updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_note_by_id**
> Note patch_note_by_id(note_id, note)



patch a note identified by the noteId with changes in the body

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.note import Note
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 
    note = trilium_client.Note() # Note | 

    try:
        api_response = api_instance.patch_note_by_id(note_id, note)
        print("The response of DefaultApi->patch_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **note** | [**Note**](Note.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note updated |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachment**
> Attachment post_attachment(create_attachment)



create an attachment

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attachment import Attachment
from trilium_client.models.create_attachment import CreateAttachment
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    create_attachment = trilium_client.CreateAttachment() # CreateAttachment | 

    try:
        api_response = api_instance.post_attachment(create_attachment)
        print("The response of DefaultApi->post_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_attachment** | [**CreateAttachment**](CreateAttachment.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attachment created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attribute**
> Attribute post_attribute(attribute)



create an attribute for a given note

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.attribute import Attribute
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attribute = trilium_client.Attribute() # Attribute | 

    try:
        api_response = api_instance.post_attribute(attribute)
        print("The response of DefaultApi->post_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attribute created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_branch**
> Branch post_branch(branch)



Create a branch (clone a note to a different location in the tree). In case there is a branch between parent note and child note already,  then this will update the existing branch with prefix, notePosition and isExpanded. 

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.branch import Branch
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    branch = trilium_client.Branch() # Branch | 

    try:
        api_response = api_instance.post_branch(branch)
        print("The response of DefaultApi->post_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | [**Branch**](Branch.md)|  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | branch updated (branch between parent note and child note already existed) |  -  |
**201** | branch created |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_refresh_note_ordering**
> post_refresh_note_ordering(parent_note_id)



notePositions in branches are not automatically pushed to connected clients and need a specific instruction.  If you want your changes to be in effect immediately, call this service after setting branches' notePosition.  Note that you need to supply \"parentNoteId\" of branch(es) with changed positions. 

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    parent_note_id = 'parent_note_id_example' # str | 

    try:
        api_instance.post_refresh_note_ordering(parent_note_id)
    except Exception as e:
        print("Exception when calling DefaultApi->post_refresh_note_ordering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_note_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | note ordering will be asynchronously updated in all connected clients |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attachment_content_by_id**
> put_attachment_content_by_id(attachment_id, body)



Updates attachment content identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    attachment_id = 'attachment_id_example' # str | 
    body = 'body_example' # str | html content of attachment

    try:
        api_instance.put_attachment_content_by_id(attachment_id, body)
    except Exception as e:
        print("Exception when calling DefaultApi->put_attachment_content_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  | 
 **body** | **str**| html content of attachment | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | attachment content updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_note_content_by_id**
> put_note_content_by_id(note_id, body)



Updates note content identified by its ID

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    note_id = 'note_id_example' # str | 
    body = 'body_example' # str | html content of note

    try:
        api_instance.put_note_content_by_id(note_id, body)
    except Exception as e:
        print("Exception when calling DefaultApi->put_note_content_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | 
 **body** | **str**| html content of note | 

### Return type

void (empty response body)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | note content updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notes**
> SearchResponse search_notes(search, fast_search=fast_search, include_archived_notes=include_archived_notes, ancestor_note_id=ancestor_note_id, ancestor_depth=ancestor_depth, order_by=order_by, order_direction=order_direction, limit=limit, debug=debug)



Search notes

### Example

* Api Key Authentication (EtapiTokenAuth):
* Basic Authentication (EtapiBasicAuth):

```python
import trilium_client
from trilium_client.models.search_response import SearchResponse
from trilium_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:37740/etapi
# See configuration.py for a list of all supported configuration parameters.
configuration = trilium_client.Configuration(
    host = "http://localhost:37740/etapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: EtapiTokenAuth
configuration.api_key['EtapiTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EtapiTokenAuth'] = 'Bearer'

# Configure HTTP basic authorization: EtapiBasicAuth
configuration = trilium_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with trilium_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trilium_client.DefaultApi(api_client)
    search = 'towers tolkien' # str | search query string as described in https://triliumnext.github.io/Docs/Wiki/search.html
    fast_search = False # bool | enable fast search (fulltext doesn't look into content) (optional) (default to False)
    include_archived_notes = False # bool | search by default ignores archived notes. Set to 'true' to includes archived notes into search results. (optional) (default to False)
    ancestor_note_id = 'ancestor_note_id_example' # str | search only in a subtree identified by the subtree noteId. By default whole tree is searched. (optional)
    ancestor_depth = 'eq1' # str | define how deep in the tree should the notes be searched (optional)
    order_by = '[\"title\",\"#publicationDate\",\"isProtected\",\"isArchived\",\"dateCreated\",\"dateModified\",\"utcDateCreated\",\"utcDateModified\",\"parentCount\",\"childrenCount\",\"attributeCount\",\"labelCount\",\"ownedLabelCount\",\"relationCount\",\"ownedRelationCount\",\"relationCountIncludingLinks\",\"ownedRelationCountIncludingLinks\",\"targetRelationCount\",\"targetRelationCountIncludingLinks\",\"contentSize\",\"contentAndAttachmentsSize\",\"contentAndAttachmentsAndRevisionsSize\",\"revisionCount\"]' # str | name of the property/label to order search results by (optional)
    order_direction = asc # str | order direction, ascending or descending (optional) (default to asc)
    limit = 10 # int | limit the number of results you want to receive (optional)
    debug = False # bool | set to true to get debug information in the response (search query parsing) (optional) (default to False)

    try:
        api_response = api_instance.search_notes(search, fast_search=fast_search, include_archived_notes=include_archived_notes, ancestor_note_id=ancestor_note_id, ancestor_depth=ancestor_depth, order_by=order_by, order_direction=order_direction, limit=limit, debug=debug)
        print("The response of DefaultApi->search_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search query string as described in https://triliumnext.github.io/Docs/Wiki/search.html | 
 **fast_search** | **bool**| enable fast search (fulltext doesn&#39;t look into content) | [optional] [default to False]
 **include_archived_notes** | **bool**| search by default ignores archived notes. Set to &#39;true&#39; to includes archived notes into search results. | [optional] [default to False]
 **ancestor_note_id** | **str**| search only in a subtree identified by the subtree noteId. By default whole tree is searched. | [optional] 
 **ancestor_depth** | **str**| define how deep in the tree should the notes be searched | [optional] 
 **order_by** | **str**| name of the property/label to order search results by | [optional] 
 **order_direction** | **str**| order direction, ascending or descending | [optional] [default to asc]
 **limit** | **int**| limit the number of results you want to receive | [optional] 
 **debug** | **bool**| set to true to get debug information in the response (search query parsing) | [optional] [default to False]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[EtapiTokenAuth](../README.md#EtapiTokenAuth), [EtapiBasicAuth](../README.md#EtapiBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

