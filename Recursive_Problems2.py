# Basic Recursive Problems

# To print sum of first n Natural Numbers
def el1(n):
    if n==0:
        return 0
    return el1(n-1)+n
n=int(input("Enter a Number to print sum of first n Natural Numbers : "))
print(el1(n))
print()


# To print sum of first n odd Numbers
def el2(n):
    if n==1:
        return 1
    return 2*n-1+el2(n-1)
n=int(input("Enter a Number to print sum of first n odd Numbers : "))
print(el2(n))
print()


# To print sum of first n even Numbers
def el3(n):
    if n==0:
        return 0
    return 2*n+el3(n-1)
n=int(input("Enter a Number To print sum of first n even Numbers : "))
print(el3(n))
print()


# To print Factorial Number
def el4(n):
    if n==1:
        return 1
    return n*el4(n-1)
n=int(input("Enter a Number to print Factorial Number : "))
print(f"Factorial Number of {n} is: {el4(n)}")
print()


# To print sum of square Numbers
def el5(n):
    if n==1:
        return 1
    return n**2+el5(n-1)
n=int(input("Enter a Number to print sum of square Numbers : "))
print(f"Sum of {n} Square Numbers is: {el5(n)}")
print()