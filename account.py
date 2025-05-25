class Accounts:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposit = []
        self.withdrawal = []
        self.loan_amount = 0
        
        self.minimum_balance = 0

    def deposit(self, amount):
        
        if amount <= 0:
            return "Deposit amount must be positive."
        
        self.deposit.append(amount)
        self.balance += amount
        return f"Confirmed: You have deposited ${amount}. New balance is ${self.balance:.2f}"
    def withdraw(self,amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance - self.minimum_balance:
            return "Insufficient funds for this withdrawal."

        self.withdrawal.append(amount)
        self.balance -= amount
        return f"Confirmed: You have withdrawn ${amount}. New balance is ${self.balance:.2f}"
    def transfer_fund(self,amount,other_account):

        if amount <=0:
            return "Transfer Amount must be positive"
        if amount > self.balance-self.minimum_balance:
            return "Insufficient funds for this transfer"
        self.withdraw(amount)
        other_account.deposit(amount)
        return f"Transferred ${amount} to {other_account.name}. Your new balance is ${self.balance:.2f}"

    def request_loan(self,amount):
        if amount <=0:
            return "Loan amount must be positive"
        
        self.loan_amount += amount
        self.balance += amount
        
        return f'loan of {amount} approaved .New balance is {self.balance:.2f}'
   
   
    def repay_loan(self,amount):
        if amount <=0:
            return "Repayment amount must be positive"
        if amount > self.balance:
            return "insufficient funds to repay the loan"
        self.loan_amount -=amount
        self.balance -= amount
        return f"Repayment of {amount} successful.Remaining loan amount is {self.loan_amount:.2f}"
    
    def view_accounts(self):
        return f"account owner :{self.name},current Balance: {self.balance:.2f}"
    

    def change_account_owner(self,new_name):
        self.name = new_name
        return f"Account owner changed to {self.name}"
    
    def account_statement(self):
        statement = "Account Statement:\n"
        statement += "Deposits:\n"
        for deposit in self.deposit:
            statement += f"  - ${deposit}\n"
        statement += "Withdrawals:\n"
        for withdrawal in self.withdrawal:
            statement += f"  - ${withdrawal}\n"
        return statement

    def interest_calculation(self):
        interest = self.balance * 0.05
        self.balance += interest
        return f"Interest of ${interest:.2f} applied. New balance is ${self.balance:.2f}"

    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen for security reasons."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance must be non-negative."
        self.minimum_balance = amount
        return f"Minimum balance set to ${self.minimum_balance:.2f}."

    def close_account(self):
        self.balance = 0
        self.deposit_history.clear()
        self.withdrawal_history.clear()
        self.loan_amount = 0
        return "Account closed. All balances and transactions have been reset."


        