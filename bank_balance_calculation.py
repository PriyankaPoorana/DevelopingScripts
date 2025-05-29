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

newstring=[]
count=1
for i in range(1,len(string)):
  if (string[i]==string[i-1]):
    count+=1
  elif string[i]==string[-1]:
    newstring.append(string[i]+str(count))
  else:
    newstring.append(string[i-1]+str(count))
    count=1
print(''.join(newstring))

for i in range(0,len(l1)):
  if l1[i]%3==0 and l1[i]%5==0:
    l2.append("FizzBizz")
  elif l1[i]%3==0:
    l2.append("Fizz")
  elif l1[i]%5==0:
    l2.append("Bizz")
  else:
    l2.append(l1[i])

    str1='a gentleman'
    str2='elegant man'

    l1=str1.split('')
    l2=str2.split('')

for i in range(0,n):
   l1=[0,1]
   if n>2:
    