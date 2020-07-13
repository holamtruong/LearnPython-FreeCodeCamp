employee_file = open("employees.txt", "r")

# Check readable
print(employee_file.readable())

# Read file
"""
print(employee_file.read())
"""

"""
print(employee_file.readlines()[2])
"""


for x in employee_file.readlines():
    print(x)


employee_file.close()