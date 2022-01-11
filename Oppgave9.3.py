class Acount:
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self): 
        return self.__id

    def setId(self, id):
        self.__id = id
    
    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
       self.__balance = balance  

    def getAnnualint(self):
        return self.__annualInterestRate

    def setAnnualint(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self): 
        return self.__annualInterestRate / 12 

    def getMonthlyInterest(self): 
        k = self.__balance * self.getMonthlyInterestRate() / 100
        return k

    def setWithdraw(self, withdraw): 
        self.__balance = self.__balance - withdraw

    def setDeposit(self, deposit): 
        self.__balance = self.__balance + deposit


def main():
    acount1 = Acount(1122, 20000, 4.5)
    acount1.setWithdraw(2500)
    acount1.setDeposit(3000)
    print(f'Bank information:')
    print(f'ID: {acount1.getId()}') 
    print(f'balance: {acount1.getBalance()}$')
    print(f'Monthly interest rate: {acount1.getMonthlyInterestRate():} %')
    print(f'monthly interest: {acount1.getMonthlyInterest()}$ ')

main()
    
