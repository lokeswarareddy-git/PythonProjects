#Setting 
from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass  = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.savingAccounts = {}
    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account Creation has been Succesful , your account number is :", self.accountNumber)
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False
    def withdraw(self,withdrawalAmount):
        if withdrawalAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficiant Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawalAmount
            print("WithDrwal Successful")
            self.displayBalance()

    def deposit(self,despositAmount):
        self.savingAccounts[self.accountNumber][1] += despositAmount
        print("Deposit Successful")
        self.displayBalance()
        
    def displayBalance(self):
        print("Avaialble Balance:", self.savingAccounts[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create new Account")
    print("Enter 2 to access Existing Account")
    print("Enter 3 to Exit ")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name")
        name = input()
        print("Enter Initial Deposit")
        deposit = int(input())
        savingsAccount.createAccount(name,deposit)
    elif userChoice is 2:
        print("Enter Your name :")
        name = input()
        print("Enter Your Account Number :")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name,accountNumber)
        if authenticationStatus is True:
            while True:
                print(" Enter 1 to Withdraw :")
                print("Enter 2 to Depost:")
                print("Enter 3 to Display Account Balance")
                print("Enter 4 to go back to previus Menu ")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter Withdrawal Amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter an amount to be deposted")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance() 
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()






