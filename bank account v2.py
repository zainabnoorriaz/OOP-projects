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

accounts = []
while True: 
 print("_____MENU_____")
 print("1. Create account")
 print("2. Deposit money")
 print("3. Withdraw money")
 print("4. Check Balance")
 print("5. View all accounts")
 print("6. Exit")

 choice = int(input("Enter your choice : "))

 if choice == 1 :
     name = input("Enter the name of account holder: ")
     balance = int(input("Enter the starting balance: "))
     new_account = BankAccount(name,balance)
     accounts.append(new_account)
     print("Account is created successfully")


 elif choice == 2 :

    name = input("Enter account holder name: ")
    selected_account = None

    for acc in accounts :
        if acc.account_holder == name:
            selected_account = acc
            break

    if selected_account :

       amount = int(input("Enter the amount to deposit: "))
       selected_account.deposit(amount)
    else :
        print("Account Not Found")

 elif choice == 3 :
    name = input("Enter the name of the account holder: ")
    selected_account = None

    for acc in accounts :
        if acc.account_holder == name :
            selected_account = acc
            break

    if selected_account :
       amount = int(input("Enter the amount to withdraw: "))
       selected_account.withdraw(amount)
    else :
        print("Account Not Found")
 
 elif choice == 4 :
     name = input("Enter the name of the account holder : ")
     selected_account = None

     for acc in accounts :
         if acc.account_holder == name:
             selected_account = acc
             break
     if selected_account:
        selected_account.check_balance()
     else :
         print("Account Not Found")

 elif choice == 5 :
     for acc in accounts :
         print(f"{acc.account_holder} | {acc.balance}")
     

 elif choice == 6 :
     print("Exiting the program")
     break
  
 else :
     print("Invalid choice")