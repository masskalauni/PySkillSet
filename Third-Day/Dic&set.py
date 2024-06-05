#In this lecture we are going to learn about Dictionary and Set Built in data types in Python 

# Dictionary
# Dictionary is a collection of key value pairs
# Dictionary is unordered and mutable
# Dictionary is represented by {}
# Dictionary keys should be unique and immutable
# Dictionary values can be mutable or immutable
# Dictionary can be nested
# Dont allow duplicate keys
# Thinks like real dictionary

# Creating a dictionary
dict={
    "name":'mass',
    "age":20,
    "city":'mnr',
    "marks":[90,80,70]
}
print(dict)
print(type(dict))

dict["name"]="mass kalauni"
dict["surname"]="kalauni"
print(dict)
# Accessing elements from dictionary
# we can access elements from dictionary using keys
print(dict['name'])


#nested dictionary 
dictionary={
    "name":'mass',
    "age":20,
    "subjects":{
        "phy":90,
        "chem":80,
        "math":70
    }
}
print(dictionary)
print(dictionary['subjects']['phy'])



# Methods in dictionary
# clear() : clears the dictionary
# copy() : returns a copy of dictionary
# fromkeys() : returns a dictionary with specified keys and values
# get() : returns the value of specified key
# items() : returns a list containing a tuple for each key value pair
# keys() : returns a list containing the dictionary keys
# pop() : removes the element with specified key
# popitem() : removes the last inserted key value pair
# setdefault() : returns the value of specified key. If the key does not exist, insert the key with the specified value
# update() : updates the dictionary with the specified key value pairs
# values() : returns a list of all the values in the dictionary
Example_dict={
    "first_name":"prem ",
    "last_name":"kalauni",
    "age":20,
    "city":"mnr",
    "marks":[90,80,70]
}

print(Example_dict)

#1. clear()
Example_dict.clear()
print(Example_dict)

#2. copy()
copied_dict=Example_dict.copy()
print("Hello this is copied dictionary using copy method ",copied_dict)

#3.values()
personal_info={
    "name":"prem",
    "age":20,
    "city":"mnr",
    "marks":[90,80,70]
}
values_display=personal_info.values()
print(values_display)

#4. keys()
print(personal_info.keys())

#5. items()
print(personal_info.items())
print(list(personal_info)) # this will return list of keys in dictionary know as type casting

#6. get()
print(personal_info.get("name"))

#7. pop()
personal_info.pop("age")
print(personal_info)

#8. popitem()
personal_info.popitem()
personal_info.popitem()
print(len(set(personal_info)))


#9. update()
personal_info.update({"name":"prakash kalauni"})
print(personal_info)




# Set                                      
# Set is a collection of unordered and unindexed elements
# Set is represented by {}
# Set is mutable
# Set does not allow duplicate elements
# Set is used to perform mathematical set operations like union, intersection, difference, symmetric difference etc
# Set is used to remove duplicate elements from list


# Creating a set
Example_set={1,2,3,4,5,6,7,8,9,10}
print("Example Set is :",Example_set)
print(type(Example_set))


collection={1,1,12,1,12,"hello","world",123} #what is the output of this set ?
#output is {1,2,12} because set does not allow duplicate elements 
print("This is set with duplicate elements",collection)
print(len(collection)) # this will return 5 because set does not allow duplicate elements


# Empty set
set={} # this is not empty set this is empty dictionary 
print(type(set))


# new_empty_set=set() # this is empty set



fruits={"apple","banana","mango","orange"}
print("Some name of fruits:",fruits)
print(type(fruits))
print(tuple(fruits)) #type casting into tuple 
print(len(fruits))

for i in fruits:
    print(i)


#methods in set
#1 add()
fruits.add(45)
print(fruits)

#2 clear()
fruits.clear()
print(fruits)
print(len(fruits))

#3 update
set1={1,2,3,4,5}
set2={6,7,8,9,10}
print(set1)
print(set2)
set1.update(set2)
print("Updated set is:",set1)


#4 remove()
set1.remove(2)
print(set1)

#5 pop()
set2.pop()
print(set2)

#6 union()
set_first={"prem","mass","tek","prakash"}
set_second={"cow","bull","goat","dog","prem","mass","tek"}
union_set=set_first.union(set_second)
print(union_set)


#7 intersection()
intersection_set=set_first.intersection(set_second)
print(intersection_set)


#Practice Question
'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
'''
marks_dict = {}

sub_first = int(input("Enter the marks of first subject: "))
marks_dict["phy"] = sub_first

sub_second = int(input("Enter the marks of second subject: "))
marks_dict["chem"] = sub_second

sub_third = int(input("Enter the marks of third subject: "))
marks_dict["eng"] = sub_third

print(marks_dict)




''''
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)

'''
setDemo={9,'9.0'}
print(setDemo)

setDemo2={
    ("integer",9),
    ("float",9.0)
}
print(list(setDemo2))