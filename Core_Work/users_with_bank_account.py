# HELLO TO WHO IS GRADING, I ASKED JUSTIN FOR HELP ON THIS ASSIGNMENT, I ALSO WORKED WITH FARYAL , SO CODES MAY HAVE SOME SIMILARITIES. THANK YOU!!
# I WAS UNABLE TO GET IT TO WORK, AM SUBMITTING THE ASSIGNMENT AND WILL ASK A TA ON  MOMDAY FOR HELP. I FEEL LIKE I'M ALMOST THERE!



class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    # 	USER.BANKACCOUNT.DEPOSIT?? I'M UNSURE HERE

    def make_withdrawal(self, amount):
        self.account.make_withdrawal(amount)
        return self

    def display_balance(self,balance):
        self.account.display_balance(balance)
        return self



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
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance <= 0:
            self.balance = self.balance - 5
            print("A withdrawal cannot be made with the remaining balance. Your account will be deducted $5.")
        else:
            return self
        
    def display_account_info(self):
        print(f"Hello, {self.first_name} {self.last_name}. Your account number is #{self.account_number}, and you currently have a balance of ${self.balance} with a {self.interest_rate} yield interest. Thank you.")
        
    def yield_interest(self, interest_rate):
        if self.balance > 0:
            self.interest_rate = self.balance * (1 - interest_rate)
            return self
        else: 
            print("Yield interest unavailable, insufficient funds.")



Adriana = User("Sonia", "B", 2400)
# Adriana = User("Adriana", "Cielo", 603882, 2500, .54)

Adriana.make_deposit(300).display_balance()



