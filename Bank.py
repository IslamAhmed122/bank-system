from datetime import datetime

class Account:
    '''
    Class that represents a bank account
    '''
    def __init__(self, account_number, currency, name):
        self.account_number = account_number
        self.currency = currency
        self.name = name
        self.balance = 0
        self.transactions = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('d', amount, datetime.now()))
        print("Deposit Successful!")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(('w', amount, datetime.now()))
            print("Withdrawal Successful")
            
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
        
    def log(self):
        print("Your account information")
        print("******************************")
        print(f"Account Owner: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print("Last Transaction: ")
        
        try:
            last = self.transactions[-1]
            if last[0] == 'd':
                print(f"Deposit | Amount: {last[1]} | Time: {last[2]}")
            else:
                print(f"Withdraw | Amount: {last[1]} | Time: {last[2]}")
        except:
            print("No transactions on the account yet")


class SavingsAccount(Account):
    def __init__(self, account_number, currency, name):
        super().__init__(account_number, currency, name)
        
        self.rate = 0.05
        
    def add_cycle(self):
        increase = self.balance * self.rate
        self.balance += increase


accounts = []

while True:
    print("""\n\n
Welcome to the Bank System!
___________________________
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Show Information
5. Add Cycle
6. Exit
___________________________
    """)
    
    choice = input('Enter your choice: ')
    if choice == '1':
        account_number = int(input("Enter account number: "))
        name = input("Enter your name: ")
        currency = input("Enter currency: ")
        type_ = input("Enter 'C' for Current Account or 'S' for Savings Account: ")
        
        if type_ == 'C':
            acc = Account(account_number, currency, name)
        else:
            acc = SavingsAccount(account_number, currency, name)
        
        accounts.append(acc)
        
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        value = float(input("Enter deposit value: "))
        
        # Search for corresponding account
        for acc in accounts:
            if acc.account_number == account_number:
                acc.deposit(value)
                break
        else:
            print("No account found with that ID")
            
    elif choice == '3':
        account_number = int(input("Enter account number: "))
        value = float(input("Enter withdraw value: "))
        
        for acc in accounts:
            if acc.account_number == account_number:
                acc.withdraw(value)
                break
        else:
            print("No account found with that ID")
    elif choice == '4':
        account_number = int(input("Enter account number: "))
        
        for acc in accounts:
            if acc.account_number == account_number:
                acc.log()
                break
        else:
            print("No account found with that ID")
    elif choice == '5':
        account_number = int(input("Enter account number: "))
        
        for acc in accounts:
            if acc.account_number == account_number:
                # Check if account is a savings account
                if type(acc) == SavingsAccount:
                    acc.add_cycle()
                else:
                    print("Error: Not a Savings Account")
                break
        else:
            print("No account found with that ID")
    elif choice == '6':
        break
    else:
        print("Invalid input. Try Again")