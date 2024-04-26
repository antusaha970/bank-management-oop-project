from user import User
from bank import Bank
from admin import Admin


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
                        print("5. Turn of loan feature")
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
                            print("3. View all total bank balance")
                            print("4. View all total bank loan amount")
                            print("5. Turn of loan feature")
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
