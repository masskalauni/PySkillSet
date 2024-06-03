#lists in python
#list is a collection of items in a particular order
#list is mutable (can be changed)
#list is defined by square brackets
#list can have any data type
#list can have any number of items
#list can have duplicate items
#list can have nested list
#list can have different data types
marks=[90,80,70,60,40.5,40]
print(marks)
length=len(marks)
print(length)
print(marks[0])
print(marks[1])
# print(marks[10]) #index out of range
#string is immutable but lists are mutable
#lets see how to change the value of a list
marks[0]=100
print(marks)
#lets see how to add a new item to the list
marks.append(50)
print(marks)
#lets see how to insert a new item to the list at a particular index
mahesh=[90,80,"math","science","mnr"]
print(mahesh)
mahesh.insert(2,100)
print(mahesh)

#lets see how to remove an item from the list
variable=['kalesh','haresh',70,70,'delhi','mumbai']
print(variable)
variable.remove('kalesh')
print(variable)



#list methods
#append()
#insert()
#remove()
#pop()
#sort()
#reverse()
#clear()

#append()
subject=['math','science','english']
print(subject)
subject.append('social') #adds at the end
print(subject)

#insert()
subject.insert(2,'hindi') #inserts at a particular index
print(subject)


#remove()
subject.remove('math') #removes the item
print(subject)

#sort()
numbers=[90,80,70,60,50,40]
print(numbers)
numbers.sort() #sorts the list in ascending order
print(numbers)


#reverse()
originalMessage=[20,10,'hello',12,'delhi']    #reverse the list
print(originalMessage)
originalMessage.reverse()
print(originalMessage)


#pop()
subject=['math','science','english','social']
print(subject)
subject.pop() #removes the last item or separate the last item
print(subject)
subject.clear() #clears the list


#Example 
#WAP to enter the name of 3 movies and store them into a list and then print the list
movies=[]
movie_first=input("Enter the name of the first movie: ")
movies.append(movie_first)
movie_second=input("Enter the name of the second movie: ")
movies.append(movie_second)
movie_third=input("Enter the name of the third movie: ")
movies.append(movie_third)
print(movies)



#Tuples in python

#Tuples are similar to lists but they are immutable(not changeable)
#Tuples are defined by round brackets
#Tuples can have any data type
#Tuples can have duplicate items
#Tuples can have nested tuples
#Tuples can have different data types
#Tuples can have any number of items

tuple=(10,20,30,40,50)
print(tuple)
print(tuple[0])
   #it is same as that of list but the only difference is that we cannot change the value of tuple
    #tuple[0]=100 #error
#let take small mind test
tup=(1,)
print(tup) #what is the output
print(type(tup)) #what is data type of tup


tup1=(11)
print(tup1) #what is the output
print(type(tup1)) #what is data type of tup1

#above  2 examples are very important to understand the concept of tuple in python
#tup=(1,) is a tuple with one item
#tup1=(11) is an integer not a tuple


#tuple methods

#count()
#index()

#count()
numbers=(10,20,30,40,50,20,30,20)
numbers.count(20) #counts the number of times 20 is present in the tuple
print(numbers.count(20))