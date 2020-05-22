# class Account(object):
class Account:
    '''This class generates an account object'''

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


account = Account('balance.txt')
print(account.balance)
account.withdraw(100)
account.deposit(300)
print(account.balance)
account.commit()


class Checking(Account):
    '''This class generates a checking account object'''

    type = 'checking'

    def __init__(self, filepath, fee):
        # Account.__init__(self, filepath)
        super().__init__(filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount
        self.balance -= self.fee


print(Checking.type)
print(Checking.__doc__)

checking = Checking('balance.txt', 1)
checking.deposit(150)
checking.transfer(200)
print(checking.balance)
checking.commit()
print(checking.type)
print(checking.fee)
print(checking.__doc__)
