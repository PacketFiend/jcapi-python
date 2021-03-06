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


class GraphObjectWithPaths(object):
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
        'type': 'GraphType',
        'id': 'str',
        'paths': 'list[list[GraphConnection]]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'paths': 'paths'
    }

    def __init__(self, type=None, id=None, paths=None):
        """
        GraphObjectWithPaths - a model defined in Swagger
        """

        self._type = None
        self._id = None
        self._paths = None

        self.type = type
        self.id = id
        self.paths = paths

    @property
    def type(self):
        """
        Gets the type of this GraphObjectWithPaths.

        :return: The type of this GraphObjectWithPaths.
        :rtype: GraphType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GraphObjectWithPaths.

        :param type: The type of this GraphObjectWithPaths.
        :type: GraphType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this GraphObjectWithPaths.
        Object ID of this graph object.

        :return: The id of this GraphObjectWithPaths.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GraphObjectWithPaths.
        Object ID of this graph object.

        :param id: The id of this GraphObjectWithPaths.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def paths(self):
        """
        Gets the paths of this GraphObjectWithPaths.
        A path through the graph between two graph objects.

        :return: The paths of this GraphObjectWithPaths.
        :rtype: list[list[GraphConnection]]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this GraphObjectWithPaths.
        A path through the graph between two graph objects.

        :param paths: The paths of this GraphObjectWithPaths.
        :type: list[list[GraphConnection]]
        """
        if paths is None:
            raise ValueError("Invalid value for `paths`, must not be `None`")

        self._paths = paths

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
        if not isinstance(other, GraphObjectWithPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
