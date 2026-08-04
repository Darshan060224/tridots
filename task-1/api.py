import frappe

@frappe.whitelist()
def assignment_demo():
    return "Hello"