class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student=get_student()
    print(Student)
    
def get_student():
    name = input("Name : ")
    house = input("House : ")
    Student(name,house)
    return student

if __name__ == "__main__":
    main()