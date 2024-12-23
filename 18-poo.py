#paradigma de programacion: programar pensando en las cosas como objetos
#el constructor se llama __init__
#todas las funciones "metodos" incluida el constructor tienen como primer parametro el mismo y se debe poner siempre sino sera no definido
#convencion es usar self, como nombre para el mismo objeto

class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def greet(self):
        print(f'Hola {self.name} {self.lastname}, tienes {self.age} años')

# mario = Person(age=29, name='Mario', lastname='Arango')
mario = Person('Mario', 'Arango', 29)
mario.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder  = account_holder
        self.balance  = balance
        self.is_active  = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo actual {self.balance}')
        else:
            print(f'No se puede depositar, Cuenta inactiva')

    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Retiro {amount}, su saldo actual es {self.balance}')
            else:
                print(f'No puede retirar más de su saldo actual de {self.balance}')
        else:
            print(f'No se puede depositar, Cuenta inactiva')
    
    def active_account(self, state):
        self.is_active = state
        print(f'Su cuenta fue {'Activada' if state == True else 'Desactivada'}')

bank_account_mario = BankAccount('Mario', 1000)
bank_account_mario.deposit(100)
bank_account_mario.withdraw(500)
bank_account_mario.active_account(False)
bank_account_mario.deposit(100)
bank_account_mario.active_account(True)
bank_account_mario.deposit(120)
