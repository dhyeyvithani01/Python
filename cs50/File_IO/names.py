file=open("name.txt","w")
for _ in range(3):
    name = input("What's your name? ")
    file.write(name)
file.close()