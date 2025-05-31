# class Accounts:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0
#         self.deposits= []
#         self.withdrawal = []
#         self.loan_amount = 0
#         self.is_frozen = False
#         self.minimum_balance = 0

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Deposit amount must be positive."
#         self.deposits.append(amount)
#         self.balance += amount
#         return f"Confirmed: You have deposited ${amount}. New balance is ${self.balance:.2f}"

#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Withdrawal amount must be positive."
#         if amount > self.balance - self.minimum_balance:
#             return "Insufficient funds for this withdrawal."
#         self.withdrawal.append(amount)
#         self.balance -= amount
#         return f"Confirmed: You have withdrawn ${amount}. New balance is ${self.balance:.2f}"

#     def transfer_fund(self, amount, other_account):
#         if amount <= 0:
#             return "Transfer Amount must be positive."
#         if amount > self.balance - self.minimum_balance:
#             return "Insufficient funds for this transfer."
#         self.withdraw(amount)
#         other_account.deposit(amount)
#         return f"Transferred ${amount} to {other_account.name}. Your new balance is ${self.balance:.2f}"

#     def request_loan(self, amount):
#         limit=self.calculate_limit()
#         if amount > limit:
#             return "you are not eligible to borrow ${amount}.Your loan limit is ${limit}"
#         if amount <= 0:
#             return "Loan amount must be positive."
#         self.loan_amount += amount
#         self.balance += amount 
#         # self.deposit +=amount
#         # checking how much loan to give /eligibility
#         return f'Loan of ${amount} approved. New balance is ${self.balance:.2f}'
#     def calculate_limit(self):
#         total_deposits=sum (self.deposits)
#         return total_deposits//3
    
#     def repay_loan(self, amount):
#         if amount <= 0:
#             return "Repayment amount must be positive."
#         if amount > self.balance:
#             return "Insufficient funds to repay the loan."
#         self.loan_amount -= amount
#         self.balance -= amount
#         return f"Repayment of ${amount} successful. Remaining loan amount is ${self.loan_amount:.2f}"

#     def view_accounts(self):
#         return f"Account owner: {self.name}, Current Balance: ${self.balance:.2f}"

#     def change_account_owner(self, new_name):      

#         self.name = new_name
#         return f"Account owner changed to {self.name}"

#     def account_statement(self):
#         statement = "Account Statement:\n"
#         statement += "Deposits:\n"
#         for deposit in self.deposits:
#             statement += f"  - ${deposit}\n"
#         statement += "Withdrawals:\n"
#         for withdrawal in self.withdrawal:
#             statement += f"  - ${withdrawal}\n"
#         return statement

#     def interest_calculation(self):
#         interest = self.balance * 0.05
#         self.balance += interest
#         return f"Interest of ${interest:.2f} applied. New balance is ${self.balance:.2f}"

#     def freeze_account(self):
#         self.is_frozen = True
#         return "Account has been frozen for security reasons."

#     def unfreeze_account(self):
#         self.is_frozen = False
#         return "Account has been unfrozen."

#     def set_minimum_balance(self, amount):
#         if amount < 0:
#             return "Minimum balance must be non-negative."
#         self.minimum_balance = amount
#         return f"Minimum balance set to ${self.minimum_balance:.2f}."

#     def close_account(self):
#         self.balance = 0
#         self.deposits.clear()
#         self.withdrawal.clear()
#         self.loan_amount = 0
#         return "Account closed. All balances and transactions have been reset."
   
# class Transaction():
#     amount=0
#     narration=
#     transaction_type=
#     date time
# Use only one method self.transaction which is a list
# update get balance 

from datetime import datetime
class Transaction:
    def __init__(self,narration,amount,transaction_type):
        self.date_time=datetime.now()
        self.narration=narration
        self.amount= amount
        self.transaction_type=transaction_type

    def __repr__(self):
        return f"{self.date_time} -{self.transaction_type}:{self.narration} of  ${self.amount:.2f}"

class Accounts:
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self._balance= 0
        self.transactions=[]
        self.minimum_balance=0
    def deposit(self,amount):
        if amount<=0:
            return "Deposit amount must be positive"
        self._balance +=amount
        self.transactions.append(Transaction("Deposit",amount,"Credit"))
        return f"confirmed,you have deposited  ${amount}.new balance is ${self.get_balance():.2f}"
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self._balance - self.minimum_balance:
            return "Insufficient funds for this withdrawal."
        self._balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount, "Debit"))
        return f"Confirmed: You have withdrawn ${amount}. New balance is ${self.get_balance():.2f}"
    def  get_balance(self):
        return self._balance
    def view_transaction(self):
        return "\n".join(str(transaction) for transaction in self.transactions )
    def change_account_owner(self,new_name):
        self.name=new_name
        return  f"Account owner changed to  ${self.name}"
    
    def  set_minimum_balance(self, amount):
        if amount <0:
            return "minimum balance must be positive"
        self.minimum_balance = amount
        return f"minimum balance set to  ${self.minimum_balance:.2f}"
    def close_account(self):
        self.balance=0
        self.transactions.clear()
        return "Account closed .All balances and transactions have been reset."
          