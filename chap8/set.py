
# UNIQUES VALUES ONLY
# USED CURLY BRACKETS {}

s = {1,2,3,4,5,6,7}

print(type(s))


a = [12,11,11,45,54,34,4,4,4,]

b = set(a)

print(b)

p = {"hello"}

print(hash(p))


l = {11,22,33,55,66,7,90}

for i in l:
    print(i)       # IT IS UNORDERD


# METHOD

l.add(88)
print(l)

l.clear()
print(l)

l.discard(11)
print(l)


a1 = {10,20,30,40}
a2 = {20,30,80,50,}

print(a1.difference(a2))    # A1 - A2
print(a1 - a2)    # A1 - A2
print(a2 - a1)    # A2 - A1


a2 -= a1
print(a2)   # a2 are updated all 

s1 = {10,20,30,40}
s2 = {10,50,30,77}
print(s1.intersection(s2))    # COMMON BHETAT


s1 &= s2
print(s1)    # S1 CAN BE CHANGE


p1 = {10,20,30,40}
p2 = {10,40,80,90}
p3 = {80,40}

print(p3 <= p2)     # P3 IS SUBSET OF P2 [1 can change not a subset]
print(p2 >= p3)     # P2 IS SUPERSET OF P3



q1 = {10,20,30,22,33}
q2 = {10,20,11,12,22,21,99}

print(q1.symmetric_difference(q2))    # COMMON NIGHUN JAYIL ANI VEG VEGLE RAHATAT
print(q1 ^ q2)    #  [power operator] COMMON NIGHUN JAYIL ANI VEG VEGLE RAHATAT

print(q1 | q2 )    # UNIUN