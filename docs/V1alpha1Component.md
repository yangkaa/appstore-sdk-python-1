# V1alpha1Component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**cmd** | **str** |  | 
**component_monitor** | [**list[V1alpha1ComponentMonitor]**](V1alpha1ComponentMonitor.md) |  | 
**cpu** | **int** |  | 
**dep_service_map_list** | [**list[V1alpha1ComponentDep]**](V1alpha1ComponentDep.md) |  | 
**deploy_version** | **str** |  | 
**extend_method** | **str** |  | 
**extend_method_map** | [**V1alpha1ComponentExtendMethodRule**](V1alpha1ComponentExtendMethodRule.md) |  | 
**image** | **str** |  | 
**language** | **str** |  | 
**memory** | **int** |  | 
**mnt_relation_list** | [**list[V1alpha1ComponentShareVolume]**](V1alpha1ComponentShareVolume.md) |  | 
**port_map_list** | [**list[V1alpha1ComponentPort]**](V1alpha1ComponentPort.md) |  | 
**probes** | [**list[V1alpha1ComponentProbe]**](V1alpha1ComponentProbe.md) |  | 
**service_alias** | **str** |  | 
**service_cname** | **str** |  | 
**service_connect_info_map_list** | [**list[V1alpha1ComponentEnv]**](V1alpha1ComponentEnv.md) |  | 
**service_env_map_list** | [**list[V1alpha1ComponentEnv]**](V1alpha1ComponentEnv.md) |  | 
**service_id** | **str** |  | 
**service_image** | [**V1alpha1ImageInfo**](V1alpha1ImageInfo.md) |  | 
**service_key** | **str** |  | 
**service_name** | **str** |  | 
**service_related_plugin_config** | [**list[V1alpha1ComponentPluginConfig]**](V1alpha1ComponentPluginConfig.md) |  | [optional] 
**service_share_uuid** | **str** |  | [optional] 
**service_source** | **str** |  | 
**service_type** | **str** |  | 
**service_volume_map_list** | [**list[V1alpha1ComponentVolume]**](V1alpha1ComponentVolume.md) |  | 
**share_image** | **str** |  | 
**share_type** | **str** |  | [optional] 
**version** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


