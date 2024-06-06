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
