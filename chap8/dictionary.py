
d = {}

print(type(d))

a = {10:11,20:200,30:300,40:400}    #KEY AND VALUES [PAIR]  KEY IS ROLE OF INDEX

print(a[10])    #  100 - READING A VALUES

# VANNILA PYTHON

a[50] = 500     # CREATING A NEW KY  VALUE PAIR
a[10] = 100     # UPDATING A KEY VALUE THAT ALREADY EXIST

print(a)



# METHODS APPROCH

b = {10:100,20:200,30:300,40:400}

b.clear()    # Removes all the elements from the dictionary
print(b)

q = b.fromkeys([10,20,30,],50)    # Returns a dictionary with the specified keys and value
print(q)

b.get(10)        # 	Returns the value of the specified key
print(b)

print(b.items())    # Returns a list containing a tuple for each key value pair

print(b.keys())      # 	Returns a list containing the dictionary's keys
print(b.values())    
print(b.pop(20))     # Removes the element with the specified key
print(b)
b.popitem()          # Removes the last inserted key-value pair
print(b)
print(b.setdefault(60,3000))   # Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(b)

b.update({10:10000})   # updates the dictionary with the specified key-value pairs
b.update({70:10000})
print(b)




#  TRAVERSING (LOOPS)

l = {10:100,20:200,30:300,40:400}

for i in l:
    print(f"key {i} values {l[i]}")