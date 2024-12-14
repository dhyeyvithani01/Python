print("Divisibility checker")
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
while x>0 and y>0:
        if x//y==x/y:
            print(f"{x} is dividable by {y}")
        else:
            print(f"{x} is not dividable by {y}")
        break
else:
    print("Enter a positive integer!")