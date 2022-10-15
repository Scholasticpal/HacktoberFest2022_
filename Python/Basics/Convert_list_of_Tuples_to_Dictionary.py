lst = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
#ans is the dictionary
ans = {}

# iterating over the list of tuples
for i in range(len(lst)):
  ans.setdefault(lst[i][0], []).append(lst[i][1])

print(ans)
