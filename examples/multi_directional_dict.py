#
# multi_directional_dict.py
#
# Demo of using a littletable Table like a bidirectional or multidirectional dict
# (given multiple unique keys per content object)

import littletable as lt

employees = lt.csv_import("""\
name,employee_id,tax_id,primary_phone,primary_dept
Wile E Coyote,A1234,123-45-6789,(555)111-2222,R&D
Hong Kong Phooey,B5678,234-56-7890,(555)222-3333,Sales
Magilla Gorilla,C9012,345-67-8901,(555)333-4444,Operations
Quick Draw McGraw,D3456,456-78-9012,(555)444-5555,Finance
Snagglepuss,A7890,567-89-0123,(555)555-6666,Sales
Jabberjaw,B1357,678-90-1234,(555)666-7777,R&D
Secret Squirrel,C2468,789-01-2345,(555)777-8888,Operations
Morocco Mole,D9753,890-12-3456,(555)888-9999,Finance
Atom Ant,A1111,901-23-4567,(555)999-0000,Sales
Squiddly Diddly,B2222,012-34-5678,(555)000-1111,R&D
Grape Ape,C3333,112-23-3445,(555)121-2323,Operations
Deputy Dawg,D4444,223-34-4556,(555)232-3434,Finance
"""
)

# Accessing the table by unique key behaves like a dict
# - if the key is present, the matching record is returned
# - if the key is absent, KeyError is raised
# Since this table has multiple unique indexes, it can be used as a
# multi-directional dict
employees.create_index("name", unique=True)
employees.create_index("employee_id", unique=True)
employees.create_index("tax_id", unique=True)
employees.create_index("primary_phone", unique=True)

# Accessing the table by non-unique key behaves like a defaultdict(Table)
# - if the key is present, a new Table is returned containing the matching records
#   (with the same indexes defined as in the original table)
# - if the key is absent, an empty Table is returned
employees.create_index("primary_dept")

# List the full table
employees.present()

# List the R&D department
employees.by.primary_dept["R&D"]("R&D").present()

print("\nLookup by name")
for name in "Snagglepuss/Quick Draw McGraw/Secret Squirrel".split("/"):
    print(name, employees.by.name[name].primary_phone, employees.by.name[name].employee_id)

print("\nLookup by primary phone number")
for phone_num in "(555)555-6666 (555)444-5555 (555)777-8888".split():
    print(phone_num, employees.by.primary_phone[phone_num].name, employees.by.primary_phone[phone_num].employee_id)

print("\nLookup by employee id")
for emp_id in "A7890 D3456 C2468".split():
    print(emp_id, employees.by.employee_id[emp_id].name, employees.by.employee_id[emp_id].primary_phone)
