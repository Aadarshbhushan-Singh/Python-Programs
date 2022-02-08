#Deque is preffered over the list where quicker append is required from both the ends of the container.
#Deque is initialized by importing the collection.

import collections

'''Commands
1) append
2) appendleft
3) pop
4) index
5) count
6) remove
'''
#initialize deque
de=collections.deque([1,2,3])
print("Original de: ",de)

#use append to insert element at right end
#append appends 4 at the end.
de.append(4)
print("Append 4: ",de)

#use appendeft to insert the element at the left end
#appendleft appends 5 at the begining.
de.appendleft(5)
print("Appendleft 5: ",de)

#pop deletes the element from the right end
#pop deletes 4
de.pop()
print("Pop(deleted 4 from end): ",de)

#popleft deletes the element from the left end
#popleft deletes 5
de.popleft()
print("Popleft(deleted 5 from the begining",de)


#Adding some elements to de
de.append(4)
de.append(5)
de.append(6)
de.append(7)
print("New de: ",de)

#using index to print the first occurance of 4
print("Index of 4: ",de.index(4))

#insert (i,a)
#insert a at ith position
de.insert(4,9)
print("Inserted 9 at 4th position: ",de)

#count is used to count the occurance of element a
#count the occurance of 3
print("Occurance of 3: ",de.count(3))

#using remove to remove the first occurance of element a
#remove the first occurance of 3
de.remove(3)
print("After removing 3: ",de)


#extend adds the elements to the right
#adding some elements to the right
de.extend([10,20,30,40])
print("After extending the values: ",de)

#extendleft adds the element to the left
#adding some elements to the left side
de.extendleft([100,200,300])
print("After extending from left: ",de)

#rotate shifts the values form right to left. If the value of the argument is negative, then the element is rotated from left to right.
#rotating 2 elements to right
de.rotate(-2)
print(de)

#reverse is used to reverse the elements
print("De without reverse: ",de)
de.reverse()
print("De After reversing: ",de)