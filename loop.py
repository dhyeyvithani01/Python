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


""""odd-even"""
x = int(input("Enter any number:"))
for x in range(x):
    if x%2==0:
        print("The",x,"is Even.")
    else:
        print("The",x,"is Odd.")