# """Understanding paratmeters in bulit-in python functions"""

# print function
# sep="" is used for seperating objects and variable
# end="" is used for ending function with certain string
# print("Hello","Dhyey",sep="------",end="\n\n\n")
# print("Hello","Dhyey",sep="******",end="\n**\n")
# print("Hello","Dhyey",sep="______",end="\n\n")
# Removes the spaces from left and right side of string
# x = input("Enter the name:")
# x = x.strip()
# print(x)
# x = x.rstrip()
# print(x)
# x = x.lstrip()
# print(x)
# x = x.capitalize()
# print(x)
# x = x.title()
# print(x)
# x = x.lower()
# print(x)
# x = x.strip().title()
# print(x)
# f,l = x.split(" ")
# print(f)
# x = input("Enter the name:").strip().title()


"""Printing hello using def"""
# def main():
#     number=get_number()
#     hello(number)
# def get_number():
#     while True:
#         n=int(input("Enter the number:"))
#         if n>0:
#             return n
# def hello(n):
#     for i in range(n):
#         print("Hello")
# main()


"""printing column"""
# def main():
#     x=int(input("Enter the Height:"))
#     print_column(x)

# def print_column(Height):
#     for _ in range(Height):
#         print("#")

# main()

"""printing row"""
# def main():
#     x=int(input("Enter the length:"))
#     print_row(x)

# def print_row(length):
#     for _ in range(length):
#         print("#",end="")

# main()

"""printing square"""
# def main():
#     x=int(input("Enter the size:"))
#     print_square(x)
"""Def square"""
"""method-1"""
# def print_square(Size):
#     for i in range(Size):
#         for j in range(Size):
#             print("#  ",end="")
#         print()
"""method-2"""
# def print_square(Size):
#     for i in range(Size):
#         print("#  "*Size)


# main()


"""Error handling and Exceptions"""
try:
    x=int(input("What's X?"))
    print(f"x is {x}.")
except ValueError:
    print("Invalid input. Enter a valid integer.")
    