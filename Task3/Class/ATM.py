from Task3.Class.Card import Card
from Task3.Fee.wealthTax import wealth_tax


class ATM:
    switch_off = False
    card = Card(33333, "Ivan")

    def __int__(self):
        self.atm_start()

    def atm_start(self):
        while not self.switch_off:
            print("Enter 1 for deposit.")
            print("Enter 2 for withdraw.")
            print("Enter 3 for quit.")
            data = input()

            match data:
                case '1':
                    try:
                        self.card.deposit(int(input("Enter sum to deposit\n")))
                        self.card.balance = wealth_tax(self.card.balance)
                    except:
                        print("Error sum!")
                        self.card.balance = wealth_tax(self.card.balance)
                case '2':
                    try:
                        self.card.withdraw(int(input("Enter sum to withdraw\n")))
                        self.card.balance = wealth_tax(self.card.balance)
                    except:
                        print("Error sum!")
                        self.card.balance = wealth_tax(self.card.balance)
                case '3':
                    self.switch_off = True
                case _:
                    print("Error command!")
                    self.card.balance = wealth_tax(self.card.balance)
                    print(self.card.balance)
