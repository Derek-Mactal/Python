class user: 
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def make_withdraw(self, amount):
        self.balance -= amount
        return self.balance
        
    def display_user_balance(self):
        print("Name is",self.name,"Balance is", self.balance)
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return other_user.balance


derek = user("Derek",100)
pingus = user("Pingus", 200)

derek.display_user_balance()

print("Other user balance is now", derek.transfer_money(pingus, 20))z
