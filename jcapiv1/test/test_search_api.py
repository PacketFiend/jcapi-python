# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv1
from jcapiv1.rest import ApiException
from jcapiv1.apis.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """ SearchApi unit test stubs """

    def setUp(self):
        self.api = jcapiv1.apis.search_api.SearchApi()

    def tearDown(self):
        pass

    def test_search_systems_post(self):
        """
        Test case for search_systems_post

        Search Systems
        """
        pass

    def test_search_systemusers_post(self):
        """
        Test case for search_systemusers_post

        Search System Users
        """
        pass


if __name__ == '__main__':
    unittest.main()
