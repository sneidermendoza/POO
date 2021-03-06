# Hacer una clase llamada Password que siga las siguientes condiciones:
# a. Que tenga los atributos longitud y contraseña. La longitud por
# defecto será de 8
# b. Crear un método que indique si la contraseña es fuerte teniendo en
# cuenta que es fuerte debe tener mínimo una longitud de 6.
# c. Mostrar
# d. Cambiar contraseña



class Password():
    def __init__(self, passphrase, longitud = 8):
        self.longitud = longitud
        self.passphrase = passphrase


    def es_fuerte(self):
       return len(self.passphrase) >= 6

    
    def mostrar(self):
       return self.passphrase


    def cambiar_passphrase(self, new_passphrase):
        self.passphrase = new_passphrase