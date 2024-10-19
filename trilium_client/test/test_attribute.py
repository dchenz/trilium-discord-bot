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

from trilium_client.models.attribute import Attribute


class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attribute:
        """Test Attribute
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Attribute`
        """
        model = Attribute()
        if include_optional:
            return Attribute(
                attribute_id = 'evnnmvHTCgIn',
                note_id = 'evnnmvHTCgIn',
                type = 'label',
                name = 'shareCss',
                value = '',
                position = 56,
                is_inheritable = True,
                utc_date_modified = '2021-12-31 19:18:11.930Z'
            )
        else:
            return Attribute(
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
