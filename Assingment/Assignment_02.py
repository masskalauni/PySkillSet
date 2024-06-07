#Lab 1 Re-write and run the example codes in sections (1.2.1, 1.2.2, 1.2.3) and play with it.

#Function definition with two positional arguments
def greet(name, message):
    return f"{message}, {name}!"
greeting = greet("KUcians", "Happy Coding")
print(greeting)  

# Function definition with two positional arguments
def greet(name, message):
    return f"{message}, {name}!"
greeting1 = greet(name="KUcians", message="Happy Coding")
greeting2 = greet(message="Happy Coding", name="KUcians")  
print(greeting1)  
print(greeting2)  

# Function definition with two positional arguments and one default one.
def greet(message,name="KUcians"):
    return f"{message}, {name}!"
# Function call with positional arguments
greeting = greet(message="Happy Coding")                
greeting1 = greet(message="Happy Coding", name="Ashwin") 
print(greeting)   
print(greeting1) 


#lab 2 Re-write and run the code examples in section (1.3.1, 1.3.2) and play with it.


#local variable
def my_function():
    x = 10
    print(x)   # x is accessible here

my_function()

#global variable
x = 10
def my_function():
    print(x)  # x is accessible here

my_function()

print("X is accessible here too: ", x)



#lab 3 
'''write a function that takes an integer as argument.return "KU" if it is divisible by 3, "AIC" when it is divisible by 5 and "KUAIC" when it is divisible by 3 and 5 both.'''

n=int(input("Enter a number: "))
def check_divisibility(n):
    if n%3 ==0 and n%5==0:
        return "KUAIC"
    elif n%3 ==0:
        return "KU"
    elif n%5 ==0:
        return "AIC"
    else:
        return "Not Divisible by 3 or 5"
result=check_divisibility(n)
print(result)


#lab 4   
'''1. Write a function that takes list of integers as parameters, square each elements and return it as list of integers.
2. In above case, sum the elements of list and return it. (use both built-in methods and explicitly for loop also.)
'''
 #1
def square_elements(l):
    return [i**2 for i in l]
l=[1,2,3,4,5]
result=square_elements(l)
print(result)


#2 
def sum_elements(l):
    return sum(l)
l=[1,2,3,4,5]
result=sum_elements(l)
print("The sum of list of elements is:",result)

#using for loop
def sum_elements(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

lst = [1, 2, 3, 4, 5]
result = sum_elements(lst)
print("The sum of the list of elements is:", result)
 

#lab 5
''''Write a program that takes variable/any number of integer arguments and return their sums (as above example)'''
def sum_elements(*agrs):
    return sum(agrs)
result=sum_elements(1,90,2,3,4,5)
print("The sum of the elements is:",result)


#lab 6
''''Create a decorator, so that we could increment the value by 1.'''
def increment_by_one(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return wrapper

@increment_by_one
def give_number(num):
    return num

print(give_number(3))  



#lab 7
''''write a program that takes two dictionaries as argument one containing price and another containing quantity. Calculate the total cost of medicine, using these dictionaries'''

medicine_prices = {
    "Paracetamol": 0.25,
    "Ibuprofen": 0.30,
    "Amoxicillin": 0.50,
    "Ciprofloxacin": 0.70,
}

medicine_quantity = {} 
medicine_quantity["Paracetamol"] = 100
medicine_quantity["Ibuprofen"] = 200
medicine_quantity["Amoxicillin"] = 50
medicine_quantity["Ciprofloxacin"] = 20

def calculate_total_cost(medicine_prices, medicine_quantity):
    total_cost=0
    for medicine in medicine_prices:
        total_cost += medicine_prices[medicine]* medicine_quantity[medicine]
    return total_cost  

result=calculate_total_cost(medicine_prices, medicine_quantity)
print("The total cost of medicines is:",result)
    

#lab 8 WAP to multiply two numbers using argument parser
'''import argparse
def multiply_two_numbers(num1, num2):
    return num1 * num2
def main():
    parser = argparse.ArgumentParser(description="Multiply two numbers")
    parser.add_argument("num1", type=int, help="First number")
    parser.add_argument("num2", type=int, help="Second number")
    args = parser.parse_args()
    result = multiply_two_numbers(args.num1, args.num2)
    print(f"The product of {args.num1} and {args.num2} is {result}")
if __name__ == "__main__":
    main()
    '''
#we can run this code in terminal by passing two numbers as arguments. 


#lab 9
''''write a function to convert temperature from fahrenheit to celcius.

$celcius = (fahrenheit - 32) * 5/9$

Print the output upto two decimal points.

Take input from the user.
'''
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 4)
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"The temperature in Celsius is: {celsius}")



#lab 10
''''
def area_of_circle(radius: int) -> float:
Please help me, calculate area of circle?
I only need two digits after decimal.
  
  '''
def area_of_circle(radius:int)->float:
    return round(3.14*radius**2,2)
radius=int(input("Enter the radius of the circle: "))
result=area_of_circle(radius)
print("The area of the circle is:",result)


#lab 11  
'''files = ['POWER_Point_Daily_19810104_20231124_027d9000N_081d9000E_LST.csv',
         'POWER_Point_Daily_19810104_20231124_028d0000N_081d9000E_LST.csv',
         'POWER_Point_Daily_19810104_20231124_028d0000N_082d0800E_LST.csv',
         'POWER_Point_Daily_19810104_20231124_028d0200N_081d7700E_LST.csv']

         **Hey, coder, I need your help. I have a list of csv file names (as in above cell). Could you give me extracted latitude and longitude from these names.**

         Output: (27.9000, 81.000)
         '''
import re

files = [
    'POWER_Point_Daily_19810104_20231124_027d9000N_081d9000E_LST.csv',
    'POWER_Point_Daily_19810104_20231124_028d0000N_081d9000E_LST.csv',
    'POWER_Point_Daily_19810104_20231124_028d0000N_082d0800E_LST.csv',
    'POWER_Point_Daily_19810104_20231124_028d0200N_081d7700E_LST.csv'
]

for file in files:
    # Extract latitude and longitude using regular expression
    lat_match, lon_match = re.findall(r"\d+d\d+", file)[-2:]

    # Convert latitude and longitude to decimal format
    lat = f"{lat_match[:-5]}.{lat_match[-5:-3]}{lat_match[-2:]}"
    lon = f"{lon_match[:-5]}.{lon_match[-5:-3]}{lon_match[-2:]}"

    print(f"Latitude: {lat}, Longitude: {lon}")


#lab 12
'''I have a GPA of students as follows:

Can you help sort by the name of the student.

from typing import Dict

gpa = {'Ritu': 2.75,
       'Neeta': 3.0,
       'Aarya': 3.5,
       'Kajal': 3.0,
       'Shuvam': 3.10,
       'Bjaya': 3.0
      }

      Expected Output:
{'Aarya': 3.5,
 'Bjaya': 3.0,
 ...
}
'''


from typing import Dict

gpa = {'Ritu': 2.75,
         'Neeta': 3.0,
         'Aarya': 3.5,
         'Kajal': 3.0,
         'Shuvam': 3.10,
         'Bjaya': 3.0
        }

sorted_gpa = dict(sorted(gpa.items(), key=lambda x: x[0]))
print(list(sorted_gpa))



#lab 13
'''
def picking_numbers(balls: List[int]) -> List[int]:
  """Can you help me picking even positioned numbers?
  """
  # your code here.

# For example
# print(picking_numbers([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
# print(picking_numbers([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]
# print(picking_numbers([1, 2, 3, 4, 5, 6, 7]))  # Output: [1, 3, 5, 7]
'''
def picking_numbers(balls:list[int])->list[int]:
    return balls[::2]
print(picking_numbers([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
print(picking_numbers([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]
print(picking_numbers([1, 2, 3, 4, 5, 6, 7]))  # Output: [1, 3, 5, 7]


#lab 14
'''
def sum_odd(a: int, b: int) -> int:
    """sum of all odd numbers between (including) a and b
    """
    # your code here.

# For example
# print(sum_odd(2, 4))  # Output: 3
# print(sum_odd(2, 7))  # Output: 15
'''

def sum_odd(a:int,b:int)->int:
    return sum(i for i in range(a,b+1) if i%2!=0)
print(sum_odd(2, 4))  # Output: 3


#lab 15
'''
def keep_consonants(word: str) -> str:
    """word is a string of lowercase letters
       Returns a string containing only the consonants
       of word in the order they appear.
    """
    # your code here.

# For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs'''

def keep_consonants(word : str)->str:
    return "".join([i for i in word if i not in "aeiou"])
print(keep_consonants("abcd"))  # prints bcd
print(keep_consonants("aaa"))  # prints an empty string
print(keep_consonants("babas"))  # prints bbs


#lab 16
'''
def remaining_fruits(fruits: List[str], bought: List[str]) -> List[str]:
    """I have list of fruits to buy, I bought some of them.
       What are other remaining fruit(s) to buy. Could you help me?
    """
    # your code here.

# For example
# fruits = ['orange', 'apple', 'grapes', 'papaya', 'mango', 'watermelon']
# bought = ['apple', 'papaya', 'mango']
# print(remaining_fruits(fruits, bought))  # Output: ['orange', 'grapes', 'watermelon']'''


def remaining_fruits(fruits: list[str], bought: list[str]) -> list[str]:
    return [fruit for fruit in fruits if fruit not in bought]

fruits = ['orange', 'apple', 'grapes', 'papaya', 'mango', 'watermelon']

bought = ['apple', 'papaya', 'mango']
print(remaining_fruits(fruits, bought))  # Output: ['orange', 'grapes', 'watermelon']


#lab 17
'''
Create a function called `subtract` that takes two arguments and returns their difference. Call the function with the arguments 10 and 4, and print the result.'''


def subtract(a, b):
    return a - b
result = subtract(10, 4)
print(result)  


#lab 18
'''
Create a generator function called `even_numbers` that yields even numbers starting from 2 up to a given maximum number. Use a for loop to print the even numbers up to 10.'''
def even_numbers(max):
    for i in range(2, max+1, 2):
        yield i
for even in even_numbers(10):
    print(even)  # Should print 2, 4, 6, 8, 10


#lab 19
'''
Write a lambda function(square) that takes a single argument and returns its square. Use this lambda function to find the square of 7 and print the result.'''


square = lambda x: x**2
result = square(7)
print(result)



#lab 20
'''
Print the current working directory using `os.getcwd()`.'''
import os
print(os.getcwd())


#lab 21
'''List all files and directories in the current directory using `os.listdir()`.'''
import os
all_files = os.listdir()
print(all_files)


#lab 22
'''Create a new directory called `test_directory` using `os.mkdir()`.'''
import os
os.mkdir("test_directory")


#lab 23
'''Delete the file called `sample_file.txt` using `os.remove()`'''
import os
os.remove("sample_file.txt")


#lab 24
'''
Question 1: Handling File Not Found Error

Write a function load_file_content that takes a file path as input and returns the file content. If the file does not exist, return a user-friendly message.'''
def load_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


#lab 25
'''
Write a function perform_division that takes two numbers as input and returns their division. Handle the case where the denominator is zero.

You can also play around with the exception handling in the next code block as you wish.
'''
def perform_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
print(perform_division(10, 0))  # Division by zero is not allowed


#lab 26
'''
Write a function ask_for_integer that prompts the user for an integer input and handles invalid inputs by asking the user to try again.

'''

def ask_for_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please try again.")
ask_for_integer()


#lab 27
'''
Question 4: Handling Multiple Exceptions

Modify the function safe_divide to handle both ZeroDivisionError and TypeError. Ensure it provides meaningful error messages for each exception.'''

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Invalid input. Please enter a number"
print(safe_divide(10, 0))  # Division by zero is not allowed


