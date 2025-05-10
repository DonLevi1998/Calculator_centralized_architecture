class Calculator:
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division (self, a, b):
        if b == 0:
            raise ValueError("Cannot be divided by zero")
        return a / b

calc = Calculator()
print("5 + 3 =", calc.addition(5, 3))
print("10 / 2 =", calc.division (10, 2))