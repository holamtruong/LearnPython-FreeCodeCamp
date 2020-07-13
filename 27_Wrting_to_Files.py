# append (not modify  old content, only add new content)
employee_file = open("employees.txt", "a")
print(employee_file.writable())
employee_file.write("\nDom - Soldier")
employee_file.close()

# write (overwrite the content)
employee_file_2 = open("employees2.txt", "w")
print(employee_file_2.writable())
employee_file_2.write("\nNai - General director")
employee_file_2.close()

# => try for index.html file
