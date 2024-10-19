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

from trilium_client.models.create_attachment import CreateAttachment


class TestCreateAttachment(unittest.TestCase):
    """CreateAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAttachment:
        """Test CreateAttachment
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateAttachment`
        """
        model = CreateAttachment()
        if include_optional:
            return CreateAttachment(
                owner_id = 'evnnmvHTCgIn',
                role = '',
                mime = '',
                title = '',
                content = '',
                position = 56
            )
        else:
            return CreateAttachment(
        )
        """

    def testCreateAttachment(self):
        """Test CreateAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
