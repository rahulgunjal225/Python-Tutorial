# tuples is not changed
# tuples are orderd collection of data items.
# they are store multiples items in a single variables.
# tuples items are sepreted by commans and enclosed within round brackets ().
# tuples are unchangele meaning we can not alter them after creation.




tup=(5,7,3,4,8)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])


if 3 in tup:
    print("yes 3 is present in this tuple")


tup2=tup[1:4]
print(tup2)