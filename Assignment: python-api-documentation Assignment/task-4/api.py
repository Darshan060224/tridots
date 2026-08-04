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

    if result:
        names = [row["name"] for row in result]
        frappe.db.set_value("one", names, "one", "Updated via Bulk Database API")

    return result