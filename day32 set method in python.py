R1={1,3,5,7,6,9}
R2={2,4,6,8,0}
print(R1.union(R2))
R1.update(R2)
print(R1,R2)

# union and update
# the union and update methods points all items that are upadate in the two sets 
# the union methods returns new set whereas update method add items into existing set from another set

city1={'india','russia','france','usa'}
city2={'UAE','tokyo','kabul','delhi'}
city3=city1.union(city2)
print(city3)

# intersection and intersection_update
# the intersection and intersection_update methods points only items that are simmiler to both the sets
# the intersection method return new set where intersection_update method update into the existing set from another set

city={'punjab','mumbai','pune','goa'}
city2={'punjab','delhi','gujrat','pune'}
city3=city.intersection(city2)
city.intersection_update(city3)
print(city3)

# symmetric_difference and symmetric_difference_update
# methods point only items that are not simmilar to both the set
# the symmetruc_difference method that returns a new set wheres symmetric_difference_update methods update into the existing set from another set

city={'punjab','mumbai','pune','goa'}
city2={'punjab','delhi','gujrat','pune'}
city3=city.symmetric_difference(city2)
city.symmetric_difference_update(city3)
print(city3)



