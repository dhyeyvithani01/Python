# class Demo:

#     def config():
#         print("Hello my name")
#     config()

#     def dh():
#         print("dfghj")
#     dh()
# print(Demo)



# class Com:

#     def config(self):
#         print("Hello bro")

# Com1 = Com()
# Com2 = Com()

# # Com.config(Com1)
# # Com.config(Com2)

# Com1.config()

# class Addition:

#     A=2
#     B=1
#     def Sum(A,B):
#         print(A+B)
#     Sum(A,B)

# print(Addition)





# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute


# dog1 = Dog("Buddy", 3)

# print(dog1.name) 
# print(dog1.age)




hello = [1,2,3,4,5]
its = iter(hello)
print(next(its))
print(next(its))
print(its.__next__())
print(its.__next__())
print(its.__next__())