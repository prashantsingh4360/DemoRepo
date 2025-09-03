
class Calculator:

    num=100

    #create default constructor
    def __init__(self, a, b):
        print("Default constructor called")
        self.firstValue=a
        self.secondValue=b

    def GreetMe(self):
        print("Good Morning")

    def sum(self):
        return self.firstValue +self.secondValue+ Calculator.num
        #return self.firstValue + self.secondValue + self.num


#outside the class, create the object
obj=Calculator(5,6)       #create class object
obj.GreetMe()
print(obj.num)
print("Sum is ",obj.sum())
print(type(obj.sum()))

print("changes done for GIT")