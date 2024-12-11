"""if elif-else conditional statments"""
# if 5<3:
#     print("right")
# elif 10>45:
#     print("rightt")
# elif 5==23:
#     print("dfghjk")
# elif 5!=5:
#     print("qwtyui")
# else:
#     print("wrong")

# <,>,==,!=,<=,>=

# print("grade:")
# x = 93.50
# if x==0:
#     print('Enter Valid marks')
# elif x>=90:
#     print('A1')
# elif x>80:
#     print('A')
# elif x>60:
#     print('B')
# elif x>35:
#     print('C')
# else:
#     print('F')

"""nested if else"""
# grade = float(input("enter your grade:"))
# if grade > 80:
#     print("A")
# else:
#     if grade > 60:
#         print("B")
#     else:
#         if grade > 40:
#             print("C")
#         else:
#             print("Fail")


# x = int(input('enter the age:'))
# if 1<=x<18:
#     print("Children")
# elif 18<=x<36:
#     print("Mrg")
# elif 36<=x<58:
#     print("kam")
# elif 58<=x<65:
#     print("goa")
# elif 65<=x<73:
#     print("temple")
# elif x>=73:
#     print("Death")

"""ternary if else"""
# # a,b = int(input())
# # print(a,b)
# a = float(input("Enter the value of A:"))
# b = float(input("Enter the value of B:"))
# print("A is equal to B" if a==b else "A is greater than B"if a>b else "B is greater than A")

""""odd-even"""
# x = int(input("Enter any number:"))
# if x%2==0:
#     print("The given number is Even.")
# else:
#     print("The given number is Odd.")

"""revere"""
x = 'my class name is transglobe multimedia education campus'
print(x[0:2],x[7:2:-1]+x[8:13],x[15:13:-1]+x[16:27],x[37:27:-1]+x[38:48],x[54:48:-1])