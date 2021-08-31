class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.other_user = other_user
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount
        return self

bankUser1 = User("John Elway", "JohnE@denverbroncos.com")
bankUser2 = User("Peyton Manning", "PeytonM@denverbroncos.com")
bankUser3 = User("Karl Meklenburg", "KarlM@denverbroncos.com")

bankUser1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).transfer_money(bankUser3, 100).display_user_balance()

bankUser2.make_deposit(100).make_deposit(100).make_deposit(50).make_withdrawal(50).display_user_balance()

bankUser3.make_deposit(200).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()