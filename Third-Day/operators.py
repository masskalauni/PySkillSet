# a=input("Enter a number: ")
# b=input("Enter another number: ")
# if a>=b:
#     print(True)
# else:
#     print(False)


import sys
print(sys.platform) # print the platform of the system
x="spam"
print(x*8) # repeat the string 8 times
print(x+"eggs!") # concatenate the string with another string

# Data types
# int, float, string, boolean,none
# int
a=5
print(a)
print(type(a))

# float
b=5.0
print(b)
print(type(b))

# string
c="Hello"
print(c)
print(type(c))

# boolean
d=True
print(d)
print(type(d))

# none
e=None
print(e)
print(type(e))



# Operators
# Arithmetic operators
# +, -, *, /, %, **, //
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Comparison operators
# ==, !=, >, <, >=, <=
a=5
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Logical operators
# and, or, not
a=True
b=False
print(a and b) # if both are true then only true
print(a or b) # if any one is true then true
print(not a) # reverse the value


# Assignment operators
# =, +=, -=, *=, /=, %=, **=, //=
a=5
a+=2
print(a) # a=a+2
a-=2
print(a) # a=a-2
a*=2
print(a) # a=a*2
a/=2
print(a) # a=a/2
a%=2
print(a)    # a=a%2
a**=2
print(a) # a=a**2
a//=2
print(a) # a=a//2



#INPUT METHOD IN PYTHONS
a=input("Enter a number: ")
print(a)
# input()  it will take input from the user and store it in a variable

var=int(input("Enter a number: "))
print(type(var)) # it will convert the input to integer
var=float(input("Enter a number: "))
print(type(var)) # it will convert the input to float