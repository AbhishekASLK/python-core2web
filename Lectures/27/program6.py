class Company:

    def __init__(self,compName,compLoc):
        print("Constructor")
        self.compName=compName
        self.compLoc=compLoc

    def disp(self):
        print(self.compName)
        print(self.compLoc)

class Employee(Company):
    pass

obj1 = Employee("Google","Pune")
obj1.disp();
