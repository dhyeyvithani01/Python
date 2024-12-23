# count = 0
# while (count > -1):
#     count = count + 1
#     print(count)

# for loop 
# x = 4
# for x in range(75):
#     if x<18:
#         print("Children")
#         continue
#     elif 19<x<36:
#         print("mrg")
#         continue
#     elif 37<x<58:
#         print("job")
#         continue
#     elif 59<x<65:
#         print("goa")
#         continue
#     elif 66<x<73:
#         print("temple")
#         continue
#     elif x>73:
#         print("death")


    
# print("\nDictionary Iteration")
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
 
""""odd-even"""
# x = int(input("Enter any number:"))
# for x in range(x):
#     if x%2==0:
#         print("The",x,"is Even.")
#     else:
#         print("The",x,"is Odd.")


# x = 10

# for i in range(0,10,3):
#     print(i)

# a = input("enter you name:")
# for x in a:
#     if x!=" ":
#         print(x,end="")
#     else:
#         break

    
# print("hello")
# for x in range(24,0,-2):
#     if x==16:
#         continue
#     elif x==4:
#         print(x)
#     elif x == 2:
#         pass
#     print(x)



# for x in range(1,20):
#     if x == 10:
#         continue
#     elif x == 14:
#         break
#     print(x)

"""while loop"""
# x = 1
# while x<=10:
#     print(x)
#     x+=1


""""odd even in while loop"""
# x = 1
# while x<11:
#     if x%2==0:
#         print(f"the {x} is even.")
#     else:
#         print(f"the {x} is odd.")
#     x+=1


"""check prime in while loop"""
# for i in range(1,10):
#     pass

# x = [1,2,[3,4,5,[6,7],8,9],10,11,12]
# print(x[2][3][0])

"""print banana in row"""
# for x in "banana":
#     print(x)    

# x=0
# while x < len("banana"):
#     print("banana"[x])
#     x+=1

"""printing adj and fruits using nested for loop"""
# adj = ["red","big","tasty"]
# fruits = ["apple","banana","cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)

"""Phibonachi sequence"""
# a=0
# b=1
# while a<35:
#     print(a)
#     a,b = b,a+b

# a, b = 0, 1
# n = int(input("enter the number: "))
# for i in range(n):
#     print(a)
#     a, b = b, a + b


"""printing 1 to 20 using while loop, continue and break """
# i=0
# while i<8:
#     print(i)
#     i+=1
#     if i==5:
#         continue
# j=8
# while j==8:
#     break
# k=9
# while 8<k<15:
#     print(k)
#     k+=1
# a=15
# while a==15:
#     break
# b=16
# while 15<b<=20:
#     print(b)
#     b+=1

# x = (input("Enter your mobile number:"))
# if (len(x)==10 and x.isdigit()):
#     print(f"Your mobile number is {x}.")
# else:
#     print("Enter a valid mobile number.")

"""factorial program in for loop"""
# def factorial():
#     x=int(input("Enter the number:"))
#     for i in range(1,x):
#         x=x*i
#     print(x)
# factorial()

"""factorial program in while loop"""
# def fact():
#     x=int(input("Enter the number:"))
#     result=1
#     i=1
#     while i<=x:
#         result=result*i
#         i+=1
#     print(result)
# fact()

"""printing stars"""
# x=int(input("enter the number:"))
# for i in range(x):
#     for a in range(i):
#         print("*")

"""printing patterns"""
"""patterns-1"""
# x = int( input("Enter Row Number: ") )
# for i in range(1, x+1):
#     print( "*"*i )
"""patterns-2"""
# x = int( input("Enter Row Number: ") )
# for i in range(x,0,-1):
#     print( "*"*i )
"""patterns-3"""
# x = int( input("Enter Row Number: ") )
# num=1
# for i in range(1, x+1):
#     print(f"{num}"*i )
#     num+=1
"""patterns-4"""
# x = int( input("Enter Row Number: ") )
# num=x
# for i in range(x,0,-1):
#     print(f"{num}"*i )
#     num-=1
"""patterns-5"""
# x = int(input("Enter the number:"))
# for i in range(1,x+1):
#     print(chr(64+i)*(i))
"""patterns-6"""
# x = int(input("Enter the number:"))
# for i in range(x,0,-1):
#     print(chr(64+i)*(i))
"""patterns-7"""
# x = int(input("Enter the number:"))
# for i in range(x,0,-1):
#     print("5"*i)
"""patterns-8"""
# x =int(input("Enter the number:"))
# for i in range(1,x+1):
#     for a in range(1,i+1):
#         print(f"{a}",end="")
#     print()
"""pattern-9"""
# x =int(input("Enter the number:"))
# for i in range(x,0,-1):
#     for a in range(1,i+1):
#         print(f"{a}",end="")
#     print()
"""Pattern-10"""
# x =int(input("Enter the number:"))
# for i in range(1,x+1):
#     print(" "*(x-i)+"*"*i)
"""pattern-11"""
# x =int(input("Enter the number:"))
# for i in range(x,0,-1):
#     print(" "*(x-i)+"*"*i)
"""pattern-12"""
# x =int(input("Enter the number:"))
# for i in range(1,x+1):
#     print(" "*(x-i),end="")
#     for a in range(1,i+1):
#         print(f"{a}",end=" "*1)
#     print()
"""pattern-13"""
# x =int(input("Enter the number:"))
# for i in range(x,0,-1):
#     print(" "*(x-i),end="")
#     for a in range(1,i+1):
#         print(f"{a}",end=" "*1)
#     print()
"""pattern-14"""
# x =int(input("Enter the number:"))
# for i in range(1,x+1):
#     for a in range(i,0,-1):
#         print(f"{a}",end="")
#     print()
"""pattern-15"""
# x=int(input("Enter the number:"))
# for i in range(1,x+1):
#     print(" "*(x-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
"""pattern-16"""
# x=int(input("Enter the number:"))
# for i in range(x,0,-1):
#     print(" "*(x-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
"""pattern-17"""
x=int(input("Enter the number:"))
j=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
        j+=1
    print()
