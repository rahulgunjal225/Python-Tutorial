
# QUE 1 = Print all positive and negative elements separately

l = [3,-1,4,-5,9]
pos = []
neg = []

for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(f"YOUR POSITIVE ELEMENTS ARE{pos}")
print(f"YOUR NEGATIVE ELEMENTS ARE{neg}")


# QUE 2 = Find the mean (average) of all list elements

a = [10,20,30,40]

sum = 0

for i in a:
    sum = sum + i

print(f"YOUR AVERAGE IS {sum/len(a)}")    # SUM/LENG IS FORMULA OF MEAN


# QUE 3 = Find the greatest element and print its index

b = [10,20,40,30,44,5,66,7777,]

largest = b[0]
index = 0

for i in range(len(b)):
    if b[i] > largest:
        largest = b[i]
        index = i

print(f"YOUR LARGEST VALUES IS {largest} AT INDEX {index}")


# QUE 4 = . Find the second greatest element

c = [11,22,3,44,56,43,90]

largest = c[0]

sec_largest = c[0]

for i in c:
    if i > largest:
        sec_largest = largest
        largest = i

    elif i > sec_largest:
        sec_largest = i
        

print(sec_largest)


# QUE 5 = Check if the list is already sorted

p = [2,1,22,54,66,7,88,9,0,7,]

for i in range(len(p)-1):
    if p[i] > p[i+1]:
        print("YOUR LIST IS NOT SORTED")
        break
    
    else:
        print("YOUR LISt IS SORTED")

