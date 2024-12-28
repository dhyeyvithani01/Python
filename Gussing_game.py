import random
# x = random.randrange(1,100)
# y = 0
# a = 1
# while a<=5:
#     while y!=x and y<=100 and a<=5:
#         y = int(input("Guess any number between 1 and 100:"))
#         if y==x:
#             print("Congratulations!!! You guessed the correct number.")
#             break
#         elif y>x and (y-x)>20:
#             print("the number is too small.")
#         elif y>x and (y-x)<=20:
#             print("the number is small.")
#         elif y<x and (y-x)>20:
#             print("the number is too big.")
#         elif y<x and (y-x)<=20:
#             print("the number is big.")
#         print(f"You have only {5-a} attemps left.")
#         a+=1
#     else:
#         print("Enter the number between 1 and 100.")
def Guessing_game():
    #generating number between 1 and 100
    x =random.randrange(1,100)
