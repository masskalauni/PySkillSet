#loops
i=1
while i<=10:
    print("hello world",i)
    i=i+1

#practice print number from 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1

#practice print number from 100 to 1 
i=100
while i>=1:
    print(i)
    i+=-1

#print the multiplication of number n
'''number=int(input("Enter the number:"))
i=1
while i<=10:
    print(number,"*",i,"=",number*i)
    i+=1  '''   

#print the following elements using  while loops
'''
[1,4,9,16,25,36,49,64,81,100]
'''
list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1

#search for a number x in below list using loops
'''
[1,4,9,16,25,36,49,64,81,100]
'''   
list2=[1,4,9,16,25,36,49,64,81,100]
index=0
number=int(input("Enter the number to search:"))
while index<len(list2):
    if list2[index]==number:
        print("number found")
        break
    index+=1
else:
    print("number not found")

#print the following elements using  for loops
'''
[1,4,9,16,25,36,49,64,81,100]
'''
list_items=[1,4,9,16,25,36,49,64,81,100]
for item in list_items:
    print(item)

#search for a number x in below list using for loops
'''
[1,4,9,16,25,36,49,64,81,100]
'''   
listing_items=[1,4,9,16,25,36,49,64,81,100]
number=int(input("Enter the number to search:"))
for item in listing_items:
    if item==number:
        print("FOUND")
        break
else:
 print("NOT FOUND")



#range ()
for i in range(10):
    print(i)

 # pass statement
for i in range(10):
    pass   