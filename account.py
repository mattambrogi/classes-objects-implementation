import classes

def make_account_class():
  """Return the Account class, which has deposit and withdraw methods.
  Mimics typical class creation thruogh class statement in Python but ends with call to make_class"""
  interest = 0.02
  # Only takes one argument. Whatever is passed will be bound to holder.
  def __init__(self, account_holder):
    self['set']('holder', account_holder)
    self['set']('balance', 0) 
  
  def deposit(self, amount):
    new_balance = self['get']('balance') + amount
    self['set']('balance', new_balance)
    return self['get']('balance')
  
  def withdraw(self, amount):
    balance = self['get']('balance')
    if amount > balance:
      return 'Insufficent funds'
    self['set']('balance', balance - amount)
    return self['get']('balance')
  
  return classes.make_class(locals())