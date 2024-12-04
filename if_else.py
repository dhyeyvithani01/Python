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

# """nested if else"""
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

"""ternary if else"""
# a,b = int(input())
# print(a,b)
a = float(input("Enter the value of A:"))
b = float(input("Enter the value of B:"))
print("A is equal to B" if a==b else "A is greater than B"if a>b else "B is greater than A")