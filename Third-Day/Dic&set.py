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
