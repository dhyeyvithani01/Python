names=[]
# name = input("What's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for i in sorted(names):
    print(f"Hello, {i}")