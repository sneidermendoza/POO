# Programe un clase que permite crear un número Fraccionario y realizar las
# siguiente operaciones:
# a. Sumar
# b. Restar
# c. Multiplicación
# d. División


class Fraction():
    def __init__(self, numerator, denominator):

        self.numerator = numerator
        self.denominator = denominator
    
    def sum(self, other_fraction):
       a = self.numerator * other_fraction.denominator
       b = self.denominator * other_fraction.numerator
       c = self.denominator * other_fraction.denominator
       d = a + b
       return Fraction(d, c)
    
    def subtration(self, other_fraction):
       a = self.numerator * other_fraction.denominator
       b = self.denominator * other_fraction.numerator
       c = self.denominator * other_fraction.denominator
       d = a - b 
       return Fraction(d, c)

    def multiplication(self, other_fraction):
        a = self.numerator * other_fraction.numerator
        b = self.denominator * other_fraction.denominator
        return Fraction(a, b)

    def division(self, other_fraction):
        a = self.numerator * other_fraction.denominator
        b = self.denominator * other_fraction.numerator
        return Fraction(a, b)
    
    def display(self):
        return f"{self.numerator}/{self.denominator}"
        

f1 = Fraction(2, 3)
print(f1.display())
f2 = Fraction(9, 5)
print(f2.display())

result = f1.sum(f2)
print(result.display())

result_2 = f1.subtration(f2)
print(result_2.display())

result_3 = f1.multiplication(f2)
print(result_3.display())

result_4 = f1.division(f2)
print(result_4.display())




