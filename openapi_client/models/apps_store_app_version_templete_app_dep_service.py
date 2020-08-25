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


class AppsStoreAppVersionTempleteAppDepService(object):
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
        'dep_service_key': 'str'
    }

    attribute_map = {
        'dep_service_key': 'dep_service_key'
    }

    def __init__(self, dep_service_key=None, local_vars_configuration=None):  # noqa: E501
        """AppsStoreAppVersionTempleteAppDepService - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dep_service_key = None
        self.discriminator = None

        self.dep_service_key = dep_service_key

    @property
    def dep_service_key(self):
        """Gets the dep_service_key of this AppsStoreAppVersionTempleteAppDepService.  # noqa: E501


        :return: The dep_service_key of this AppsStoreAppVersionTempleteAppDepService.  # noqa: E501
        :rtype: str
        """
        return self._dep_service_key

    @dep_service_key.setter
    def dep_service_key(self, dep_service_key):
        """Sets the dep_service_key of this AppsStoreAppVersionTempleteAppDepService.


        :param dep_service_key: The dep_service_key of this AppsStoreAppVersionTempleteAppDepService.  # noqa: E501
        :type dep_service_key: str
        """
        if self.local_vars_configuration.client_side_validation and dep_service_key is None:  # noqa: E501
            raise ValueError("Invalid value for `dep_service_key`, must not be `None`")  # noqa: E501

        self._dep_service_key = dep_service_key

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
        if not isinstance(other, AppsStoreAppVersionTempleteAppDepService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppsStoreAppVersionTempleteAppDepService):
            return True

        return self.to_dict() != other.to_dict()
