class BankAccount:
    def __init__(self, owner: str, number: str, balance: float):
        self.__owner = owner
        self.__number = number
        self.__balance = balance
        self.__service_charge()  # Apply service charge on initialization
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
            return f"Deposited {amount} to {self.__owner}'s account. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
            return f"Withdrew {amount} from {self.__owner}'s account. New balance: {self.__balance}"
        elif amount > self.__balance:
            return "Insufficient funds for this withdrawal."
        else:
            return "Withdrawal amount must be positive."
    
    @property
    def get_balance(self) -> float:
        return self.__balance
    
    def __service_charge(self):
        # A simple service charge of 1% of the balance
        charge = self.__balance * 0.01
        self.__balance -= charge
        return f"Service charge of {charge} applied. New balance: {self.__balance}"
    
    

banco1 = BankAccount("Alice", "123456789", 1000.0)
print(banco1.deposit(200))  # Deposit
print(banco1.withdraw(150))  # Withdraw
print(f"Current balance: {banco1.get_balance()}")  # Get balance