class Admin:
    def __init__(self, name, password, bank) -> None:
        self.name = name
        self.password = password
        self.bank = bank

    def delete_user_account(self, account_no):
        self.bank.delete_user_account(account_no)

    def see_all_users(self):
        self.bank.view_all_account_list()

    def check_bank_available_balance(self):
        self.bank.check_total_balance()

    def check_bank_given_loan(self):
        self.bank.check_total_loan()

    def turn_off_bank_loan_feature(self):
        self.bank.turn_off_loan_feature()

    def set_bank_to_bankrupt(self):
        self.bank.set_bankrupt()
