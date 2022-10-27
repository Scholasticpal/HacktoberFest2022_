def sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return(sum)

lst = [32,8,65,10]
n = len(lst)
ans = sum(lst)
print('Sum of the array is ', ans)
