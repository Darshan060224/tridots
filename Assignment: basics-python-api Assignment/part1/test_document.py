# Copyright (c) 2026, Darshan and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class TestDocument(Document):
    def before_save(self):
        if not self.description:
            self.description = "Default Description"


test_document = TestDocument