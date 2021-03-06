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


class GraphConnection(object):
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
        '_from': 'GraphObject',
        'to': 'GraphObject'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, _from=None, to=None):
        """
        GraphConnection - a model defined in Swagger
        """

        self.__from = None
        self._to = None

        if _from is not None:
          self._from = _from
        self.to = to

    @property
    def _from(self):
        """
        Gets the _from of this GraphConnection.

        :return: The _from of this GraphConnection.
        :rtype: GraphObject
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this GraphConnection.

        :param _from: The _from of this GraphConnection.
        :type: GraphObject
        """

        self.__from = _from

    @property
    def to(self):
        """
        Gets the to of this GraphConnection.

        :return: The to of this GraphConnection.
        :rtype: GraphObject
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this GraphConnection.

        :param to: The to of this GraphConnection.
        :type: GraphObject
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

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
        if not isinstance(other, GraphConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
