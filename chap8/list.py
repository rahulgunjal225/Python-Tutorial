
# MUTTABLE
# ONLY USED SQUARE BRACKETS []

a = [1,2,3,3,3,2,]

print(a)
print(type(a))


print(a[1])   # ORDER NATURE YOU CAN ACESS ANY ELELMENT AT ANY POINT OF TIME



# MUTABLE NATURE = YOU CAN CHANGE ANY VALUES ON YOUR LIST
L = [11,23,56,70]

L[1] = 20  # B MADHLI 1 NO CHI VALUES CHANGE KARNYA SATHI

print(L)   # LIST MADHLI VALUES CHANGE KARU SHAKTO


# DULICATE
t = [11,22,33,44,44,4,4,4,44,33,3,33,]



# Creating and Accessing Lists

fruits = ["apple", "banana", "mango"]

print(fruits[0])      # apple
print(fruits[-1])     # mango
print(fruits[0:2])    # ['apple', 'banana']

fruits[1] = "grape"   # mutation - lists allow this!


# TRAVERSING ON LIST (LOOP CHALVANE)


a = [11,22,12,55,66,]

# TRAVERSING ON VALUES
for i in a:
    print(i)

# TRAVERSING ON INDEX
for i in range(0,len(a)):   # JRR LAST PARYANT JAYCH ASEL TRR LEN(A) LIHYCH
    print(f'{i} : {a[i]} ')