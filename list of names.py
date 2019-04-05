x= int(input("Enter the number of names: "))

lst = []
for i in range(x):
    i=input("Enter next name: ")
    lst.append(i)
print(lst)
def count(lst):
    more = 0
    less = 0
    for i in lst:
        if len(i)>=5:
            more+=1
        else:
            less+=1
    return more,less
more,less = count(lst)
print(more)
print(less)
