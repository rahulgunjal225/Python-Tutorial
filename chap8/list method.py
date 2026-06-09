
# METHODS [ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# CRUD OPERATION ( CREATE , READ , UPDATE , DELETE )

a = [10,20,50,55,60]

a.append( 90 )
a.append( 'HEllo' )  # ADDS TO LAST SPOT
print(a)

a.insert(2 , 30)   # ADD VALUES IN MIDDLE
print(a)

b = a.pop()        # REMOVES LAST NUMBERS
print(b)

b = a.pop(4)
print(a)

a.remove(10)        # REMOVES 1ST ELEMENTS
print(a)

#a.clear()
#print(a)           # ALL CLEARS


a.sort()            # ASCENDING ORDER
a.sort(reverse=True)            # DESCENDING ORDER
print(a)

