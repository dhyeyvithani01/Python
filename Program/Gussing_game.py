# import random
# # x = random.randrange(1,100)
# # y = 0
# # a = 1
# # while a<=5:
# #     while y!=x and y<=100 and a<=5:
# #         y = int(input("Guess any number between 1 and 100:"))
# #         if y==x:
# #             print("Congratulations!!! You guessed the correct number.")
# #             break
# #         elif y>x and (y-x)>20:
# #             print("the number is too small.")
# #         elif y>x and (y-x)<=20:
# #             print("the number is small.")
# #         elif y<x and (y-x)>20:
# #             print("the number is too big.")
# #         elif y<x and (y-x)<=20:
# #             print("the number is big.")
# #         print(f"You have only {5-a} attemps left.")
# #         a+=1
# #     else:
# #         print("Enter the number between 1 and 100.")
# def Guessing_game():
#     #generating number between 1 and 100
#     x =random.randrange(1,100)
#     Max_attempts=10
#     y=0
#     a=0

#     print("Welcome to the Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     print(f"You have {Max_attempts} attempts to guess the number.")

    
#     while y!=x and y>=0 and y<=100 and a<=Max_attempts:
#         y = int(input("Guess the number:"))
#         if y>=0 and y<=100:
#             if y==x:
#                 print("Congratulations!!! You guessed the correct number.")
#                 break
#             elif y>x:
#                 if (y-x)>=20:
#                     print("The number is too small.")
#                 if (y-x)<20:
#                     print("The number is small.")
#                 if (y-x)<5:
#                     print("You're very close, within 5 numbers.")
#             elif y<x:
#                 if (x-y)>=20:
#                     print("The number is too big.")
#                 if (x-y)<20:
#                     print("The number is big.")
#                 if (x-y)<5:
#                     print("You're very close, within 5 numbers.")
#             a+=1
#             if a!=0:
#                 print(f"You have only {Max_attempts-a} attempts left.")
#             else:
#                 print(f"Sorry, you're out of attempts. The number was {y}.")
#         else:
#             print("Enter the number between 1 and 100.")
    


# Guessing_game()

"""Probabilty """
"""Program-1"""
# import random
# Data_size = int(input("Enter the datasize:"))
# a=0
# Heads = 0
# Tails = 0
# while a<=Data_size:
#     x=random.randint(1,2)
#     if x==1:
#         Heads+=1
#         print("Heads")
#     else:
#         Tails+=1
#         print("Tails")
#     a+=1
# print(f"Probabilty of Head is{Heads/(Heads+Tails)}")
# print(f"Probabilty of Tails is{Tails/(Heads+Tails)}")
"""Program-2"""
# import random
# Data_size = int(input("Enter the datasize:"))
# a=0
# num1=num2=num3=num4=num5=num6=num7=num8=num9=num10=0
# while a<=Data_size:
#     x=random.randint(1,10)
#     if x==1:
#         num1+=1
#     elif x==2:
#         num2+=1
#     elif x==3:
#         num3+=1
#     elif x==4:
#         num4+=1
#     elif x==5:
#         num5+=1
#     elif x==6:
#         num6+=1
#     elif x==7:
#         num7+=1
#     elif x==8:
#         num8+=1
#     elif x==9:
#         num9+=1
#     else:
#         num10+=1
#     a+=1
# print(f"Probability for each number is :\n1 : {num1/Data_size}\n2 : {num2/Data_size}\n3 : {num3/Data_size}\n4 : {num4/Data_size}\n5 : {num5/Data_size}\n6 : {num6/Data_size}\n7 : {num7/Data_size}\n8 : {num8/Data_size}\n9 : {num9/Data_size}\n10: {num10/Data_size}")
