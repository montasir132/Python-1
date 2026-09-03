class AB_bank_bd:
    def __init__(self):
        self.__balance = 5000000
    def show(self):
        print(f"Total balance: {self.__balance}")
    def deposit(self, amount):
        self.__balance += amount 
        print("total amount are you deposit",amount)
        
r = AB_bank_bd()
r.deposit(500)
r.show()
r.__balance()