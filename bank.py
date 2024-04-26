class Bank:
    def __init__(self) -> None:
        self.accounts = []  # user objects
        self.totalAvailableBalance = 0
        self.totalLoan = 0
        self.isLoanOff = False
        self.isBankrupt = False
        self.admins = []  # admin class object

    def add_admin(self, admin):
        self.admins.append(admin)

    def add_bank_balance(self, amount):
        self.totalAvailableBalance += amount

    def withdraw_bank_balance(self, amount):
        self.totalAvailableBalance -= amount

    def add_account(self, account):  # account object
        self.accounts.append(account)

    def add_loan_amount(self, amount):
        self.totalLoan += amount

    def add_admin(self, admin):  # admin object
        self.admins.append(admin)
        print("A admin added")

    def login_admin(self, admin):
        for ad in self.admins:
            if ad.name == admin.name and ad.password == admin.password:
                print("Login successful")
                return admin
        return False

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
        print("AC_NO\tOwner name\tAccount type")
        for account in self.accounts:
            print(f"""{account.account_num}\t{
                  account.name}\t{account.account_type}""")

    def check_total_balance(self):
        print(f"Total balance: {self.totalAvailableBalance}")

    def check_total_loan(self):
        print(f"Total loan: {self.totalLoan}")

    def turn_off_loan_feature(self):
        self.isLoanOff = True
        print("Loan feature is turned off")

    def set_bankrupt(self):
        self.isBankrupt = True
        print("Bankrupt is turned on")
