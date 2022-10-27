'''
input:
    1
    2
    3
output:
    the array is: ['1','2','3']
input:
    first position: 1
    second position:2
output:
    the new array is ['2','1','3']

'''


list1 = []
i = 0
a = 0
#ask user to create list
print("Input numbers and input 'end' to stop inputing")
while i < 1:
    x = input()
    if x == "end":
        break
    else:
        list1.append(x)
#swap elements of list
print("the array is:", list1)
print("select two positions to be swapped")
n = int(input("first position: "))
m = int(input("Second position: "))

if n <= len(list1) and m <= len(list1):
    list1[n-1],list1[m-1] = list1[m-1], list1[n-1]
    print("the new list is:",list1)
else:
    print("INVALID POSITIONS")
