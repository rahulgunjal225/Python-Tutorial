#  set is collection of well defined objects  #     
#   set are unordered collection of data items 
#  they store multiple items in a single variables
#  set items are seorated by commas and enclosed within curly backets{}
#  sets are unchangeable, meaning you cannot change items of the set once created
#  sets do not contain duplicate items


r={2,3,2,4,4,5,7,6,8,5}
print(r)


info={"rahul",234,"ashu", True,123,1,2,3}
print(info)


rahul={}
print(type(rahul))


ashu=set()
print(type(ashu))


for value in info:
    print(value)