string= list(input("Enter the number of elements in list:").strip().split(" "))
newstring=[]
count=0
removeword=input("Enter word to remove: ")
removeocc=int(input("Enter the occurrence to remove: "))
for word in string:
    if(word==removeword):
        count=count+1
        if(count!=removeocc):
            newstring.append(word)
    else:
        newstring.append(word)
if(count==0):
    print("Item not found ")
elif(count<removeocc):
    print("The word does not occur {} times".format(removeocc))
else: 
    print("Updated string is: ",newstring)
