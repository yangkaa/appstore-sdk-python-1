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


class V1UserAppListResponse(object):
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
        'apps': 'list[V1AppBaseInfo]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'apps': 'apps',
        'page': 'page',
        'page_size': 'pageSize',
        'total': 'total'
    }

    def __init__(self, apps=None, page=None, page_size=None, total=None, local_vars_configuration=None):  # noqa: E501
        """V1UserAppListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apps = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        self.apps = apps
        self.page = page
        self.page_size = page_size
        self.total = total

    @property
    def apps(self):
        """Gets the apps of this V1UserAppListResponse.  # noqa: E501

        应用列表  # noqa: E501

        :return: The apps of this V1UserAppListResponse.  # noqa: E501
        :rtype: list[V1AppBaseInfo]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this V1UserAppListResponse.

        应用列表  # noqa: E501

        :param apps: The apps of this V1UserAppListResponse.  # noqa: E501
        :type: list[V1AppBaseInfo]
        """
        if self.local_vars_configuration.client_side_validation and apps is None:  # noqa: E501
            raise ValueError("Invalid value for `apps`, must not be `None`")  # noqa: E501

        self._apps = apps

    @property
    def page(self):
        """Gets the page of this V1UserAppListResponse.  # noqa: E501


        :return: The page of this V1UserAppListResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this V1UserAppListResponse.


        :param page: The page of this V1UserAppListResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and page is None:  # noqa: E501
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this V1UserAppListResponse.  # noqa: E501


        :return: The page_size of this V1UserAppListResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this V1UserAppListResponse.


        :param page_size: The page_size of this V1UserAppListResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and page_size is None:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this V1UserAppListResponse.  # noqa: E501


        :return: The total of this V1UserAppListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this V1UserAppListResponse.


        :param total: The total of this V1UserAppListResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, V1UserAppListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1UserAppListResponse):
            return True

        return self.to_dict() != other.to_dict()
