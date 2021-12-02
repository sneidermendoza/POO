# Programe una clase que permita crear un número complejo y realizar las
# siguientes operaciones:
# a. Sumar
# b. Restar
# c. Multiplicar


class ComplexNumber():
    def __init__(self, n1, n2 ):
        self.n1 = n1
        self.n2 = n2


    def sum(self, other_n):
        a = self.n1 + other_n.n1
        b = self.n2 + other_n.n2
        return ComplexNumber(a, b)


    def subtraction(self, other_n):
        a = self.n1 - other_n.n1
        b = self.n2 - other_n.n2
        return ComplexNumber(a, b)


    def multiplication(self, other_n):
        a = self.n1 * other_n.n1
        b = self.n1 * other_n.n2
        c = self.n2 * other_n.n1
        d = self.n2 * other_n.n2
        e = a - d
        f = b + c
        return ComplexNumber(e, f)
    
        
 
    def display(self):
        return f"{self.n1} + {self.n2}i"

    
c1 = ComplexNumber(2,3)

c2 = ComplexNumber(5, 8)

result = c1.sum(c2)
print(result.display())

result_2 = c1.subtraction(c2)
print(result_2.display())

result_3 = c1.multiplication(c2)
print(result_3.display())

