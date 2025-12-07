l=[12,34,5,56,78,12]
print(l)
l.append(7)
# append is a method
l.sort()
# sort means increse order
l.sort(reverse=True)
# decrese order
l.reverse()
print(l.index(12))
print(l.count(12))
l.insert(5,899)
m=[900,8700,6700]
l.extend(m)
print(l)
chai = ["masal","lemon","ginger"]
print("-".join(chai))