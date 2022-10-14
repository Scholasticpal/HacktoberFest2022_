arr = []   #initializing empty array
n=int(input("Enter total number of elements : "))  #taking input of total number of element in an array
for i in range(0,n):    #using for loop to get all element input one by one
   ele=int(input("Enter elements value : "))
   arr.append(ele)      #storing all element in arr one by one
Sum = 0                 #initializing sum variable to zero , this will hold our result

for i in range(len(arr)):  #iterating every element of array
   Sum = Sum + arr[i]      #adding each and every element one by one in sum
print (f"The total sum of all elements will be : {Sum}")    #printing the final sum of all element