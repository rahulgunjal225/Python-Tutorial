# map

def cube(x):
    return x*x*x
print(cube(2))


r=[12,34,56,78]
newr=list(map(cube,r))
print(newr)

# filter

def filter_function(a):
    return a>4

newnewr=list(filter_function,r)
print(newnewr)
