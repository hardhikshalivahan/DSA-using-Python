# Basic Recursive Problems

#Print first n natural numbers
def har1(n):
    if n>0:
        har1(n-1)
        print(n,end=" ")
n=int(input("Enter the digit to print first n natural numbers: "))
har1(n)
print()


#Print first n natural numbers in reverse
def har2(n):
    if n>0:
        print(n,end=" ")
        har2(n-1)
n=int(input("Enter the digit to print first n natural numbers in reverse: "))
har2(n)
print()


#Print first n odd numbers
def har3(n):
    if n>0:
        har3(n-1)
        print(2*n-1,end=" ")
n=int(input("Enter the digit to print n odd numbers: "))
har3(n)
print()


#Print first n natural even numbers
def har4(n):
    if n>0:
        har4(n-1)
        print(2*n,end=" ")
n=int(input("Enter the digit to print n even numbers: "))
har4(n)
print()


#Print first n odd numbers in reverse
def har5(n):
    if n>0:
        print(2*n-1,end=" ")
        har5(n-1)
n=int(input("Enter the digit to print n odd numbers in reverse: "))
har5(n)
print()


#Print first n natural even numbers in reverse
def har6(n):
    if n>0:
        print(2*n,end=" ")
        har6(n-1)
n=int(input("Enter the digit to print n even numbers in reverse: "))
har6(n)
print()