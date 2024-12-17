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
            print("The {x} is dividable by {y}.") 
        else:
            print("The {x} is dividable by {y}.")
        a = int(input("Enter 0 to end program:\nEnter 1 to run again program:\n"))
    else:
        print("Program ended.")