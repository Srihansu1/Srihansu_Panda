# Create a calculator using class that performs
class Calculator:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    def calculate(self):
        if self.operation =="addition":
            return self.a + self.b
        elif self.operation =="subtraction":
            return self.a - self.b
        elif self.operation =="multiply":
            return self.a * self.b
        elif self.operation =="divide":
            if self.b ==0:
                return "cannot divide by zero"
            else:
                return self.a/self.b
        else:
            return "Invalid operation"
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (addition/subtraction/multiply/divide): ")
calculation=Calculator(a,b,operation)
print(calculation.calculate())