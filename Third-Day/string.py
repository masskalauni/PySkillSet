string="mass kalauni"
string1='mass prem'
string2="""mass kalauni"""
# we have 3 ways to define string in python 
# The question is why we have 3 ways to define  string in python 
# The answer is if we have single line string we can use single quote or double quote
# if we have multiple line string we can use triple quote
# we can use single quote in double quote and double quote in single quote
# we can use single quote and double quote in triple quote
multiLine="""Hey guys it's me mass kalauni
.And I am a Developer"""
print(multiLine)

# Basic operations in string
# Concatenation
# Repetition
# Slicing
# Membership
# Indexing


# Concatenation
a="Hello"
b="World"
print(a+b)

# Repetition
a="Hello"
print(a*3)

# Slicing  a[start:end]
a="Hello"
print(a[0])
print(a[1])
print(a[2])
print(a[1:4])

# Membership
a="Hello"
print('H' in a)

# Indexing

a="Hello"
print(a[0])

# String methods (functions)
# len()
# lower()
# upper()
# title()
# strip()
# replace()

# len()
a="Hello"
print(len(a))

# lower()
a="Hello"
print(a.lower()) # small letter

#upper()
a="Hello"
print(a.upper()) # capital letter 

# title()
a="hello"
print(a.title()) # first letter capital


# strip()
a=" Hello "
print(a.strip()) # remove white space

# replace()
a="Hello"
print(a.replace('H','J')) # replace H with J



#capitalize()
var="prem praksah kalauni"
Capitilize=var.capitalize()
print(Capitilize)
print(var.title())