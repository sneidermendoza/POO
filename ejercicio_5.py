# Crear una clase Cafetera con los atributos capaciadadMaxima (la cantidad
# máxima de café que puede contener la cafetera) y _cantidadActual( la
# cantidad actual de café que hay en la cafetera). Esta debe realizar los
# siguientes métodos:
# a. Contructor predeterminado: establece la capacidad máxima en 1000
# y la actual en cero.
# b. Constructor con la capacidad máxima y la cantidad actual: si la
# cantidad actual es mayor que la capacidad máxima de la cafetera, la
# ajustará al máximo.
# c. Llenar la cafetera: pues eso, hace que la cantidad actual sea igual a
# la capacidad.
# d. ServirTaza: simula la acción de servir una taza con la capacidad
# indicada. Si la cantidad actual de café “no alcanza” para llenar la
# taza, se sirve lo que quede.
# e. Vaciar la cafetera: pone la cantidad de café actual en cero.
# f. Agregar Café: añade a la cafetera la cantidad de café indicada.

class CoffeeMaker():
    def __init__(self):
        self.current_amount = 0
        self.max_capacity = 1000
    
    def get_max_capacity(self):
        return self.max_capacity


    def get_current_amount(self):
        return self.current_amount


    def current_volume(self, current_volume):
        self.current_amount = current_volume
        if self.current_amount > self.max_capacity:
            self.current_amount = self.max_capacity
        return self.current_amount

    
    def fill_coffeemaker(self):
        self.current_amount = self.max_capacity
        return self.current_amount
        



cafetera = CoffeeMaker()
print(cafetera.fill_coffeemaker())









    

