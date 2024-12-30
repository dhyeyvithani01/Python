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
    Max_attempts=10
    y=0
    a=0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {Max_attempts} attempts to guess the number.")

    
    while y!=x and y>=0 and y<=100 and a<=Max_attempts:
        y = int(input("Guess the number:"))
        if y>=0 and y<=100:
            if y==x:
                print("Congratulations!!! You guessed the correct number.")
                break
            elif y>x:
                if (y-x)>=20:
                    print("The number is too small.")
                if (y-x)<20:
                    print("The number is small.")
                if (y-x)<5:
                    print("You're very close, within 5 numbers.")
            elif y<x:
                if (x-y)>=20:
                    print("The number is too big.")
                if (x-y)<20:
                    print("The number is big.")
                if (x-y)<5:
                    print("You're very close, within 5 numbers.")
            a+=1
            if a!=0:
                print(f"You have only {Max_attempts-a} attempts left.")
            else:
                print(f"Sorry, you're out of attempts. The number was {y}.")
        else:
            print("Enter the number between 1 and 100.")
    


Guessing_game()