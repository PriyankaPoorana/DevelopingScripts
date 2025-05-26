class bank_account:
    def __init__(self,account_holder,balance=0.0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("you have deposited ",amount," so your new balance is ",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            amount=self.balance-amount
            print("you have withdrawn ",amount," so your new balance is ",self.balance)
    def get_balance(self):
        print("your balance is ",self.balance)

def main():
    option,amount=input("Enter 1 to deposit, 2 to withdraw, 3 to check balance: "), float(input("Enter amount: "))
    if option == '1':
        bac.deposit(amount)
    elif option == '2':
        bac.withdraw(amount)
    else:
        bac.get_balance()

if __name__=="__main__":
    main()