
for i in range(0,101,2):
    print(i)

print("HELLO RAHUL")


for l in range(46):
    print(l)


for k in range(10,101,10):
    print(k)


for p in range(5,51,5):
    print(p)


# TABLE

n = int(input("PLEASE TELL YOUR NAME :- "))

for i in range(n,(n*10)+1,n):      
    print(i)

# ( n =  Mhanje user cha input this is start position )
# (n*10 = mhanje jith paryant jaych tevdh 10 paryant janar )
# ( +1 = mhanje 10 paryant thambel)
# (n = mhanje gapp [user jo no denar tyachya madhla gapp])




# FOR LOOPS IN STRING 

a = "students"

for i in a :
    print(i)

for i in range(len(a)):    # len ( counting karnya sathi)
    print(i)


for i in range(len(a)):
    print(f"{i} : {a[i]}")  # CHARACTER SOBT NUMBER PN YENAR




# BREAK AND CONTINUE AND ELSE

for i in range(1,20):
    if i == 12:
        break       # jagge var thmbnar oudhe jaun nahi denar
    print(i)



for i in range(1,21):
    if i == 12 or i == 3 or i==7:
        continue      # skip karnar number
    print(i)


# else with break run hot sobt chaltat
# JAR ELSE CHALALA TRR BREAK NAHI CHALT
# JAR BREAK CHALA TRR ELSE NHI CHALAT

for i in range(1,21):
    if i == 12:
       break
    print(i)

else:
    print("rahul ")


for i in range(1,21):
    if i == 77:
       break
    print(i)

else:
    print("rahul ")

