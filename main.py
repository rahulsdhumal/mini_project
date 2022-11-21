# *********3 day weakend schedule for preparation of python certification Exam**********
# 3)21/11/2022-Monday
# 	*1)Read and study carefully the Bank Account project
# 	*2)Try to solve the Bank Account project with json
# 	*3)Expect min 9 hour quality study

from BankAccountManager import Customer,Trancacrions
class Main:
    def execute(self):
        account_nbr = Trancacrions.create_accounts()
        customers_list = []
        while True:
            print('*******Welcome to the Bank*******')
            select = int(input('Select the service:\n 1. Banking\n 2. ATM\n 3. Exit\n'))
            if select not in (1, 2, 3):
                print('Plsease select the valid option')
                continue
            if select == 3:
                exit()
            while True and select == 1:
                option = int(input('How Can We Assist you\nPlease enter your options:\n 1: Open a new Account\n 2: Deposit money into your account\n 3: Exit the Bank\n'))
                if option not in (1, 2, 3):
                    print('Please select the valid option')
                    continue
                if option == 3:
                    exit()
                if option == 1:
                    exist_custm = int(input('Are you an existing customer ?\n 1. yes\n 2. no\n'))
                    if exist_custm not in (1, 2):
                        print('Please select the valid option')
                        continue
                try:
                    name = input('Please enter your name\n')
                    pin = int(input('Please enter a four digit Pin\n'))
                    acc_type = input('Please enter the type of account you want to open:\nChecking: "C", Saving: "S", Business: "B"\n')
                    if option == 2:
                        accnt_nbr = int(input('Please Enter your Account number\n'))
                    opening_deposit = int(input('Enter the amount you want to deposite\n'))
                except TypeError:
                    print('Information you entered is not in order! Please try again')
                    continue
                else:
                    if option in (1,2):
                        custm = Trancacrions.check_for_credentials(customers_list, name, pin)
                    if option == 2:
                        if custm:
                            Trancacrions.make_deposit(custm, acc_type.upper(), accnt_nbr, opening_deposit)
                            print(f'Name: {name}')
                            customers.get_total_deposit()
                        else:
                            print('Entered Credentials didnot match, Please re try')
                    else:
                        if exist_custm == 2:
                            customers = Customer(name, pin)
                        elif custm:
                            customers = custm
                        else:
                            print('Entered Credentials didnot match, Please re try')
                            continue
                        if acc_type.upper() == 'C':
                            customers.open_checking(next(account_nbr), opening_deposit)
                        elif acc_type.upper() == 'S':
                            customers.open_saving(next(account_nbr), opening_deposit)
                        elif acc_type.upper() == 'B':
                            customers.open_business(next(account_nbr), opening_deposit)
                        else:
                            print('Failed to open an Account!\nPlease select the proper account type\n')
                            continue
                        customers_list.append(customers)
                        print(f'Congratulations Account has been created Sucessfully\nName: {name}\n')
                        customers.get_total_deposit()
            while True and select == 2:
                print('*****Welcome to the ATM Service*****')
                option = int(input('\nHow Can We Assist you\nPlease enter your options:\n 1: Withdraw money from ATM\n 2: Exit the Bank\n'))
                if option not in (1, 2): 
                    print('Plsease select the valid option')
                    continue
                if option == 2:
                    break
                try:
                    name = input('Please enter your name\n')
                    acc_type = input('Please enter the type of account:\nChecking: "C", Saving: "S", Business: "B"\n')
                    accnt_nbr = int(input('Please Enter your Account number\n'))
                    pin = int(input('Please enter a four digit Pin\n'))
                    withdraw_amnt = int(input('Enter the amount you want to withdraw\n'))
                except TypeError:
                    print('Information you entered is not in order! Please try again')
                    continue
                else:
                    custm = Trancacrions.check_for_credentials(customers_list, name, pin)
                    if custm:
                        Trancacrions.make_withdraw(custm, acc_type.upper(), accnt_nbr, withdraw_amnt)
                        print(f'Available balance:\nName: {name}')
                        custm.get_total_deposit()
                    else:
                        print('Entered Credentials didnot match, Please re try')
if __name__ == '__main__':
    obj=Main()
    obj.execute()