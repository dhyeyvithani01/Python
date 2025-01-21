def main():
    Name = input("What's your name ?\n")
    print(hello(Name))

def hello(To="World"):
    return f"Hello,{To}"

if __name__ == "__main__":
    main()
    