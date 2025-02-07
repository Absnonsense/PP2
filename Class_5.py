class Account:
  def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

  def deposit(self, amount):
      self.balance += amount

  def withdraw(self, amount):
      if amount > self.balance:
          print("Not enough balance")
      else:
          self.balance -= amount

  def __str__(self):
      return "Account owner: " + str(self.owner) + "Balance: " + str(self.balance)

account = Account("John Doe", 100)
print(account)
account.deposit(50)
print(account)
account.withdraw(75)
print(account)
account.withdraw(100)
print(account)
