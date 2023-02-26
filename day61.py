class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"The name of Employee:{self.id} is {self.name}")

class Programmer(Employee):
    def showItem(self):
        print("this is Inheritance ")

e1 = Employee("Rohan",400)
e1.showDetails()
e2 = Programmer("Nur",14)
e2.showDetails()
e2.showItem()