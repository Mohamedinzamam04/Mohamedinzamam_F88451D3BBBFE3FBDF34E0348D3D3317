class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance


  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited:₹{}. New balance:₹{}".format(amount,
                                                   self.__account_balance))
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")


  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw:₹{}.New balance:₹{}".format(amount,
                                                 self.__account_balance))
    else:
       print("Invalid withdrawl amount of insufficient balance.")


  def display_balance(self):
      print("Account balance for {} (Account #{}):{}".format(self.__account_holder_name, self.__account_number,self.__account_balance))


account = BankAccount(account_number="123456789",
                      account_holder_name="mohamed Inzamam ",
                      initial_balance=9000.0)

account.display_balance()
account.deposit(1500.0)
account.withdraw(3500.0)
account.display_balance()