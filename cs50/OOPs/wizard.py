class Wizard:
    def __init__(self,name):
        if not name:
            raise ValuError("Missing name")
        self.name = name
    
    def __str__(self):
        return self.name

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
        
class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self):
        return f"{self.name} from {self.subject}"

wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defence against Dark Art")
print(student,professor,wizard)