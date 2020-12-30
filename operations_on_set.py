#Declearing a set
set1={1,2,3,4,5}
print(set1)
print(len(set1))
list1=['a','b',1,2,3,4,5]
print("List: ",list1)
set2=set(list1)
print("Set: ",set2)
set2.add('apple')

#Adding a value to set
set2.add('apple')
print(set2)

#Adding a set to the set
set2.add(('ball','cat'))
print(set2)

#Updating a set
set2.update(['hello','world'])
print(set2)

#Updating a list to set
list2=['hi','how','are','you?']
set2.update(list2)
print(set2)

#Updating a set to set
set3={'I','am','fine.'}
set2.update(set3)  
print(set2)

set2.discard('hello')   #discard() doesn't show any error if there is not value in the given set
print(set2)
set2.remove("world")   #remove() gives an error if there is not any value in the given set.
print(set2)


#UNION
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b)
print(a.union(b))
b.union(a)
print(b.union(a))
print(a.union(b)==b.union(a))

#INTERSECTION
print(a.intersection(b))
print(b.intersection(a))
print(a.intersection(b)==b.intersection(a))

#DIFFERENCE
print(a.difference(b))
print(b.difference(a))
print(a.difference(b)==b.difference(a))


#Sorting a set with difference Hackerrank question for 10 points
set1={2, 4, 5, 9}
set2={2, 4, 11, 12}
set3=set1.difference(set2)
set3.update(set2.difference(set1))
print(set3)
print(sorted(set3))