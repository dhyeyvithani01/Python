class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self.house

    # Setter
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house

def main():
    student = get_student()
    student.house = "Privet Drive"
    print(student)

def get_student():
    name = input("Name: ") 
    house = input("House: ")  
    student = Student(name,house)
    return student

if __name__ == "__main__":
    main()
