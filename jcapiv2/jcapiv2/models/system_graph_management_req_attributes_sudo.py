# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SystemGraphManagementReqAttributesSudo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'without_password': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'without_password': 'withoutPassword'
    }

    def __init__(self, enabled=None, without_password=None):
        """
        SystemGraphManagementReqAttributesSudo - a model defined in Swagger
        """

        self._enabled = None
        self._without_password = None

        if enabled is not None:
          self.enabled = enabled
        if without_password is not None:
          self.without_password = without_password

    @property
    def enabled(self):
        """
        Gets the enabled of this SystemGraphManagementReqAttributesSudo.

        :return: The enabled of this SystemGraphManagementReqAttributesSudo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SystemGraphManagementReqAttributesSudo.

        :param enabled: The enabled of this SystemGraphManagementReqAttributesSudo.
        :type: bool
        """

        self._enabled = enabled

    @property
    def without_password(self):
        """
        Gets the without_password of this SystemGraphManagementReqAttributesSudo.

        :return: The without_password of this SystemGraphManagementReqAttributesSudo.
        :rtype: bool
        """
        return self._without_password

    @without_password.setter
    def without_password(self, without_password):
        """
        Sets the without_password of this SystemGraphManagementReqAttributesSudo.

        :param without_password: The without_password of this SystemGraphManagementReqAttributesSudo.
        :type: bool
        """

        self._without_password = without_password

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SystemGraphManagementReqAttributesSudo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
