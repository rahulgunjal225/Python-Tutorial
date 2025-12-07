# list are ordered collection of data items
# they store multiple items in a single variables
# list items are separated by commas and enclosed within square brackets[]
# list are changeable meanings we can alter them after creation


l=[1,2,3,6,7]
print(l)
print(type(l))


marks=[12,45,67,86,45,"rahul",]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])



print(marks[-3]) # negative index
print(marks[len(marks)-3]) # positive index
print(marks[5-3]) #posititve index


if 7 in marks:
    print("yes")
else:
    print("no")


if "hul" in "rahul":
    print("yes")
else:
    print("no")