Convert a list of Tuples into Dictionary

//code

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
        
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))
