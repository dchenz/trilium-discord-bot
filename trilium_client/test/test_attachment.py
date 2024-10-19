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

from trilium_client.models.attachment import Attachment

class TestAttachment(unittest.TestCase):
    """Attachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attachment:
        """Test Attachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attachment`
        """
        model = Attachment()
        if include_optional:
            return Attachment(
                attachment_id = 'evnnmvHTCgIn',
                owner_id = 'evnnmvHTCgIn',
                role = '',
                mime = '',
                title = '',
                position = 56,
                blob_id = '',
                date_modified = '2021-12-31 20:18:11.930+0100',
                utc_date_modified = '2021-12-31 19:18:11.930Z',
                utc_date_scheduled_for_erasure_since = '2021-12-31 19:18:11.930Z',
                content_length = 56
            )
        else:
            return Attachment(
        )
        """

    def testAttachment(self):
        """Test Attachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
