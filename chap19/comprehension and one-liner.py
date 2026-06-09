

# ternary operation

#print("even number") if a % 2 ==0 else print("odd number")

# comprehension

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]

v = []

for i in a:
    if i % 2== 0:
        v.append(i)

print(v)


v = [i for i in a if i %2==0]    # LIST COMPREHENSIONS
print(v)