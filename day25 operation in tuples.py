# tuples are immutable,hence if you want to add ,remove or change tuple items ,then first you meet
# conert yhe tuple for a list

country=("japan","india","usa","spain")
temp=list(country)
temp.append("chain")
temp.pop(3)
temp[2]="italy"
country=tuple(temp)
print(country)



tuple1=(1,2,2,3,3,3,3,3,4,5,6,7,8,9,)
res=tuple1.count(3)
print('count of 3 in tuple is:',res)


