from Task3.Fee.bonus import bonus
from Task3.Fee.commission import commission


class Card:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self.balance = float(0)
        self.count_operation = int(0)

    def operation(self):
        if self.count_operation == 2:
            self.count_operation = 0
        else:
            self.count_operation = self.count_operation + 1

    def deposit(self, sum_deposit):
        if self.is_divide_50(sum_deposit):
            self.operation()
            if self.count_operation == 0:
                balance_old = self.balance
                self.balance = bonus(self.balance + sum_deposit)
                print(f"Bonus {self.balance - balance_old - sum_deposit}")
            else:
                self.balance = self.balance + sum_deposit
            print(self.balance)
        else:
            print("Error! The amount must be a multiple of 50")
            print(self.balance)

    def withdraw(self, sum_withdraw):
        if self.is_divide_50(sum_withdraw):
            balance_old = self.balance
            data = commission(self.balance, sum_withdraw) # Вычисляем комиссию
            if data >= sum_withdraw:
                self.operation()
                if self.count_operation == 0:
                    self.balance = bonus(data - sum_withdraw) # Сначала снимаем, потом начисляем бонус
                    print(f"Commission {balance_old  - data}. Bonus {self.balance - (data -sum_withdraw)}")
                else:
                    self.balance = data-sum_withdraw
                    print(f"Commission {balance_old  - data}")

            else:
                print("Error! Amount withdraw more than balance card")
            print(self.balance)
        else:
            print("Error! The amount must be a multiple of 50")
            print(self.balance)

    def quit(self):
        print(self.balance)
        return None

    def is_divide_50(self, sum_operation):
        return (sum_operation % 50) == 0
