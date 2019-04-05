from numpy import *
from array import *
arr = array('i',[])

n= int(input('enter the length of the array'))

for i in range(n):
    x= int(input("Enter the next value"))
    arr.append(x)
x= int(n/2)
print(arr)
for e in range(x):
    temp = arr[n-1-e]
    arr[n-1-e] = arr[e]
    arr[e]=temp
print(arr)