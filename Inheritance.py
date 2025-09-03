from PythonConcepts.BaseClass import Calculator1


class ChildClass(Calculator1):

    num2=60

    #create default constructor
    def __init__(self):
        Calculator1.__init__(self,2 ,10)
        print("Default constructor from ChildClass executed")

    def getDisplay(self):
        return ChildClass.num2+self.firstValue+self.secondValue



obj1=ChildClass()
print(obj1.getDisplay())