def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
x=5
f = fact(x)
print(f)