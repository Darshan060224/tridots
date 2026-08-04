import frappe

@frappe.whitelist()
def assignment_demo():

    One = frappe.qb.DocType("one")
    Two = frappe.qb.DocType("two")

    query = (
        frappe.qb
        .from_(One)
        .join(Two)
        .on(One.name == Two.one)   
        .select(
            One.name
        )
    )

    result = query.run(as_dict=True)

    return result