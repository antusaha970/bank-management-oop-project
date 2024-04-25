# todo: is total available balance is the amount the sum of what users deposited?
class Bank:
    def __init__(self) -> None:
        self.accounts = []  # user objects
        self.totalAvailableBalance = 0
        self.totalLoan = 0
        self.isLoanOff = False
        self.isBankrupt = False

    def add_account(self, account):  # account object
        self.accounts.append(account)

    def add_loan_amount(self, amount):
        self.totalLoan += amount

    def find_bank_account(self, account_no):
        for account in self.accounts:
            if account.account_num == account_no:
                return account
        return False

    def delete_user_account(self, account_no):
        for account in self.accounts:
            if account.account_num == account_no:
                self.accounts.remove(account)
                print("Account deleted!!!")
                return

    def view_all_account_list(self):
        print("Account num\tOwner name\tAccount type")
        for account in self.accounts:
            print(f"""{account.account_num}\t{
                  account.name}\t{account.account_type}""")

    def check_total_balance(self):
        print(f"Total balance: {self.totalAvailableBalance}")

    def check_total_loan(self):
        print(f"Total loan: {self.totalLoan}")

    def turn_of_loan_feature(self):
        self.isLoanOff = True

    def set_bankrupt(self):
        self.isBankrupt = True
