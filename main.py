from user import User
from bank import Bank

brack = Bank()

antu = User("antu", "ppp", "saving")
brack.add_account(antu)
print(antu.available_balance())
antu.deposit_money(550)
print(antu.available_balance())
antu.withdraw_money(500, brack)
print(antu.available_balance())
antu.show_all_transaction()
antu.deposit_money(900)
antu.show_all_transaction()
print(antu.available_balance())
antu.take_loan(brack, 300)
brack.turn_of_loan_feature()
antu.take_loan(brack, 300)
antu.take_loan(brack, 300)
brack.view_all_account_list()
brack.check_total_loan()
