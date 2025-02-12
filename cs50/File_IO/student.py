students=[]

with open("students.csv","r") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student ={"name":name,"house":house}
        students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students,key=get_house,reverse=True): #here 'get house' is used without paranthesis because get_house is passed in sorted function
#     print(f"{student['name']} is in {student['house']}")


"""method-2 for sorting using lambda function"""

for student in sorted(students,key=lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")