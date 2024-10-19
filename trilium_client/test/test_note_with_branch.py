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

from trilium_client.models.note_with_branch import NoteWithBranch


class TestNoteWithBranch(unittest.TestCase):
    """NoteWithBranch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NoteWithBranch:
        """Test NoteWithBranch
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NoteWithBranch`
        """
        model = NoteWithBranch()
        if include_optional:
            return NoteWithBranch(
                note = trilium_client.models.note.Note(
                    note_id = 'evnnmvHTCgIn', 
                    title = '', 
                    type = 'text', 
                    mime = '', 
                    is_protected = True, 
                    blob_id = '', 
                    attributes = [
                        trilium_client.models.attribute.Attribute(
                            attribute_id = 'evnnmvHTCgIn', 
                            note_id = 'evnnmvHTCgIn', 
                            type = 'label', 
                            name = 'shareCss', 
                            value = '', 
                            position = 56, 
                            is_inheritable = True, 
                            utc_date_modified = '2021-12-31 19:18:11.930Z', )
                        ], 
                    parent_note_ids = [
                        'evnnmvHTCgIn'
                        ], 
                    child_note_ids = [
                        'evnnmvHTCgIn'
                        ], 
                    parent_branch_ids = , 
                    child_branch_ids = , 
                    date_created = '2021-12-31 20:18:11.930+0100', 
                    date_modified = '2021-12-31 20:18:11.930+0100', 
                    utc_date_created = '2021-12-31 19:18:11.930Z', 
                    utc_date_modified = '2021-12-31 19:18:11.930Z', ),
                branch = trilium_client.models.branch.Branch(
                    branch_id = 'evnnmvHTCgIn', 
                    note_id = 'evnnmvHTCgIn', 
                    parent_note_id = 'evnnmvHTCgIn', 
                    prefix = '', 
                    note_position = 56, 
                    is_expanded = True, 
                    utc_date_modified = '2021-12-31 19:18:11.930Z', )
            )
        else:
            return NoteWithBranch(
        )
        """

    def testNoteWithBranch(self):
        """Test NoteWithBranch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
