import json
class BankAccount :
    def __init__ (self, account_holder, balance) :
        self.account_holder = account_holder
        self.balance = balance

    def deposit (self,amount) :

        self.balance += amount
        print(f"{self.account_holder}'s balance after deposit is {self.balance}")

    def withdraw (self, amount) :
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_holder}'s balance after withdraw is {self.balance}")

        else :
            print("Not enough balance")

    def check_balance(self):
        print(f"{self.account_holder}'s balance is {self.balance}")

    def to_dict(self) :
        return {
            "account_holder" : self.account_holder,
            "balance" : self.balance
        }

def save_accounts(accounts):
    data = []
    for acc in accounts :
        data.append(acc.to_dict())

    with open("accounts.json", "w") as file:
        json.dump(data,file)

def load_accounts ():
    accounts = []
    try: 
     with open ("accounts.json", "r") as file :
        data = json.load(file)

        for item in data :
           account = BankAccount(item["account_holder"], item["balance"])
           accounts.append(account)
        
    except FileNotFoundError:
     pass
    return accounts



accounts = load_accounts()

while True :
    print("1. Create Account ")
    print("2. Deposit Money ")
    print("3. Withdraw Money ")
    print("4. View All Accounts")
    print("5. Check Balance ")
    print("6. Exit ")

    choice = (input("Enter your choice: "))

    if choice == '1' :
        name = input("Enter the name of the account holder: ")
        balance = int(input("Enter the starting balance: "))
        new_account = BankAccount(name,balance)
        accounts.append(new_account)
        save_accounts(accounts)
        print("Account created successfully!")

    elif choice == '2' :

        name = input("Enter the name of the account holder: ")
        selected_account = None

        for acc in accounts :
            if acc.account_holder == name :
                selected_account = acc
                break

        if selected_account :
            amount = int(input("Enter the amount to deposit: "))
            selected_account.deposit(amount)
            save_accounts(accounts)
            
        else :
            print("Not enough amount")

    elif choice == '3' :
        name = input("Enter the name of the account holder: ")

        selected_account = None

        for acc in accounts :
            if acc.account_holder == name:
                selected_account = acc
                break

        if selected_account :
            amount = int(input("Enter the amount to withdraw: "))
            selected_account.withdraw(amount)
            save_accounts(accounts)
        else : 
            print("Not enough amount!!!")

    elif choice == '4' :
        for acc in accounts :
            print(f"{acc.account_holder} | {acc.balance}")

    elif choice == '5' :
        name = input("Enter the name of the account holder: ")

        selected_account = None

        for acc in accounts :
            if acc.account_holder == name:
                selected_account = acc
                break
            
        if selected_account:
            selected_account.check_balance()
        
        else :
            print("Account not found")

    elif choice == '6' :
        print("Exiting the program")
        break

    else :
       print("Invalid choice")


