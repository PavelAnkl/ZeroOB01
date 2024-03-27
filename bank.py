class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы внесли {money} руб. Ваш баланс теперь - {self.balance}')
    def withdraw(self, money):
        if money > self.balance:
            print('Денег на счету недостаточно')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы сняли {money} руб. Ваш баланс теперь - {self.balance}')

    def all_balance(self):
        print(f'Текущий баланс - {self.balance}')

man = Account('123456789', 60)

man.all_balance()
man.deposit(40)
man.withdraw(20)