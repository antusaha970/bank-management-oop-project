from user import User
from bank import Bank

gp = Bank()

antu = User("Antu", "ss", "saving")
gp.add_account(antu)
raju = User("raju", "ra", "current")
gp.add_account(raju)
antu.deposit_money(500, gp)
print(antu.available_balance())
gp.check_total_balance()
antu.withdraw_money(400, gp)
gp.check_total_balance()
antu.transfer_money("raju", 20, gp)
print(antu.available_balance())
antu.take_loan(gp, 250)
antu.take_loan(gp, 50)
antu.take_loan(gp, 50)
gp.check_total_balance()
print(antu.available_balance())
