class BankAccount:

    def __init__ (self, account_holder, balance) :
      
        self.account_holder = account_holder
        self.balance = balance

    def deposit (self, amount):
  
        self.balance += amount
        print(f"The {self.account_holder}'s new balance is: {self.balance} " )

    def withdraw (self, amount) :
        if self.balance >= amount :
            self.balance -= amount
            print(f"{self.account_holder}'s new balance is {self.balance}")
        else :
            print("Not enough money to withdraw")

    def check_balance(self) :
        print(f"{self.account_holder}'s balance is {self.balance} ")


account_holder = input("Enter the account holder: ")
balance = int(input("Enter the balance:"))

account1 = BankAccount(account_holder, balance)

accounts = []
while True: 
 print("_____MENU_____")
 print("1. Deposit money")
 print("2. Withdraw money")
 print("3. Check Balance")
 print("4. Exit")

 choice = int(input("Enter your choice : "))

 if choice == 1 :
    
    amount = int(input("Enter the amount to deposit"))
    account1.deposit(amount)

 elif choice == 2 :
    
    amount = int(input("Enter the amount to withdraw: "))
    account1.withdraw(amount)
 
 elif choice == 3 :
     account1.check_balance()

 elif choice == 4 :
     print("Exiting the program")
     break
  
 else :
     print("Invalid choice")


