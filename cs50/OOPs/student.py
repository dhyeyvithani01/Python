class Student:
    def __init__(self,name="jenish",area="varachcha"):
        self.name = name
        self.area = area

def main():
    student=get_student()
    print(f"{student.name} from {student.area}")
    
def get_student():
    name = input("Name : ")
    area = input("Area : ")
    return Student(name,area)

if __name__ == "__main__":
    main()