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
# def main():
#     y = get_int("What's X? ")
#     print(f"X is {y}")

# def get_int(prompt):
# # Case 1:you can tighten up you're code like this
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Enter a valid integer.")   # you can also useuse pass instead of printing this statement
#             #pass
# # Case 2:you can also this code to under stand the code well
#     # while True:
#     #     try:
#     #         x=int(input("What's X? "))
#     #     except ValueError:
#     #         print("Invalid input. Enter a valid integer.")
#     #     else:
#     #         return x   #return is used to return value and also to break the program.
    
# main()

"""Libraries"""
"""Random"""
# import random
# population = ["cat","dog","lion"]
# population_1 = ["cat","dog","lion"]
# W=[3,6,9]
# print(random.choices(population,weights=W,k=9))
# print(random.choices(population_1,cum_weights=W,k=9))
# y=["A","B","C","D","E","F","G"]
# random.shuffle(y)
# for i in y:
#     print(i)
"""statistics"""
# import statistics
# print(statistics.mean([1,2,3,4,5]))
# print(statistics.fmean([2.5,3.0,7.0,18.0]))
# print(statistics.median([1,4,666,7,9]))
"""Sys"""
import sys
"""1"""
# try:
#     print("my name is",sys.argv[1])
# except IndexError:
#     if len(sys.argv)<2:
#         print("too few arguments!!")
#     elif len(sys.argv)>2:
#         print("Too many arguments!!")
"""1"""
# if len(sys.argv)<2:
#     sys.exit("too few arguments!!")
# elif len(sys.argv)>2:
#     sys.exit("Too many arguments!!")
# print("my name is",sys.argv[1])

# for args in sys.argv[1:]:# here "1:" is used to start the loop from index 1
#     print("My name is",args)

"""Cowsay"""
# import cowsay
# import sys
# """printing cow using ASCII art"""
# cowsay.cow("hello")

# """printing trex using ASCII art"""
# if len(sys.argv)==2:
#     cowsay.trex("hello "+ sys.argv[1])

# """printing penguin using ASCII art"""
# cowsay.tux("I am Tux the penguin!")

"""Turtle"""
"""1"""
##import package
# import turtle
# # loop for pattern
# for i in range(4):
# # motion
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(20)
#     turtle.right(90)
#     turtle.forward(100)
# # set the y coordinate 
#     turtle.up()
#     turtle.sety(-40*(i+1))
#     turtle.down()
# # change the direction
#     turtle.left(180)

"""2"""
# #import package
# import turtle
# # loop for pattern 
# for i in range(50): 
# # set turtle speed 
#     turtle.speed(50-i) 
# # motion for pattern 
#     turtle.forward(50+10*i) 
#     turtle.right(90)
"""3"""
# # import package and making object
# import turtle
# screen = turtle.Screen()

# # method to draw ellipse
# def draw(rad):
	
# # rad --> radius for arc
# 	for i in range(2):
# 		turtle.circle(rad,90)
# 		turtle.circle(rad//2,90)

# # Main Section 
# # Set screen size
# screen.setup(500,500)

# # Set screen color
# screen.bgcolor('black')

# # Colors
# col=['violet','blue','green','yellow',
# 	'orange','red']

# # some integers
# val=10
# ind=0

# # turtle speed
# turtle.speed(10)

# # loop for multiple ellipse
# for i in range(36):
	
# 	# oriented the ellipse at angle = -val
# 	turtle.seth(-val)
	
# 	# color of ellipse
# 	turtle.color(col[ind])
	
# 	# to access different color
# 	if ind==5:
# 		ind=0
# 	else:
# 		ind+=1
	
# 	# calling method
# 	draw(80)
	
# 	# orientation change
# 	val+=10

# # for hiding the turtle
# turtle.hideturtle()

"""4"""
# # import the time module 
# import time 

# # define the countdown func. 
# def countdown(t): 
	
# 	while t: 
# 		mins, secs = divmod(t, 60) 
# 		timer = '{:02d}:{:02d}'.format(mins, secs) 
# 		print(timer, end="\r") 
# 		time.sleep(1) 
# 		t -= 1
	
# 	print('Fire in the hole!!') 


# # input time in seconds 
# t = input("Enter the time in seconds: ") 

# # function call 
# countdown(int(t)) 

"""requests"""
# import json
# import requests
# import sys

# if len(sys.argv)!=2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
# print(json.dumps(response.json(),indent=2))

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
# o=response.json()
# for result in o["results"]:
#     print(result["trackName"],result["artistName"],result["trackId"])