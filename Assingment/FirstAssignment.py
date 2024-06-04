#Task1  OUTPUT TO BE DISPLAYED : Python is my favorite Language
print("Python is my favorite Language")

#Task2 Print the message "The answer is 42" using two separate objects.
print("The answer is",42)

#Task3 Print the fruits "apple", "banana", and "cherry" separated by a comma and a space.
print("apple", "banana", "cherry",sep="____________ ")

#Task4 Print the words "Hello" and "World!" on the same line.
print("Hello",end=" ")
print("World!")

#Task5 OUTPUT TO BE DISPLAYED: x : 10 y : 100 z : 0.1
x=10
y=100
z=0.1
print("x :",x,"y :",y,"z :",z)


#Task6

# Performing all operations in Python

# Addition
add_int = 5 + 5
add_float = 5.0 + 5.0

# Subtraction
sub_int = 30 - 3
sub_float = 30.0 - 3.0

# Division
div_int = 36 // 2
div_float = 36.0 / 2.0

# Multiplication
mul_int = 9 * 6
mul_float = 9.0 * 6.0

# Modulus
mod_int = 19 % 5

# Absolute value
abs_int = abs(-19)

# Conversion to integer from float
int_val = int(100.9)

# Collecting all results
results = {
    "addition": (add_int, add_float),
    "subtraction": (sub_int, sub_float),
    "division": (div_int, div_float),
    "multiplication": (mul_int, mul_float),
    "modulus": mod_int,
    "absolute": abs_int,
    "integer_conversion": int_val
}

print(results)


#Task7 
'''
TASK TO BE DONE : ASSIGN STRINGS TO VARIABLES
CONCATENATE:
    OUTPUT: Turing Test
REPETITION:
    OUTPUT: ATTENTION!!! ATTENTION!!! ATTENTION!!!
LENGTH:
    BOILERPLATE (Copy the code and print the length of the string):
        name = "John Doe"
'''
string_first="Turing"
string_second="Test"
concatenate=string_first+" "+string_second
print(concatenate)

string="ATTENTION!!! "
repetition=string*3
print(repetition)

name = "John Doe"
print(len(name))



#Task8
'''
TASKS TO BE DONE
    1) Assign a string value in smallcase to a variable and convert to upper case
    2) Assign a string value in bigcase to a variable and convert to lower case
    3) Assign the sentence "My name is John Doe" in a variable and find the index of John
    4) Replace name `John Doe` with your name
    5) Assign your name in a variable and store first name in fname, last name in lname using split() function
    6) Demonstrate format() function
'''
#1
lowercase_variable="python"
uppercase_variable=lowercase_variable.upper()
print(uppercase_variable)

#2
bigcase_variable="PYTHON"
lowercase_variable=bigcase_variable.lower()
print(lowercase_variable)

#3
sentence="My name is John Doe"
index=sentence.index("John")
print(index)

#4
name='John Doe'
replace_name=name.replace(name,"Mass Kalauni")
print(replace_name)

#5
name="Mass Kalauni"
fname,lname=name.split()
print(fname)
print(lname)

#6
name="Mass Kalauni"
print("My name is {}".format(name))



#Task9
'''
TASK TO BE DONE :
1. Assign a variable with a number and Check if the Number is Positive or Negative.
2. Check if the number is greater than 20.
'''

#1
number=10
if number>0:
    print("Number is Positive")
else:
    print("Number is Negative")

#2
if number>20:
    print("Number is greater than 20")
else:
    print("Number is less than 20")


#Task10
'''
  Assignment : Print Numbers from 2 to 10:
'''
#  for i in range(2,11):
#     print(i) 
i=2
while i<11:
    print(i)
    i=i+1

#Task11
'''
Assignment -
  1.Take first 10 natural numbers and multiply by 2 to each number

'''
for i in range(1,11):
    print(i*2)

#This below code is also correct    
natural_number=list(range(1,11))
print(natural_number)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplied_number=[i*2 for i in natural_number]
print(multiplied_number)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#Task12
'''WAP to check the number is positive ,negative or zero and store the string in result variable'''
number=10
if number>0:
    result="Number is Positive"
elif number<0:
    result="Number is Negative"
else:
    result="Number is Zero"
print(result)


#Task13
'''WAP to print all even number from  1 to 10 '''
even_number=[]
for i in range(1,11):
    if i%2==0:
        even_number.append(i)
print(even_number)

# for i in range(1,11):
#     if i%2==0:
#         print(i)


#Task14
''' 1.Put the first element to its corresponding variable
    2.Change the last element to 12
'''


li = [1,2,3,4,5,6]
first_element = None

first_element = li[0]
print(first_element)

li[-1] = 12

print(li)


#Task15
'''
Use slicing to create a list, downstairs, that contains the first 6 elements of areas by using slicing method.
Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas by using slicing method.
'''

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
sliced_areas = []
downstairs = areas[:6]
upstairs = areas[-4:]
print(downstairs)
print(upstairs)



# Task 16
'''
From given list: words = ["elephant", "dog", "hippopotamus", "cat", "giraffe"]
1. Sort the words by their length in ascending order.
'''
words = ["elephant", "dog", "hippopotamus", "cat", "giraffe"]   
words.sort(key=len)
print(words)


# Task 17
"""Create a list with odd numbers from range 1 to 20 and store it in variable `odd`"""
odd = [i for i in range(1, 21) if i % 2 != 0]
print(odd)



# Task 18
'''

Given 2 lists `a` and `b` use zip and create a new list `c` where each element of c is the sum of elements of a and b
'''
a =  [1,2,3,4,5]
b = [3,4,1,5,6]
c = []
for i, j in zip(a, b):
    c.append(i + j)
print(c)


# Task 19
'''
- Given the lists: fruits = ['apple', 'banana', 'orange']
- Use the enumerate() function to iterate over the fruits list.
For each fruit in the fruits list, print the fruit and its index (starting from 1) in the colors list.
- Output:

Fruit: apple, Index: 1
Fruit: banana, Index: 2
Fruit: orange, Index: 3
'''
fruits = ['apple', 'banana', 'orange']
for index,fruit in enumerate(fruits,1):
    print(f"Fruit: {fruit}, Index: {index}")


# Task 20

'''
You have been given a dictionary `student_dict` containing information about students' ages. Perform the following operations:

1. Update the dictionary to include a new student named "David" with age 23.
2. Print all the values in the dictionary.
3. Print all the keys in the dictionary.
4. Print all the key-value pairs in the dictionary.
5. Clear the dictionary.
6. Print the length of the dictionary.

### Expected Output:
```
# Values
dict_values([20, 22, 21, 23])

# Keys
dict_keys(['Alice', 'Bob', 'Charlie', 'David'])

# Items
dict_items([('Alice', 20), ('Bob', 22), ('Charlie', 21), ('David', 23)])

# Length
0
'''    

student_dict = {"Alice": 20, "Bob": 22, "Charlie": 21}

#1
student_dict["David"]=23
print(student_dict)

#2
print(student_dict.values())

#3
print(student_dict.keys())

#4
print(student_dict.items())

#5
student_dict.clear()
print(student_dict)
print(len(student_dict))


# Task 21
'''
# Task 10
You have been given a tuple `my_tuple` containing the ages of students. Perform the following operations:

1. Count the number of occurrences of the age 20 in the tuple.
2. Find the index of the first occurrence of the age 25 in the tuple.
'''
my_tuple = (18, 20, 22, 20, 25, 21)
print(my_tuple.count(20))
print(my_tuple.index(25))



# Task 22
'''
# Task 11

You have been given two sets, `set1` and `set2`. Perform the following set operations:

1. Find the intersection of `set1` and `set2`.
2. Find the union of `set1` and `set2`.
3. Find the set difference of `set1` and `set2` (elements in `set1` but not in `set2`).
'''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Write the code below
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))