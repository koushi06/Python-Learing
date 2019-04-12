
def sum_file(*b):

    c = 0
    for i in b:
        c = c + i

    return c
def sub_file(a,b):
    c = a-b
    return c
def main():
    sum_file()
    sub_file()
if __name__ == "__main__":
    main()