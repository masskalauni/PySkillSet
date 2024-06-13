import numpy as np

# Create a 1D array
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("the array is :",arr)
print("the length is :",len(arr))
print("type is :",type(arr))



# Creating an array using arange()
import numpy as np
array = np.arange(1,11, 4)
print(array)


import numpy as np

p = np.zeros((3,3),dtype=np.int16)   # Create an array of all zeros
print("3*3 zero matrix:",p) 

q = np.ones((2,2))    # Create an array of all ones
print("2*2 matrix",q)

r = np.full((2,3), 4)  # Create a constant array
print(r) 

s = np.eye(4)         # Create a 2x2 identity matrix
print(s) 

t = np.random.random((3,3))  # Create an array filled with random values
print(t)

# Creating an array using arange()
import numpy as np
a = np.arange(1,11)
print(type(a))
print(a.dtype)

# Creating an array using linspace()
import numpy as np

# Generate an array of 10 evenly spaced values from 1 to 10
b = np.linspace(1, 10, 10)

# Print the array
print(b)
# Output: [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# Print the shape of the array
print(b.shape)
# Output: (10,)

# Print the data type of the array elements
print(b.dtype)
# Output: float64


import numpy as np
one_d = np.array([1,2,3,4,5])
print(one_d)

two_d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d)


import numpy as np

# Create a 1D array using random function
one_d = np.random.randint(5,size=2)
print(one_d)


import numpy as np
array=np.linspace(4,9,10)
print(array)


list=[1,2,3,4,5,6,7,8,9,10]
print(list)
#i want to generate 1 3 5 7 9 suliscing slicing concept
print(list[0:10:2])
#max value in the list
print(max(list))


two_d=np.random.randint(18,size=(5,3))
print(two_d)

#print 10 on the screen
print(two_d[1,1])

#i want only 2 row and 3 row
print(two_d[1:3,:])
#another mwthod
print(two_d[1:3])


# make two array and perform addition
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
sum=np.add(a,b)
sub=np.subtract(a,b)
mul=np.multiply(a,b)
div=np.divide(a,b)
print(sub)
print(sum)
print(mul)
print(div)


#classs
class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b!=0:
            return a/b
        else:
            return "division is not possible"
        

if __name__=="__main__":
    c=calculator()
    print(c.add(10,20))
    print(c.sub(10,20))
    print(c.mul(10,20))
    print(c.div(10,20))
    print(c.div(10,0))
       