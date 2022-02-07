import account
import classes


def make_checking_account_class():
  interest = 0.01
  withdraw_fee = 1
  def withdraw(self, amount):
    fee = self['get']('withdraw_fee')
    return Account['get']('withdraw')(self, amount + fee)
  return classes.make_class(locals(), account.make_account_class())