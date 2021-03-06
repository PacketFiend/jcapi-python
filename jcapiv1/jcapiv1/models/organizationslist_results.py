# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrganizationslistResults(object):
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
        'id': 'str',
        'display_name': 'str',
        'logo_url': 'str'
    }

    attribute_map = {
        'id': '_id',
        'display_name': 'displayName',
        'logo_url': 'logoUrl'
    }

    def __init__(self, id=None, display_name=None, logo_url=None):
        """
        OrganizationslistResults - a model defined in Swagger
        """

        self._id = None
        self._display_name = None
        self._logo_url = None

        if id is not None:
          self.id = id
        if display_name is not None:
          self.display_name = display_name
        if logo_url is not None:
          self.logo_url = logo_url

    @property
    def id(self):
        """
        Gets the id of this OrganizationslistResults.
        the ID of the organization.

        :return: The id of this OrganizationslistResults.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrganizationslistResults.
        the ID of the organization.

        :param id: The id of this OrganizationslistResults.
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this OrganizationslistResults.
        The name of the organization.

        :return: The display_name of this OrganizationslistResults.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OrganizationslistResults.
        The name of the organization.

        :param display_name: The display_name of this OrganizationslistResults.
        :type: str
        """

        self._display_name = display_name

    @property
    def logo_url(self):
        """
        Gets the logo_url of this OrganizationslistResults.
        The organization logo image URL. 

        :return: The logo_url of this OrganizationslistResults.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this OrganizationslistResults.
        The organization logo image URL. 

        :param logo_url: The logo_url of this OrganizationslistResults.
        :type: str
        """

        self._logo_url = logo_url

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
        if not isinstance(other, OrganizationslistResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
