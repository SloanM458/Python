class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance, interest_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
    # don't forget to add some default values for these parameters!

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    # return self or self.balance????
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance <= 0:
            self.balance = self.balance - 5
            print("A withdrawal cannot be made with the remaining balance. Your account will be deducted $5.")
        else:
            return self
        # if BankAccount.can_withdraw(self.balance, amount):
        #     self.balance = self.balance - amount
        # else:
        #     print("A withdrawal cannot be made with the remaining balance. Your account will be deducted $5.")
        #     self.balance = self.balance - 5
        # return self
        # print(self.balance)
    # @staticmethod
    # def can_withdraw(balance, amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else:
    #         return True
    def display_account_info(self):
        print(f"Hello, {self.first_name} {self.last_name}. Your account number is #{self.account_number}, and you currently have a balance of ${self.balance} with a {self.interest_rate} yield interest. Thank you.")
        
    def yield_interest(self, interest_rate):
        if self.balance > 0:
            self.interest_rate = self.balance * (1 - interest_rate)
            return self
        else: 
            print("Yield interest unavailable, insufficient funds.")

Zane = BankAccount("Zane", "Trems", 550632, 12000, .4)
Zane.deposit(200).deposit(130).deposit(500).withdraw(700).yield_interest(.4).display_account_info()

Adriana = BankAccount("Adriana", "Cielo", 603882, 2500, .54)
Adriana.deposit(350).deposit(2000).withdraw(100).withdraw(300).withdraw(270).withdraw(1000).yield_interest(.54).display_account_info()


# I AM STUCK ON THE YIELD INTEREST FUNCTION, SPEND AN HOUR ON IT AND DON'T UNDERSTAND. WILL ATTEND A DOJO HALL TO GET A BETTER UNDERSTANDING THIS WEEK. THANKS!