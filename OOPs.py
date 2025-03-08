# class Demo:

#     # def config():
#     #     print("Hello my name")
#     # config()

#     def dhyey():
#         return "Hello, dhyey" 
#     print(dhyey())
# Demo()



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




# hello = [1,2,3,4,5]
# its = iter(hello)
# print(next(its))
# print(next(its))
# print(its.__next__())
# print(its.__next__())
# print(its.__next__())



"""inheritence"""

# Single Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# # Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name}Guides the way!")

# # # Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()

# guide_dog = GuideDog("Max")
# guide_dog.display_name()
# guide_dog.guide()

# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()



"""polymorphism"""




# # Parent Class
# class Dog:
#     def sound(self):
#         print("dog sound")  # Default implementation

# # Run-Time Polymorphism: Method Overriding
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")  # Overriding parent method

# class Beagle(Dog):
#     def sound(self):
#         print("Beagle Barks")  # Overriding parent method

# # Compile-Time Polymorphism: Method Overloading Mimic
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c  # Supports multiple ways to call add()

# # Run-Time Polymorphism
# dogs = [Dog(), Labrador(), Beagle()]
# for dog in dogs:
#     dog.sound()  # Calls the appropriate method based on the object type


# # Compile-Time Polymorphism (Mimicked using default arguments)
# calc = Calculator()
# print(calc.add(5, 10))  # Two arguments
# print(calc.add(5, 10, 15))  # Three arguments





"""Encapsulation"""
