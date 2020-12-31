# openapi_client.PlatformOpenApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_healthz**](PlatformOpenApi.md#check_healthz) | **GET** /app-server/openapi/healthz | 检查应用市场的是否运行中


# **check_healthz**
> RestfulutilResult check_healthz()

检查应用市场的是否运行中

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PlatformOpenApi(api_client)
    
    try:
        # 检查应用市场的是否运行中
        api_response = api_instance.check_healthz()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlatformOpenApi->check_healthz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestfulutilResult**](RestfulutilResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

