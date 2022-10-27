# initializing the list
tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]

# result
result = {}

# iterating over the tuples lists
for (key, value) in tuples:
   # setting the default value as list([])
   # appending the current value
   result.setdefault(key, []).append(value)

# printing the list
print(result)
