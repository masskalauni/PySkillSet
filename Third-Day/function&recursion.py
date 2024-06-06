#functions
'''function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. It can define by using def keyword and function name and parameters and the colon(:)'''
# def my_function():
#     print("Hello from a function")
def mY_function():
    print("Hello I am from a function")
mY_function()


def sum():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    sum=num1+num2
    print("The sum of ",num1,"and",num2 ,"is:",sum)
sum()    


def cal_avg(a,b,c):
     sum=a+b+c
     avg=sum/3
     print("The average of ",a,b,c,"is:",avg)
cal_avg(10,20,30)
