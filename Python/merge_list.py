from functools import reduce 

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
l4 = [10, 11, 12]

l = [l1, l2, l3, l4]

data = reduce(lambda a, b: a+b, l)
print(data
