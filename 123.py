print("Divisibility checker")
a = 1
while a!=0:
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    if x//y==x/y:
        print(f"{x} is dividable by {y}")
    else:
        print(f"{x} is not dividable by {y}")
    a = int(input("\nEnter 0 to end the program\nEnter 1 to run the program again:\n"))
else:
    print("program ended")
