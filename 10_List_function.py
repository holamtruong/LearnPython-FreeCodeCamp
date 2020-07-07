lucky_number = [4, 8, 15, 23, 42]
friends = ["Lu", "Su", "Na", "No", "Nai"]


friends.extend(lucky_number)
print(friends) # =>  ['Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42]

friends.append("Dom")
print(friends)  # => ['Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42, 'Dom']

friends.insert(1, "Super Lu")
print(friends)  # => ['Lu', 'Super Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42, 'Dom']

friends.remove("Super Lu")
print(friends) # => ['Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42, 'Dom']

friends.pop()
print(friends) # => ['Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42]

friends.insert(1, "Lu")
print(friends)  # => ['Lu', 'Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42]

print(friends.count("Lu"))  # => 2

print(friends.index("No")) # => 4

lucky_number.sort()
print(lucky_number) # => [4, 8, 15, 23, 42]

lucky_number.reverse()
print(lucky_number) # => [42, 23, 15, 8, 4]

friend2 = friends.copy()
print(friend2) # =>['Lu', 'Lu', 'Su', 'Na', 'No', 'Nai', 4, 8, 15, 23, 42]

# reset the list
friends.clear()
print(friends)











