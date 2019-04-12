from files import sum_file, sub_file

def add():
    a=[]
    n=int(input("enter the length of the sum list "))
    for i in range(n):
        i= int(input("Enter the next number "))
        a.append(i)
    print("the sum is ",sum_file(*a))
def subt():
    a = int(input("enter a value "))
    b = int(input("Enter b value "))
    print("the sub is ",sub_file(a,b))
def main():
    func = input("Enter the function ")
    if func=='add':
        add()
    else:
        subt()

main()

