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

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)