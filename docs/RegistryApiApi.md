# openapi_client.RegistryApiApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_auth**](RegistryApiApi.md#do_auth) | **GET** /app-server/v1/registry/auth | image registry auth server


# **do_auth**
> ControllerResult do_auth(account=account, service=service, scope=scope)

image registry auth server

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RegistryApiApi(api_client)
    account = 'account_example' # str | registry acount (optional)
service = 'service_example' # str | registry service (optional)
scope = 'scope_example' # str | registry scope (optional)

    try:
        # image registry auth server
        api_response = api_instance.do_auth(account=account, service=service, scope=scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistryApiApi->do_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| registry acount | [optional] 
 **service** | **str**| registry service | [optional] 
 **scope** | **str**| registry scope | [optional] 

### Return type

[**ControllerResult**](ControllerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | no auth |  -  |
**403** | auth failure |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

