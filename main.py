import account
import checking_account




Account = account.make_account_class()
matt_account = Account['new']('Matt')
print(matt_account['get']('interest')) #Class interest .02
matt_account['set']('interest', .01)
matt_interest = matt_account['get']('interest')
print(matt_interest) #instance interest .01
print(Account['get']('interest')) # class interest .02
matt_account['get']('deposit')(100)
matt_account['get']('withdraw')(20)
print(matt_account['get']('balance'))


CheckingAccount = checking_account.make_checking_account_class()
matt_checking_account = CheckingAccount['new']('Matt')
print(matt_checking_account['get']('withdraw_fee')) # 1