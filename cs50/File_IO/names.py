name = input("What's your name? ")
with open("names.txt","a") as file:
    file.write(f"{name}\n")
with open("names.txt","r") as file:
    lines = file.readlines()
for line in lines:
    print("Hello",line.rstrip())