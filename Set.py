s =set()
print(type(s))

a=[1,2,3,4,5]
s_from_list=set(a)
print(s_from_list)
print(type(s_from_list))

#Adding Elements in a set:                   #removing elements : .remove()
s.add(6)
print(s)               #6 gets added in the EMPTY set s
#But on again adding 6:
s.add(6)
print(s)           #Shows 6 only one time as::::::::::::::::::
"""SET ONLY RETAINS AN UNIQUE VALUE"""

#but adding another
s.add(1)
print(s)                      #1 and 6 addedd in empty set s

#SET OPERATIONS :
#1) UNION :    .union() - joins the two or more sets
s1 = s.union({2,3,4})
print(s1,s)

#2)INTERSECTION :  .intersection()  - finds common elements in two sets
s2 = s.intersection({1,2,3,4,5,6,7,8,9,0})                   #FORMAT NECESSARY  ({})
print(s2,s)

#3) DISJOINT CHECK :  .isdisjoint()   - retruns boolean values TRUE or FALSE after checking whether the set is disjoint or not
s3= {10,11,12}
print(s3.isdisjoint(s1))       #Returns True as both are disjoint

s4={10,11,12}
print(s4.isdisjoint(s3))       #Return false as both are same or joint or not disjoint

s5={10, 11, 12}
print(s5.isdisjoint(s4))     #Returns false again





