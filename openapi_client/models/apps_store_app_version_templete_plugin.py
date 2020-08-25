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


class AppsStoreAppVersionTempletePlugin(object):
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
        'id': 'int',
        'build_source': 'str',
        'build_version': 'str',
        'category': 'str',
        'code_repo': 'str',
        'config_groups': 'list[AppsStoreAppVersionTempletePluginConfigGroup]',
        'create_time': 'str',
        'desc': 'str',
        'image': 'str',
        'origin': 'str',
        'origin_share_id': 'str',
        'plugin_alias': 'str',
        'plugin_id': 'str',
        'plugin_image': 'AppsImageInfo',
        'plugin_key': 'str',
        'plugin_name': 'str',
        'share_image': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'build_source': 'build_source',
        'build_version': 'build_version',
        'category': 'category',
        'code_repo': 'code_repo',
        'config_groups': 'config_groups',
        'create_time': 'create_time',
        'desc': 'desc',
        'image': 'image',
        'origin': 'origin',
        'origin_share_id': 'origin_share_id',
        'plugin_alias': 'plugin_alias',
        'plugin_id': 'plugin_id',
        'plugin_image': 'plugin_image',
        'plugin_key': 'plugin_key',
        'plugin_name': 'plugin_name',
        'share_image': 'share_image'
    }

    def __init__(self, id=None, build_source=None, build_version=None, category=None, code_repo=None, config_groups=None, create_time=None, desc=None, image=None, origin=None, origin_share_id=None, plugin_alias=None, plugin_id=None, plugin_image=None, plugin_key=None, plugin_name=None, share_image=None, local_vars_configuration=None):  # noqa: E501
        """AppsStoreAppVersionTempletePlugin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._build_source = None
        self._build_version = None
        self._category = None
        self._code_repo = None
        self._config_groups = None
        self._create_time = None
        self._desc = None
        self._image = None
        self._origin = None
        self._origin_share_id = None
        self._plugin_alias = None
        self._plugin_id = None
        self._plugin_image = None
        self._plugin_key = None
        self._plugin_name = None
        self._share_image = None
        self.discriminator = None

        self.id = id
        self.build_source = build_source
        self.build_version = build_version
        self.category = category
        self.code_repo = code_repo
        if config_groups is not None:
            self.config_groups = config_groups
        self.create_time = create_time
        self.desc = desc
        self.image = image
        self.origin = origin
        self.origin_share_id = origin_share_id
        self.plugin_alias = plugin_alias
        self.plugin_id = plugin_id
        self.plugin_image = plugin_image
        self.plugin_key = plugin_key
        self.plugin_name = plugin_name
        self.share_image = share_image

    @property
    def id(self):
        """Gets the id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppsStoreAppVersionTempletePlugin.


        :param id: The id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def build_source(self):
        """Gets the build_source of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The build_source of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._build_source

    @build_source.setter
    def build_source(self, build_source):
        """Sets the build_source of this AppsStoreAppVersionTempletePlugin.


        :param build_source: The build_source of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type build_source: str
        """
        if self.local_vars_configuration.client_side_validation and build_source is None:  # noqa: E501
            raise ValueError("Invalid value for `build_source`, must not be `None`")  # noqa: E501

        self._build_source = build_source

    @property
    def build_version(self):
        """Gets the build_version of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The build_version of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this AppsStoreAppVersionTempletePlugin.


        :param build_version: The build_version of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type build_version: str
        """
        if self.local_vars_configuration.client_side_validation and build_version is None:  # noqa: E501
            raise ValueError("Invalid value for `build_version`, must not be `None`")  # noqa: E501

        self._build_version = build_version

    @property
    def category(self):
        """Gets the category of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The category of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AppsStoreAppVersionTempletePlugin.


        :param category: The category of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type category: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def code_repo(self):
        """Gets the code_repo of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The code_repo of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._code_repo

    @code_repo.setter
    def code_repo(self, code_repo):
        """Sets the code_repo of this AppsStoreAppVersionTempletePlugin.


        :param code_repo: The code_repo of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type code_repo: str
        """
        if self.local_vars_configuration.client_side_validation and code_repo is None:  # noqa: E501
            raise ValueError("Invalid value for `code_repo`, must not be `None`")  # noqa: E501

        self._code_repo = code_repo

    @property
    def config_groups(self):
        """Gets the config_groups of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The config_groups of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: list[AppsStoreAppVersionTempletePluginConfigGroup]
        """
        return self._config_groups

    @config_groups.setter
    def config_groups(self, config_groups):
        """Sets the config_groups of this AppsStoreAppVersionTempletePlugin.


        :param config_groups: The config_groups of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type config_groups: list[AppsStoreAppVersionTempletePluginConfigGroup]
        """

        self._config_groups = config_groups

    @property
    def create_time(self):
        """Gets the create_time of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The create_time of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AppsStoreAppVersionTempletePlugin.


        :param create_time: The create_time of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type create_time: str
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def desc(self):
        """Gets the desc of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The desc of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AppsStoreAppVersionTempletePlugin.


        :param desc: The desc of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type desc: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def image(self):
        """Gets the image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AppsStoreAppVersionTempletePlugin.


        :param image: The image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type image: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def origin(self):
        """Gets the origin of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The origin of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AppsStoreAppVersionTempletePlugin.


        :param origin: The origin of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type origin: str
        """
        if self.local_vars_configuration.client_side_validation and origin is None:  # noqa: E501
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501

        self._origin = origin

    @property
    def origin_share_id(self):
        """Gets the origin_share_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The origin_share_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._origin_share_id

    @origin_share_id.setter
    def origin_share_id(self, origin_share_id):
        """Sets the origin_share_id of this AppsStoreAppVersionTempletePlugin.


        :param origin_share_id: The origin_share_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type origin_share_id: str
        """
        if self.local_vars_configuration.client_side_validation and origin_share_id is None:  # noqa: E501
            raise ValueError("Invalid value for `origin_share_id`, must not be `None`")  # noqa: E501

        self._origin_share_id = origin_share_id

    @property
    def plugin_alias(self):
        """Gets the plugin_alias of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The plugin_alias of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._plugin_alias

    @plugin_alias.setter
    def plugin_alias(self, plugin_alias):
        """Sets the plugin_alias of this AppsStoreAppVersionTempletePlugin.


        :param plugin_alias: The plugin_alias of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type plugin_alias: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_alias`, must not be `None`")  # noqa: E501

        self._plugin_alias = plugin_alias

    @property
    def plugin_id(self):
        """Gets the plugin_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The plugin_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this AppsStoreAppVersionTempletePlugin.


        :param plugin_id: The plugin_id of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type plugin_id: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def plugin_image(self):
        """Gets the plugin_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The plugin_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: AppsImageInfo
        """
        return self._plugin_image

    @plugin_image.setter
    def plugin_image(self, plugin_image):
        """Sets the plugin_image of this AppsStoreAppVersionTempletePlugin.


        :param plugin_image: The plugin_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type plugin_image: AppsImageInfo
        """
        if self.local_vars_configuration.client_side_validation and plugin_image is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_image`, must not be `None`")  # noqa: E501

        self._plugin_image = plugin_image

    @property
    def plugin_key(self):
        """Gets the plugin_key of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The plugin_key of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._plugin_key

    @plugin_key.setter
    def plugin_key(self, plugin_key):
        """Sets the plugin_key of this AppsStoreAppVersionTempletePlugin.


        :param plugin_key: The plugin_key of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type plugin_key: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_key is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_key`, must not be `None`")  # noqa: E501

        self._plugin_key = plugin_key

    @property
    def plugin_name(self):
        """Gets the plugin_name of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The plugin_name of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this AppsStoreAppVersionTempletePlugin.


        :param plugin_name: The plugin_name of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type plugin_name: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_name is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_name`, must not be `None`")  # noqa: E501

        self._plugin_name = plugin_name

    @property
    def share_image(self):
        """Gets the share_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501


        :return: The share_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :rtype: str
        """
        return self._share_image

    @share_image.setter
    def share_image(self, share_image):
        """Sets the share_image of this AppsStoreAppVersionTempletePlugin.


        :param share_image: The share_image of this AppsStoreAppVersionTempletePlugin.  # noqa: E501
        :type share_image: str
        """
        if self.local_vars_configuration.client_side_validation and share_image is None:  # noqa: E501
            raise ValueError("Invalid value for `share_image`, must not be `None`")  # noqa: E501

        self._share_image = share_image

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
        if not isinstance(other, AppsStoreAppVersionTempletePlugin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppsStoreAppVersionTempletePlugin):
            return True

        return self.to_dict() != other.to_dict()
