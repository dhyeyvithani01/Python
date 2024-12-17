# def hello(x):
#     print('hello world')
#     print(x)

# # inbilt function 
# print('hello')
# hello(10)

"""Divisibility Checker"""
def Divisibilty_Check():
    a=1
    while a!=0:
        x = int(input("Enter a first number:"))
        y = int(input("Enter a second number:"))
        if x//y == x/y:
            print(f"The {x} is dividable by {y}.") 
        else:
            print(f"The {x} is not dividable by {y}.")
        a = int(input("Enter 0 to end program:\nEnter 1 to run again program:\n"))
    else:
        print("Program ended.")

"""marks to grade converter"""
def Result():
    marks = float(input("Enter your marks:"))
    if 100<marks:
        print("Enter marks between 0 and 100")
    elif 100>=marks>80:
        print("A")
    elif marks>60:
        print("B")
    elif marks>40:
        print("C")
    elif marks>=35:
        print("D")
    elif 0<=marks<35:
        print("F")
    elif marks<0:
        print("Enter marks between 0 and 100")

"""Comparing values"""
def Compare_value():
    a = float(input("Enter the value of A:"))
    b = float(input("Enter the value of B:"))
    print("A is equal to B" if a==b else "A is greater than B"if a>b else "B is greater than A")

"""Odd even"""
def odd_even():
    number = int(input("Enter any number:"))
    if number%2==0:
        print("The given number is Even.")
    else:
        print("The given number is Odd.")

"""Phibonachi sequence"""
def Phibonachi():
    a, b = 0, 1
    n = int(input("enter the number: "))
    for i in range(n):
        print(a)
        a, b = b, a + b

A=int(input("print 1 to run Divisibilty_Check() program.\nprint 2 to run Result() program.\nprint 3 to run Compare_value().\nprint 4 to run odd_even() program.\nprint 5 to Phibonachi() program.:\n"))
if A == 1:
    Divisibilty_Check()
elif A==2:
    Result()
elif A==3:
    Compare_value()
elif A==4:
    odd_even()
elif A==5:
    Phibonachi()