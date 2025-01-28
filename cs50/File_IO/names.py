names=[]
# name = input("What's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
"""method-1"""
# with open("names.txt","r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for i in sorted(names):
#     print(f"Hello, {i}")
"""method-2"""
with open("names.txt","r") as file:
    for line in sorted(file):
        print("Hello",line.rstrip())