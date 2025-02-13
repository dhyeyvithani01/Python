students=[]

# with open("students.csv","r") as file:
#     for line in file:
#         name,house,home = line.rstrip().split(",")
#         student ={"name":name,"house":house,"home":home}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students,key=get_house,reverse=True): #here 'get house' is used without paranthesis because get_house is passed in sorted function
#     print(f"{student['name']} is in {student['house']}")


"""method-2 for sorting using lambda function"""

for student in sorted(students,key=lambda student : student["name","home"]):
    print(f"{student['name']} is in {student['house']}")


import csv

with open("students.csv","r") as file:
    reader = csv.reader(file)
    """method-1"""
    # for row in reader:
    #     students.append({"name":row[0],"house":row[1],"home":row[2]})
    """method-2"""
    for name,house,home in reader:
        students.append({"name":name,"house":house,"home":home})

for student in sorted(students,key=lambda student : student["name"]):
    if student['home']!='Unknown':
        print(f"{student['name']} is in {student['house']} and {student['name']} lives in {student['home']}")
    else:
        print(f"{student['name']} is in {student['house']} and information about {student['name']}'s home is Unknown.")