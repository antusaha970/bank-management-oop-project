from user import User
from bank import Bank
from admin import Admin


def runSystem():
    bank = Bank()
    while True:
        print("<--- Welcome to the bank --->")
        print("1. Continue as admin")
        print("2. Continue as user")
        print("3. Exit")
        cmd = int(input("please enter an option: "))
        if cmd == 1:
            while True:
                print("1. Create and admin account")
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
                        print("3. View all total bank balance")
                        print("4. View all total bank loan amount")
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

        elif cmd == 2:
            pass
        elif cmd == 3:
            break
        else:
            print("Invalid input")


runSystem()
