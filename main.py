from random import randint


class User:
    def __init__(self, name, email, account_type) -> None:
        self.name = name
        self.email = email
        self.account_type = account_type
        self.balance = 0
        self.account_num = name + f"{randint(1, 100)}"
        self.transactions = []  # {'deposit': 500}
        self.loan_count = 0

    def view_account_num(self):
        return self.account_num

    def available_balance(self):
        return self.balance

    def add_transaction(self, name, amount):
        self.transactions.append({name: amount})

    def deposit_money(self, money, bank, addToBank=True):
        if money > 0:
            self.balance += money
            self.add_transaction("deposit", money)
            if addToBank:
                bank.add_bank_balance(money)

        else:
            print("Negative money can't be deposited")

    def withdraw_money(self, amount, bank):  # bank object
        if not bank.isBankrupt:
            if self.available_balance() >= amount and self.available_balance() != 0:
                self.balance -= amount
                print("Withdrawal successful")
                self.add_transaction("withdrawal", amount)
                bank.withdraw_bank_balance(amount)

            else:
                print("Withdrawal amount exceeded")
        else:
            print("Can't withdraw amount because bank is bankrupt")

    def take_loan(self, bank, amount):  # bank object
        if not bank.isBankrupt:
            if not bank.isLoanOff:
                if self.loan_count < 2:
                    if bank.totalAvailableBalance >= amount:
                        self.loan_count += 1
                        bank.add_loan_amount(amount)  # bank class method
                        bank.withdraw_bank_balance(amount)  # bank class method
                        self.deposit_money(amount, bank, False)
                        print("Loan has given to you")
                    else:
                        print("Not enough money in the bank to give loan")
                else:
                    print("You have reached to loan limit")
            else:
                print("Bank has turn offed the loan feature")

        else:
            print("Bank is bankrupt")

    def transfer_money(self, account_no, amount, bank):  # bank object
        account = bank.find_bank_account(account_no)  # bank class method
        if account:
            if self.available_balance() != 0 and self.available_balance() >= amount:
                self.balance -= amount
                account.deposit_money(amount, bank, False)
                self.add_transaction("bank_transfer", amount)
                print("Bank transfer successful")
            else:
                print("Not enough money to transfer!!")
        else:
            print("Account does not exist")

    def show_all_transaction(self):
        print("Your transactions!!")
        for transaction in self.transactions:
            print(transaction)


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

    def login_admin(self, admin):  # admin object
        for ad in self.admins:
            if ad.name == admin.name and ad.password == admin.password:
                print("Login successful")
                return admin
        return False

    def login_user(self, name, email):  # user object
        for user in self.accounts:
            if name == user.name and email == user.email:
                print("Login successful")
                return user
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
        print(f"""Total balance: {
              self.totalAvailableBalance}""")

    def check_total_loan(self):
        print(f"Total loan: {self.totalLoan}")

    def turn_off_loan_feature(self):
        self.isLoanOff = True
        print("Loan feature is turned off")

    def set_bankrupt(self):
        self.isBankrupt = True
        print("Bankrupt is turned on")


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


def runSystem():
    bank = Bank()
    default_admin = Admin("admin", "123", bank)
    bank.add_admin(default_admin)
    while True:
        print("<--- Welcome to the bank --->")
        print("1. Continue as admin")
        print("2. Continue as user")
        print("3. Exit")
        cmd = int(input("please enter an option: "))
        if cmd == 1:  # continue as admin
            while True:
                print("<--- Admin options --->")
                print("1. Create an admin account")
                print("2. Login to admin account")
                print("3. Exit")
                op = int(input("Enter your option: "))
                if op == 1:  # create admin account
                    name = input("Enter name: ")
                    password = input("Enter password: ")
                    admin = Admin(name, password, bank)
                    bank.add_admin(admin)
                    while True:
                        print("1. Delete user account")
                        print("2. View all users account list")
                        print("3. View total bank balance")
                        print("4. View total bank loan amount")
                        print("5. Turn off loan feature")
                        print("6. Set bank to bank to bankrupt")
                        print("7. Exit")
                        admin_op = int(input("Please choose your option: "))
                        if admin_op == 1:
                            user_acc_no = input("Enter user account no: ")
                            admin.delete_user_account(user_acc_no)
                        elif admin_op == 2:
                            admin.see_all_users()
                        elif admin_op == 3:
                            admin.check_bank_available_balance()
                        elif admin_op == 4:
                            admin.check_bank_given_loan()
                        elif admin_op == 5:
                            admin.turn_off_bank_loan_feature()
                        elif admin_op == 6:
                            admin.set_bank_to_bankrupt()
                        elif admin_op == 7:
                            break
                        else:
                            print("Invalid input")

                elif op == 2:  # login admin
                    name = input("Enter name: ")
                    password = input("Enter password: ")
                    admin = bank.login_admin(Admin(name, password, bank))
                    if admin:
                        while True:
                            print("1. Delete user account")
                            print("2. View all users account list")
                            print("3. View total bank balance")
                            print("4. View total bank loan amount")
                            print("5. Turn off loan feature")
                            print("6. Set bank to bank to bankrupt")
                            print("7. Exit")
                            admin_op = int(
                                input("Please choose your option: "))
                            if admin_op == 1:
                                user_acc_no = input("Enter user account no: ")
                                admin.delete_user_account(user_acc_no)
                            elif admin_op == 2:
                                admin.see_all_users()
                            elif admin_op == 3:
                                admin.check_bank_available_balance()
                            elif admin_op == 4:
                                admin.check_bank_given_loan()
                            elif admin_op == 5:
                                admin.turn_off_bank_loan_feature()
                            elif admin_op == 6:
                                admin.set_bank_to_bankrupt()
                            elif admin_op == 7:
                                break
                            else:
                                print("Invalid input")
                    else:
                        print("Wrong admin name or password")

                elif op == 3:
                    break
                else:
                    print("Invalid input")

        elif cmd == 2:  # continue as user
            while True:
                print("<--- User options --->")
                print("1. Create account")
                print("2. Login to user account")
                print("3. Exit")
                op = int(input("Select your option: "))
                if op == 1:  # create account
                    name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    account_type = input("Enter your account type: ")
                    user = User(name, email, account_type)
                    bank.add_account(user)
                    print(f"""Account created!\nYour account no: {
                          user.view_account_num()}""")
                    while True:
                        print("1. Deposit money")
                        print("2. Withdraw money")
                        print("3. Available balance")
                        print("4. Transaction history")
                        print("5. Take loan")
                        print("6. Transfer money")
                        print("7. Exit")
                        user_op = int(input("Select you option: "))
                        if user_op == 1:  # deposit
                            money = int(input("Enter amount: "))
                            user.deposit_money(money, bank, True)
                            print("Deposited!!!")
                        elif user_op == 2:  # withdraw
                            money = int(input("Enter amount: "))
                            user.withdraw_money(money, bank)
                        elif user_op == 3:  # available balance
                            print(f"""Account balance: {
                                  user.available_balance()}""")
                        elif user_op == 4:  # transaction history
                            user.show_all_transaction()
                        elif user_op == 5:  # take loan
                            money = int(input("Enter loan amount: "))
                            user.take_loan(bank, money)
                        elif user_op == 6:  # transfer money
                            account_no = input("Enter account no: ")
                            money = int(input("Enter amount: "))
                            user.transfer_money(account_no, money, bank)
                        elif user_op == 7:
                            break
                        else:
                            print("Invalid input")

                elif op == 2:  # login account
                    name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    user = bank.login_user(name, email)
                    if user:  # login success
                        while True:
                            print("1. Deposit money")
                            print("2. Withdraw money")
                            print("3. Available balance")
                            print("4. Transaction history")
                            print("5. Take loan")
                            print("6. Transfer money")
                            print("7. Exit")
                            user_op = int(input("Select you option: "))
                            if user_op == 1:  # deposit
                                money = int(input("Enter amount: "))
                                user.deposit_money(money, bank, True)
                                print("Deposited!!!")
                            elif user_op == 2:  # withdraw
                                money = int(input("Enter amount: "))
                                user.withdraw_money(money, bank)
                            elif user_op == 3:  # available balance
                                print(f"""Account balance: {
                                    user.available_balance()}""")
                            elif user_op == 4:  # transaction history
                                user.show_all_transaction()
                            elif user_op == 5:  # take loan
                                money = int(input("Enter loan amount: "))
                                user.take_loan(bank, money)
                            elif user_op == 6:  # transfer money
                                account_no = input("Enter account no: ")
                                money = int(input("Enter amount: "))
                                user.transfer_money(account_no, money, bank)
                            elif user_op == 7:
                                break
                            else:
                                print("Invalid input")
                    else:
                        print("Invalid user name or email")
                elif op == 3:
                    break
                else:
                    print("Invalid input")

        elif cmd == 3:
            break
        else:
            print("Invalid input")


runSystem()
