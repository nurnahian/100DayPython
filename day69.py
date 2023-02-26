class Employee:
    company ="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(self, newcompany):
        self.company =newcompany


e1 = Employee()
e1.name = "Nahian"
e1.show()
print(Employee.company)
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
