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
            One.name,
            One.one
        )
        .limit(5)
    )

    result = query.run(as_dict=True)

    # Task 3 - Document API
    if result:
        doc = frappe.get_doc("one", result[0]["name"])
        doc.one = result[0]["one"]   # Update the field
        doc.save()

    return result