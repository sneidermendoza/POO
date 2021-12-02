# Crear una clase Cuenta con atributos para el número de cuenta (, el
# número de identificación del cliente, el saldo actual y el interes anual que se
# aplica a la cuenta. Define en la clase los siguientes métodos:
# a. ActualizarSaldo(): actualizará el saldo de la cuenta aplicándole el
# interés diario (interes anual dividido entre 365 aplicado al saldo
# actual)
# b. Ingresar: permitirá ingresar una cantidad en la cuenta
# c. Retirar: permitirá sacar una cantidad de la cuenta siempre y cuando
# haya saldo.
# d. Mostrar: método que permita mostrar todos los datos de la cuenta


class Account():
    def __init__(self, account_number, id, balance, anual_interest):
        self.account_number =account_number
        self.id = id
        self.balance = balance
        self.anual_interest = anual_interest


    def update_balance(self):
        self.balance += (self.balance * (self.anual_interest / (365 * 100)))


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance > 0:
           self.balance -= amount


    def display(self):
        return (f"Account Number: {self.account_number} \nId: {self.id} \nbalance: {round(self.balance)} \nAnual Interest: {round(self.anual_interest)}")


gabo = Account(12345, 6789, 10000, 10)

print(gabo.display())

gabo.update_balance()

print(round(gabo.balance, 2))






