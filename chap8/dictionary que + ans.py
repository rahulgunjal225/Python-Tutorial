
# QUE 1 = Merge two dictionaries into one

d1 = {'a' : 10 , "b" : 20 , "c" : 30}
d2 = {'d' : 40 , "e" : 50 , "f" : 60}

d1.update(d2)    # USED METHOD
print(d1)

for i in d2:
    d1[i] = d2[i]

print(d1)


# QUE 2 = Sum all values in a dictionary

d1 = {'a' : 10 , "b" : 20 , "c" : 30}

sum = 0

for i in d1:
    sum = sum + d1[i]

print(sum)



d = {"a": 10, "b": 20, "c": 30}

total = sum(d.values())

print("Sum =", total)





# QUE 3 = Count the frequency of each element in a list using a dictionary

l = ['a','s','d','f','a','a','a','d']

d = {}

for i in l:
    if i in d.keys():
        d[i] = d[i]
    
    else:
        d[i] = 1

print(d)


# QUE 4 = Combine two dictionaries, adding values for common keys

d1 = {'a' : 10 , "b" : 20 , "c" : 30}
d2 = {'c' : 40 , "e" : 50 , "f" : 60}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]

    else:
        d1[i] = d2[i]

print(d1)
