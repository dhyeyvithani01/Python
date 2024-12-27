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
        a = int(input("\nEnter 0 to end program:\nEnter 1 to run again program:\n"))
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

# A=int(input("print 1 to run Divisibilty_Check() program.\nprint 2 to run Result() program.\nprint 3 to run Compare_value().\nprint 4 to run odd_even() program.\nprint 5 to Phibonachi() program.:\n"))
# if A == 1:
#     Divisibilty_Check()
# elif A==2:
#     Result()
# elif A==3:
#     Compare_value()
# elif A==4:
#     odd_even()
# elif A==5:
#     Phibonachi()


# num =5
# def hellos():
#     print(num)
    
# hellos()
# print(num)

# x = [1,2,-1,-4,6.5,-23,-2.3]
# for i in x:
#     if i<0:
#         print(i)

# name = ["jay","jay shah","patel jay"]
# for i in name:
#     if len(i)==3:
#         print(i)

# """is_prime()"""
# def is_prime(n):
#     if n in [2, 3]:
#         return True
#     if (n == 1) or (n % 2 == 0):
#         return False
#     r = 3
#     while r * r <= n:
#         if n % r == 0:
#             return False
#         r += 2
#     return True
# n=int(input("Enter any number to if it is prime or not:"))
# print(is_prime(n))


"""*args for variable number of arguments"""
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


"""lamba function"""
# x = lambda y:(y*2,y+4,y%4)
# print(x(20))


# Kdot = lambda x,b,c,d:(x+b,x-c,x**d,c//d,b/x,d*b)
# print(Kdot(5,6,7,8))

# x = lambda a,b,c,d:(a+1,b+c*a,b%d,a-c)
# print(x(4,56,23,12))


# def myfunctionb(shanu,virani):
#     return lambda s:(s*shanu,s+virani)
# TG = myfunctionb(10,9)
# print(TG(115))

# def myfunc(x,y):
#     return lambda fun_1 :(fun_1*x,fun_1/y)
# Object_1 = myfunc(2,3)
# print(Object_1(10))



# def mydata(Djengo,panda,syntex):
#     return lambda y,h,c: (Djengo+y, panda*h, syntex-c)
# hii = mydata(1.2,1.3,1.4)
# TG = mydata(1,2,3)
# print(TG(1.2,1.3,1.4))
# print(hii(20,30,40))





#array

# import array

# from array import *


# value = array('i',[1,2,3,4,5,6,7])

# print(value)


# print(value.buffer_info())
# print(value.typecode)


# print(value[3])


# def is_palindrome(s):
#     s = s.lower()
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome!')
# else:
#     print(f'"{input_string}" is not a palindrome.')

"""KBC"""


qestions = [
  [
    "Which language was used to create fb?", "Python","none", "French", "JavaScript","d"
  ],
  [
    "India Prime minister name?", "Modi", "Rahul", "none","Jay","d"
  ],
  [
    "Surat kesa city he", "Smart", "Cleane", "Green","none","a"
  ],
  [
    "Apdi Company kevi che?", "Gosod", "V.Good", "Bed","none","c"
  ],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,3200000]
money = 0

for i in range(0,len(qestions)):
  qestion = qestions[i]
  print(f"Qestions for Rs.{levels[i]} is {qestions[i][0]}")
  print(f"a. {qestions[i][1]}      b.{qestions[i][2]}")
  print(f"c. {qestions[i][3]}      d.{qestions[i][4]}")

  reply = str(input("Enter your answer:"))
  if(reply == qestions[i][5]):
    print(f"Correct answear, you have win Rs.{levels[i]}")
    
  else:
    print("Wrong answer!")
    break