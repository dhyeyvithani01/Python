# A simple Python function
# def odd_even():
#     number = int(input("Enter any number:"))
#     if number%2==0:
#         print("The given number is Even.")
#     else:
#         print("The given number is Odd.")



# # Driver code to call a function
# odd_even()



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
    marks = int(input("Enter your marks:"))
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












A=int(input("print 1 to run Divisibilty_Check() program.\nprint 2 to run Result() program:\n"))
if A == 1:
    Divisibilty_Check()
elif A==2:
    Result()