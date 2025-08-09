class BankAccount:
    """A class to manage a bank account with basic operations."""
    
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = initial_balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        self.account_balance += amount
        return True

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0 or self.account_balance < amount:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")