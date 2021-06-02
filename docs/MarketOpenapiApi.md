# openapi_client.MarketOpenapiApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](MarketOpenapiApi.md#create_app) | **POST** /app-server/openapi/apps | create an app model
[**create_app_version**](MarketOpenapiApi.md#create_app_version) | **POST** /app-server/openapi/apps/{appID}/versions | post an app version
[**get_app_hub_info**](MarketOpenapiApi.md#get_app_hub_info) | **GET** /app-server/openapi/apps/{appID}/apphubinfo | get app image save info
[**get_market_info**](MarketOpenapiApi.md#get_market_info) | **GET** /app-server/openapi/info | get mrket info
[**get_orgs**](MarketOpenapiApi.md#get_orgs) | **GET** /app-server/openapi/organizations | 获取组织机构(行业)列表
[**get_user_app_detail**](MarketOpenapiApi.md#get_user_app_detail) | **GET** /app-server/openapi/apps/{appID} | Query the specified application details
[**get_user_app_list**](MarketOpenapiApi.md#get_user_app_list) | **GET** /app-server/openapi/apps | A list of installable applications
[**get_user_app_version_detail**](MarketOpenapiApi.md#get_user_app_version_detail) | **GET** /app-server/openapi/apps/{appID}/versions/{version} | Query the specified version details of the specified application
[**get_user_app_versions**](MarketOpenapiApi.md#get_user_app_versions) | **GET** /app-server/openapi/apps/{appID}/versions | Query the specified application version list
[**update_app**](MarketOpenapiApi.md#update_app) | **PUT** /app-server/openapi/apps/{appID} | update app model base info


# **create_app**
> V1AppDetailInfoResponse create_app(body, market_domain=market_domain)

create an app model

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    body = openapi_client.V1AppModelCreateRequest() # V1AppModelCreateRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # create an app model
        api_response = api_instance.create_app(body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AppModelCreateRequest**](V1AppModelCreateRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Field validation |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_version**
> V1AppVersionBase create_app_version(app_id, body, market_domain=market_domain)

post an app version

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
body = openapi_client.V1CreateAppPaaSVersionRequest() # V1CreateAppPaaSVersionRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # post an app version
        api_response = api_instance.create_app_version(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **body** | [**V1CreateAppPaaSVersionRequest**](V1CreateAppPaaSVersionRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppVersionBase**](V1AppVersionBase.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_hub_info**
> V1AppImageHubInfoResponse get_app_hub_info(app_id, market_domain=market_domain)

get app image save info

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # get app image save info
        api_response = api_instance.get_app_hub_info(app_id, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_app_hub_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppImageHubInfoResponse**](V1AppImageHubInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_info**
> V1MarketInfoResponse get_market_info(market_domain=market_domain)

get mrket info

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # get mrket info
        api_response = api_instance.get_market_info(market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_market_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1MarketInfoResponse**](V1MarketInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orgs**
> list[V1Organization] get_orgs()

获取组织机构(行业)列表

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    
    try:
        # 获取组织机构(行业)列表
        api_response = api_instance.get_orgs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_orgs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1Organization]**](V1Organization.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_detail**
> V1AppDetailInfoResponse get_user_app_detail(app_id, market_domain)

Query the specified application details

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
market_domain = 'market_domain_example' # str | the market domain

    try:
        # Query the specified application details
        api_response = api_instance.get_user_app_detail(app_id, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **market_domain** | **str**| the market domain | 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_list**
> V1UserAppListResponse get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)

A list of installable applications

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | the market domain
query = 'query_example' # str | The search criteria (optional)
query_all = True # bool | true (optional)
page = 56 # int | query page num (optional)
page_size = 56 # int | query page size, if -1 return all app (optional)

    try:
        # A list of installable applications
        api_response = api_instance.get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| the market domain | 
 **query** | **str**| The search criteria | [optional] 
 **query_all** | **bool**| true | [optional] 
 **page** | **int**| query page num | [optional] 
 **page_size** | **int**| query page size, if -1 return all app | [optional] 

### Return type

[**V1UserAppListResponse**](V1UserAppListResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | market not found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_version_detail**
> V1AppVersionDetailResponse get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)

Query the specified version details of the specified application

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
version = 'version_example' # str | The app version
market_domain = 'market_domain_example' # str | the market domain (optional)
for_install = True # bool | Whether used for installation (optional)
get_template = True # bool | Whether get templete (optional)

    try:
        # Query the specified version details of the specified application
        api_response = api_instance.get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_version_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **version** | **str**| The app version | 
 **market_domain** | **str**| the market domain | [optional] 
 **for_install** | **bool**| Whether used for installation | [optional] 
 **get_template** | **bool**| Whether get templete | [optional] 

### Return type

[**V1AppVersionDetailResponse**](V1AppVersionDetailResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_versions**
> V1AppVersionListResponse get_user_app_versions(app_id, query_all, market_domain)

Query the specified application version list

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
query_all = True # bool | query all versions, must have write perm
market_domain = 'market_domain_example' # str | the market domain

    try:
        # Query the specified application version list
        api_response = api_instance.get_user_app_versions(app_id, query_all, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **query_all** | **bool**| query all versions, must have write perm | 
 **market_domain** | **str**| the market domain | 

### Return type

[**V1AppVersionListResponse**](V1AppVersionListResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> V1AppDetailInfoResponse update_app(app_id, body, market_domain=market_domain)

update app model base info

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
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
body = openapi_client.V1AppUpdateRequest() # V1AppUpdateRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # update app model base info
        api_response = api_instance.update_app(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **body** | [**V1AppUpdateRequest**](V1AppUpdateRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

