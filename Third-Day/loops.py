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
for i in range(1,10,2): #it will print 1,3,5,7,9 then how it works 1 is start,10 is stop and 2 is the difference or step value
    print(i)


#range(start, stop, step)


 # pass statement
for i in range(10):
    pass   

# WAP to find the sum of first n numbers. (using while)
n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum of first",n,"numbers is",sum)


# WAP to find the factorial of first n numbers. (using for)
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of",n,"is",fact)