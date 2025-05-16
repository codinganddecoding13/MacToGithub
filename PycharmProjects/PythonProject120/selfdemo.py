class ProgStaff:
    companyName = 'ProgrammingLab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print("Company name is", ProgStaff.companyName)
        print("Salary is", self.salary)

peter = ProgStaff(2500)
john = ProgStaff(2500)
ProgStaff.companyName = 'ProgrammingSchool'
print(peter.companyName)
print(john.companyName)
#left off at the beginning of page 92 after getting the correct output
