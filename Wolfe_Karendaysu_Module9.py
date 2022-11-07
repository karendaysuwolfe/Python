# Name: Karendaysu Wolfe
# Date: 9-15-22
# Course: Intro to Programming with Pyth
# Assignment: Module 7
# Description: we will work with classes by creating a banking program

class BankAcct():
    def __init__(self, acct_num, balance):
        self.__account_number = acct_num
        self.__balance = balance

    def withdrawl(self, amount):
        if amount >= 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Sorry, You do not have sufficient balance')

    def deposit(self, amount):
       if amount > 0:
        self.balance += amount

    def getBalance(self):
       return self.__balance

class CheckingAccount(BankAcct):
    def __init__(self, acct_num, balance, fees, min_bal):
        super().__init__(acct_num, balance)
        self.__fees = fees
        self.__min_balance = min_bal

    def deductFees(self):
        self.withdrawl(self.__fees)

    def withdrawl(self, amount):
        self.withdrawl(amount)
        if self.getBalance() < self.__min_balance:
            print('Info *** You are not maintaining a minimum balance in account.')

    def checkMinimumBalance(self):
        return self.__min_balance


class SavingsAccount(BankAcct):
    def __init__(self, acct_num, balance, rate):
        super().__init__(acct_num, balance)
        self.__interestRate = rate

    def addInterest(self):
        interest = self.getBalance() * self.__interestRate / 100
        self.deposit(interest)

class BankAccount():

    def __init__(self, acct_no, balance):
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._account_number = acct_no
        self._balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawn amount is negative.")
        if amount > self._balance:
            raise ValueError('Dont have sufficient balance')
        self._balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount is negative.")
        self._balance += amount

    def getBalance(self):
        return self._balance


class CheckingAccount(BankAccount):

    def __init__(self, acct_no, balance, fees, minimumBalance):
        super().__init__(acct_no, balance)
        self._fees = fees
        self._minimumBalance = minimumBalance
        if self.checkMinimumBalance():
            self.deductFees()

    def deductFees(self):
        print('${} deducted for not maintaining sufficient balance'.format(self._fees))
        self._balance -= self._fees

    def checkMinimumBalance(self):
        return self.getBalance() < self._minimumBalance


def withdraw(self, amount):
    super().withdraw(amount)

    if self.checkMinimumBalance():
        self.deductFees()


def __str__(self):
    return 'Account Number: {}, Current Balance: ${:.2f}'.format(self._account_number, self.getBalance())


class SavingsAccount(BankAccount):
    def __init__(self, acct_no, balance, interest_rate):
        super().__init__(acct_no, balance)
        self._interest_rate = interest_rate

    def addInterest(self):
        interest = self.getBalance() * self._interest_rate / 100
        self.deposit(interest)


def main():
    id = input('Enter checking account id: ')
    balance = float(input('Enter checking account initial balance: '))
    min_balance = float(input('Enter minimum balance to be maintained: '))
    fees = float(input('Enter fees to be deducted for not maintaining minimum balance: '))
    try:
        checkAccount = CheckingAccount(id, balance, fees, min_balance)
        print(checkAccount)
    except Exception as e:
        print(str(e))


main()

input('press enter to exit')