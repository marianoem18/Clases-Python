class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.isActive = True


    def deposit(self, amount):
        if self.isActive:
            self.balance += amount  
            print(f"Se ha depositado: {amount}. El saldo es:  {self.balance}")
        else:
            print("La cuenta está inactiva. No se pueden hacer depósitos.")    


    def retirar(self, amount):
        if self.isActive:
            if amount <= self.balance:
                self.balance -= amount  # self.balance = self.balance - amount
                print(f"Se ha retirado: {amount}. El saldo es: {self.balance}")
            else:
                print("Fondos insuficientes para retirar.")
        else:
            print("La cuenta está inactiva. No se pueden hacer retiros.")      


    def desactivar_cuenta(self):
        self.isActive = False
        print("La cuenta ha sido desactivada.") 

    def activar_cuenta(self):
        self.isActive = True
        print("La cuenta ha sido activada.")             


cuenta1 = BankAccount("1", 1000) 
cuenta2 = BankAccount("2", 500)

print(type(cuenta1))
