
from array import *
arr = array('i',[])

n= int(input('enter the length of the array'))

for i in range(n):
    x= int(input("Enter the next value"))
    arr.append(x)

print(arr)
val = int(input("Enter the value for searching"))
k=0
for a in arr:
    if a==val:
        print("the index value is ",k)
        break
    k=k+1

print(arr.index(val))