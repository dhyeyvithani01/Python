with open("students.csv","r") as file:
    for line in sorted(file):
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
