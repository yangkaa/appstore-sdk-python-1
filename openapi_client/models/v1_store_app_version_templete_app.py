# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1StoreAppVersionTempleteApp(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'category': 'str',
        'cmd': 'str',
        'dep_service_map_list': 'list[V1StoreAppVersionTempleteAppDepService]',
        'deploy_version': 'str',
        'extend_method': 'str',
        'extend_method_map': 'V1StoreAppVersionTempleteAppExtendMethodRule',
        'image': 'str',
        'language': 'str',
        'memory': 'int',
        'mnt_relation_list': 'list[V1StoreAppVersionTempleteAppShareVolume]',
        'port_map_list': 'list[V1StoreAppVersionTempleteAppPort]',
        'probes': 'list[V1StoreAppVersionTempleteAppProbe]',
        'service_alias': 'str',
        'service_cname': 'str',
        'service_connect_info_map_list': 'list[V1StoreAppVersionTempleteAppEnv]',
        'service_env_map_list': 'list[V1StoreAppVersionTempleteAppEnv]',
        'service_id': 'str',
        'service_image': 'V1ImageInfo',
        'service_key': 'str',
        'service_name': 'str',
        'service_region': 'str',
        'service_related_plugin_config': 'list[V1StoreAppVersionTempleteAppPluginConfig]',
        'service_share_uuid': 'str',
        'service_source': 'str',
        'service_type': 'str',
        'service_volume_map_list': 'list[V1StoreAppVersionTempleteAppVolume]',
        'share_image': 'str',
        'share_type': 'str',
        'tenant_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'category': 'category',
        'cmd': 'cmd',
        'dep_service_map_list': 'dep_service_map_list',
        'deploy_version': 'deploy_version',
        'extend_method': 'extend_method',
        'extend_method_map': 'extend_method_map',
        'image': 'image',
        'language': 'language',
        'memory': 'memory',
        'mnt_relation_list': 'mnt_relation_list',
        'port_map_list': 'port_map_list',
        'probes': 'probes',
        'service_alias': 'service_alias',
        'service_cname': 'service_cname',
        'service_connect_info_map_list': 'service_connect_info_map_list',
        'service_env_map_list': 'service_env_map_list',
        'service_id': 'service_id',
        'service_image': 'service_image',
        'service_key': 'service_key',
        'service_name': 'service_name',
        'service_region': 'service_region',
        'service_related_plugin_config': 'service_related_plugin_config',
        'service_share_uuid': 'service_share_uuid',
        'service_source': 'service_source',
        'service_type': 'service_type',
        'service_volume_map_list': 'service_volume_map_list',
        'share_image': 'share_image',
        'share_type': 'share_type',
        'tenant_id': 'tenant_id',
        'version': 'version'
    }

    def __init__(self, category=None, cmd=None, dep_service_map_list=None, deploy_version=None, extend_method=None, extend_method_map=None, image=None, language=None, memory=None, mnt_relation_list=None, port_map_list=None, probes=None, service_alias=None, service_cname=None, service_connect_info_map_list=None, service_env_map_list=None, service_id=None, service_image=None, service_key=None, service_name=None, service_region=None, service_related_plugin_config=None, service_share_uuid=None, service_source=None, service_type=None, service_volume_map_list=None, share_image=None, share_type=None, tenant_id=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1StoreAppVersionTempleteApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category = None
        self._cmd = None
        self._dep_service_map_list = None
        self._deploy_version = None
        self._extend_method = None
        self._extend_method_map = None
        self._image = None
        self._language = None
        self._memory = None
        self._mnt_relation_list = None
        self._port_map_list = None
        self._probes = None
        self._service_alias = None
        self._service_cname = None
        self._service_connect_info_map_list = None
        self._service_env_map_list = None
        self._service_id = None
        self._service_image = None
        self._service_key = None
        self._service_name = None
        self._service_region = None
        self._service_related_plugin_config = None
        self._service_share_uuid = None
        self._service_source = None
        self._service_type = None
        self._service_volume_map_list = None
        self._share_image = None
        self._share_type = None
        self._tenant_id = None
        self._version = None
        self.discriminator = None

        self.category = category
        self.cmd = cmd
        self.dep_service_map_list = dep_service_map_list
        self.deploy_version = deploy_version
        self.extend_method = extend_method
        self.extend_method_map = extend_method_map
        self.image = image
        self.language = language
        self.memory = memory
        self.mnt_relation_list = mnt_relation_list
        self.port_map_list = port_map_list
        self.probes = probes
        self.service_alias = service_alias
        self.service_cname = service_cname
        self.service_connect_info_map_list = service_connect_info_map_list
        self.service_env_map_list = service_env_map_list
        self.service_id = service_id
        self.service_image = service_image
        self.service_key = service_key
        self.service_name = service_name
        self.service_region = service_region
        if service_related_plugin_config is not None:
            self.service_related_plugin_config = service_related_plugin_config
        if service_share_uuid is not None:
            self.service_share_uuid = service_share_uuid
        self.service_source = service_source
        self.service_type = service_type
        self.service_volume_map_list = service_volume_map_list
        self.share_image = share_image
        if share_type is not None:
            self.share_type = share_type
        self.tenant_id = tenant_id
        self.version = version

    @property
    def category(self):
        """Gets the category of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The category of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this V1StoreAppVersionTempleteApp.


        :param category: The category of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type category: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def cmd(self):
        """Gets the cmd of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The cmd of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this V1StoreAppVersionTempleteApp.


        :param cmd: The cmd of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type cmd: str
        """
        if self.local_vars_configuration.client_side_validation and cmd is None:  # noqa: E501
            raise ValueError("Invalid value for `cmd`, must not be `None`")  # noqa: E501

        self._cmd = cmd

    @property
    def dep_service_map_list(self):
        """Gets the dep_service_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The dep_service_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppDepService]
        """
        return self._dep_service_map_list

    @dep_service_map_list.setter
    def dep_service_map_list(self, dep_service_map_list):
        """Sets the dep_service_map_list of this V1StoreAppVersionTempleteApp.


        :param dep_service_map_list: The dep_service_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type dep_service_map_list: list[V1StoreAppVersionTempleteAppDepService]
        """
        if self.local_vars_configuration.client_side_validation and dep_service_map_list is None:  # noqa: E501
            raise ValueError("Invalid value for `dep_service_map_list`, must not be `None`")  # noqa: E501

        self._dep_service_map_list = dep_service_map_list

    @property
    def deploy_version(self):
        """Gets the deploy_version of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The deploy_version of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._deploy_version

    @deploy_version.setter
    def deploy_version(self, deploy_version):
        """Sets the deploy_version of this V1StoreAppVersionTempleteApp.


        :param deploy_version: The deploy_version of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type deploy_version: str
        """
        if self.local_vars_configuration.client_side_validation and deploy_version is None:  # noqa: E501
            raise ValueError("Invalid value for `deploy_version`, must not be `None`")  # noqa: E501

        self._deploy_version = deploy_version

    @property
    def extend_method(self):
        """Gets the extend_method of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The extend_method of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._extend_method

    @extend_method.setter
    def extend_method(self, extend_method):
        """Sets the extend_method of this V1StoreAppVersionTempleteApp.


        :param extend_method: The extend_method of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type extend_method: str
        """
        if self.local_vars_configuration.client_side_validation and extend_method is None:  # noqa: E501
            raise ValueError("Invalid value for `extend_method`, must not be `None`")  # noqa: E501

        self._extend_method = extend_method

    @property
    def extend_method_map(self):
        """Gets the extend_method_map of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The extend_method_map of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: V1StoreAppVersionTempleteAppExtendMethodRule
        """
        return self._extend_method_map

    @extend_method_map.setter
    def extend_method_map(self, extend_method_map):
        """Sets the extend_method_map of this V1StoreAppVersionTempleteApp.


        :param extend_method_map: The extend_method_map of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type extend_method_map: V1StoreAppVersionTempleteAppExtendMethodRule
        """
        if self.local_vars_configuration.client_side_validation and extend_method_map is None:  # noqa: E501
            raise ValueError("Invalid value for `extend_method_map`, must not be `None`")  # noqa: E501

        self._extend_method_map = extend_method_map

    @property
    def image(self):
        """Gets the image of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1StoreAppVersionTempleteApp.


        :param image: The image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type image: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def language(self):
        """Gets the language of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The language of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V1StoreAppVersionTempleteApp.


        :param language: The language of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def memory(self):
        """Gets the memory of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The memory of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this V1StoreAppVersionTempleteApp.


        :param memory: The memory of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type memory: int
        """
        if self.local_vars_configuration.client_side_validation and memory is None:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def mnt_relation_list(self):
        """Gets the mnt_relation_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The mnt_relation_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppShareVolume]
        """
        return self._mnt_relation_list

    @mnt_relation_list.setter
    def mnt_relation_list(self, mnt_relation_list):
        """Sets the mnt_relation_list of this V1StoreAppVersionTempleteApp.


        :param mnt_relation_list: The mnt_relation_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type mnt_relation_list: list[V1StoreAppVersionTempleteAppShareVolume]
        """
        if self.local_vars_configuration.client_side_validation and mnt_relation_list is None:  # noqa: E501
            raise ValueError("Invalid value for `mnt_relation_list`, must not be `None`")  # noqa: E501

        self._mnt_relation_list = mnt_relation_list

    @property
    def port_map_list(self):
        """Gets the port_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The port_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppPort]
        """
        return self._port_map_list

    @port_map_list.setter
    def port_map_list(self, port_map_list):
        """Sets the port_map_list of this V1StoreAppVersionTempleteApp.


        :param port_map_list: The port_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type port_map_list: list[V1StoreAppVersionTempleteAppPort]
        """
        if self.local_vars_configuration.client_side_validation and port_map_list is None:  # noqa: E501
            raise ValueError("Invalid value for `port_map_list`, must not be `None`")  # noqa: E501

        self._port_map_list = port_map_list

    @property
    def probes(self):
        """Gets the probes of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The probes of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppProbe]
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        """Sets the probes of this V1StoreAppVersionTempleteApp.


        :param probes: The probes of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type probes: list[V1StoreAppVersionTempleteAppProbe]
        """
        if self.local_vars_configuration.client_side_validation and probes is None:  # noqa: E501
            raise ValueError("Invalid value for `probes`, must not be `None`")  # noqa: E501

        self._probes = probes

    @property
    def service_alias(self):
        """Gets the service_alias of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_alias of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_alias

    @service_alias.setter
    def service_alias(self, service_alias):
        """Sets the service_alias of this V1StoreAppVersionTempleteApp.


        :param service_alias: The service_alias of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_alias: str
        """
        if self.local_vars_configuration.client_side_validation and service_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `service_alias`, must not be `None`")  # noqa: E501

        self._service_alias = service_alias

    @property
    def service_cname(self):
        """Gets the service_cname of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_cname of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_cname

    @service_cname.setter
    def service_cname(self, service_cname):
        """Sets the service_cname of this V1StoreAppVersionTempleteApp.


        :param service_cname: The service_cname of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_cname: str
        """
        if self.local_vars_configuration.client_side_validation and service_cname is None:  # noqa: E501
            raise ValueError("Invalid value for `service_cname`, must not be `None`")  # noqa: E501

        self._service_cname = service_cname

    @property
    def service_connect_info_map_list(self):
        """Gets the service_connect_info_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_connect_info_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppEnv]
        """
        return self._service_connect_info_map_list

    @service_connect_info_map_list.setter
    def service_connect_info_map_list(self, service_connect_info_map_list):
        """Sets the service_connect_info_map_list of this V1StoreAppVersionTempleteApp.


        :param service_connect_info_map_list: The service_connect_info_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_connect_info_map_list: list[V1StoreAppVersionTempleteAppEnv]
        """
        if self.local_vars_configuration.client_side_validation and service_connect_info_map_list is None:  # noqa: E501
            raise ValueError("Invalid value for `service_connect_info_map_list`, must not be `None`")  # noqa: E501

        self._service_connect_info_map_list = service_connect_info_map_list

    @property
    def service_env_map_list(self):
        """Gets the service_env_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_env_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppEnv]
        """
        return self._service_env_map_list

    @service_env_map_list.setter
    def service_env_map_list(self, service_env_map_list):
        """Sets the service_env_map_list of this V1StoreAppVersionTempleteApp.


        :param service_env_map_list: The service_env_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_env_map_list: list[V1StoreAppVersionTempleteAppEnv]
        """
        if self.local_vars_configuration.client_side_validation and service_env_map_list is None:  # noqa: E501
            raise ValueError("Invalid value for `service_env_map_list`, must not be `None`")  # noqa: E501

        self._service_env_map_list = service_env_map_list

    @property
    def service_id(self):
        """Gets the service_id of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_id of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this V1StoreAppVersionTempleteApp.


        :param service_id: The service_id of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_id: str
        """
        if self.local_vars_configuration.client_side_validation and service_id is None:  # noqa: E501
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def service_image(self):
        """Gets the service_image of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: V1ImageInfo
        """
        return self._service_image

    @service_image.setter
    def service_image(self, service_image):
        """Sets the service_image of this V1StoreAppVersionTempleteApp.


        :param service_image: The service_image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_image: V1ImageInfo
        """
        if self.local_vars_configuration.client_side_validation and service_image is None:  # noqa: E501
            raise ValueError("Invalid value for `service_image`, must not be `None`")  # noqa: E501

        self._service_image = service_image

    @property
    def service_key(self):
        """Gets the service_key of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_key of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_key

    @service_key.setter
    def service_key(self, service_key):
        """Sets the service_key of this V1StoreAppVersionTempleteApp.


        :param service_key: The service_key of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_key: str
        """
        if self.local_vars_configuration.client_side_validation and service_key is None:  # noqa: E501
            raise ValueError("Invalid value for `service_key`, must not be `None`")  # noqa: E501

        self._service_key = service_key

    @property
    def service_name(self):
        """Gets the service_name of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_name of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this V1StoreAppVersionTempleteApp.


        :param service_name: The service_name of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_name: str
        """
        if self.local_vars_configuration.client_side_validation and service_name is None:  # noqa: E501
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def service_region(self):
        """Gets the service_region of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_region of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_region

    @service_region.setter
    def service_region(self, service_region):
        """Sets the service_region of this V1StoreAppVersionTempleteApp.


        :param service_region: The service_region of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_region: str
        """
        if self.local_vars_configuration.client_side_validation and service_region is None:  # noqa: E501
            raise ValueError("Invalid value for `service_region`, must not be `None`")  # noqa: E501

        self._service_region = service_region

    @property
    def service_related_plugin_config(self):
        """Gets the service_related_plugin_config of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_related_plugin_config of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppPluginConfig]
        """
        return self._service_related_plugin_config

    @service_related_plugin_config.setter
    def service_related_plugin_config(self, service_related_plugin_config):
        """Sets the service_related_plugin_config of this V1StoreAppVersionTempleteApp.


        :param service_related_plugin_config: The service_related_plugin_config of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_related_plugin_config: list[V1StoreAppVersionTempleteAppPluginConfig]
        """

        self._service_related_plugin_config = service_related_plugin_config

    @property
    def service_share_uuid(self):
        """Gets the service_share_uuid of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_share_uuid of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_share_uuid

    @service_share_uuid.setter
    def service_share_uuid(self, service_share_uuid):
        """Sets the service_share_uuid of this V1StoreAppVersionTempleteApp.


        :param service_share_uuid: The service_share_uuid of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_share_uuid: str
        """

        self._service_share_uuid = service_share_uuid

    @property
    def service_source(self):
        """Gets the service_source of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_source of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_source

    @service_source.setter
    def service_source(self, service_source):
        """Sets the service_source of this V1StoreAppVersionTempleteApp.


        :param service_source: The service_source of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_source: str
        """
        if self.local_vars_configuration.client_side_validation and service_source is None:  # noqa: E501
            raise ValueError("Invalid value for `service_source`, must not be `None`")  # noqa: E501

        self._service_source = service_source

    @property
    def service_type(self):
        """Gets the service_type of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_type of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this V1StoreAppVersionTempleteApp.


        :param service_type: The service_type of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_type: str
        """
        if self.local_vars_configuration.client_side_validation and service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501

        self._service_type = service_type

    @property
    def service_volume_map_list(self):
        """Gets the service_volume_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The service_volume_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: list[V1StoreAppVersionTempleteAppVolume]
        """
        return self._service_volume_map_list

    @service_volume_map_list.setter
    def service_volume_map_list(self, service_volume_map_list):
        """Sets the service_volume_map_list of this V1StoreAppVersionTempleteApp.


        :param service_volume_map_list: The service_volume_map_list of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type service_volume_map_list: list[V1StoreAppVersionTempleteAppVolume]
        """
        if self.local_vars_configuration.client_side_validation and service_volume_map_list is None:  # noqa: E501
            raise ValueError("Invalid value for `service_volume_map_list`, must not be `None`")  # noqa: E501

        self._service_volume_map_list = service_volume_map_list

    @property
    def share_image(self):
        """Gets the share_image of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The share_image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._share_image

    @share_image.setter
    def share_image(self, share_image):
        """Sets the share_image of this V1StoreAppVersionTempleteApp.


        :param share_image: The share_image of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type share_image: str
        """
        if self.local_vars_configuration.client_side_validation and share_image is None:  # noqa: E501
            raise ValueError("Invalid value for `share_image`, must not be `None`")  # noqa: E501

        self._share_image = share_image

    @property
    def share_type(self):
        """Gets the share_type of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The share_type of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this V1StoreAppVersionTempleteApp.


        :param share_type: The share_type of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type share_type: str
        """

        self._share_type = share_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The tenant_id of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this V1StoreAppVersionTempleteApp.


        :param tenant_id: The tenant_id of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type tenant_id: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def version(self):
        """Gets the version of this V1StoreAppVersionTempleteApp.  # noqa: E501


        :return: The version of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1StoreAppVersionTempleteApp.


        :param version: The version of this V1StoreAppVersionTempleteApp.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1StoreAppVersionTempleteApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1StoreAppVersionTempleteApp):
            return True

        return self.to_dict() != other.to_dict()
