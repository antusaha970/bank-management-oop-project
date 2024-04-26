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
