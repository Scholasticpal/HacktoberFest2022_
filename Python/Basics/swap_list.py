lst = ['a', 'b', 'c']
x, y = 'a', 'c'
# Get indices i and j of elements x and y
i, j = lst.index(x), lst.index(y)
# Swap element index i with element index j
lst[i], lst[j] = lst[j], lst[i]
print(lst)
# ['c', 'b', 'a']
