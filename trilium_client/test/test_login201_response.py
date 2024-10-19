# coding: utf-8

"""
ETAPI

External Trilium API

The version of the OpenAPI document: 1.0.0
Contact: zadam.apps@gmail.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from trilium_client.models.login201_response import Login201Response


class TestLogin201Response(unittest.TestCase):
    """Login201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Login201Response:
        """Test Login201Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Login201Response`
        """
        model = Login201Response()
        if include_optional:
            return Login201Response(
                auth_token = 'Bc4bFn0Ffiok_4NpbVCDnFz7B2WU+pdhW8B5Ne3DiR5wXrEyqdjgRIsk='
            )
        else:
            return Login201Response(
        )
        """

    def testLogin201Response(self):
        """Test Login201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
