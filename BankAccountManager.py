class Account:
    
    def __init__(self, acc_nbr, opening_balance):
        self.acc_nbr = acc_nbr
        self.balance = opening_balance

    def __str__(self):
        return f'{self.acc_nbr}\nBalance: {self.balance:.2f}\n'
    
    def deposit(self, dep_amnt):
        self.balance += dep_amnt

    def withdrawl(self, with_amnt):
        if with_amnt > self.balance:
            print('\nFunds Unavailable/low')
        else:
            self.balance -= with_amnt
            print('\nTransaction Sucessfull')
        
class Checking(Account):

    def __init__(self, acc_nbr, opening_deposit):
        super().__init__(acc_nbr, opening_deposit)

    def __str__(self):
        return f'Checking Account: {Account.__str__(self)}'

class Saving(Account):

    def __init__(self, saving_acc_nbr, opening_deposit):
        super().__init__(saving_acc_nbr, opening_deposit)

    def __str__(self):
        return f'Saving Account: {Account.__str__(self)}'

class Business(Account):

    def __init__(self, business_acc_nbr, opening_deposit):
        super().__init__(business_acc_nbr, opening_deposit)

    def __str__(self):
        return f'Business Account: {Account.__str__(self)}'

class Customer:

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.accts = {'C':[], 'S':[], 'B':[]}

    def __str__(self):
        return self.name

    def open_checking(self, acc_nbr, opening_deposit):
        self.accts['C'].append(Checking(acc_nbr, opening_deposit))
    
    def open_saving(self, acc_nbr, opening_deposit):
        self.accts['S'].append(Saving(acc_nbr, opening_deposit))
    
    def open_business(self, acc_nbr, opening_deposit):
        self.accts['B'].append(Business(acc_nbr, opening_deposit))

    def get_total_deposit(self):
        total = 0
        for accnt in self.accts['C']:
            print(accnt)
            total += accnt.balance
        for accnt in self.accts['S']:
            print(accnt)
            total += accnt.balance
        for accnt in self.accts['B']:
            print(accnt)
            total += accnt.balance
        print(f'Combined deposits in all accounts is: {total:.2f}\n')

class Trancacrions:
    def make_deposit(cust, acc_type, accnt_nbr, dep_amnt):
        for accnt in cust.accts[acc_type]:
            if accnt_nbr == accnt.acc_nbr:
                accnt.deposit(dep_amnt)
                return True
        return False

    def make_withdraw(cust, acc_type, accnt_nbr, with_amnt):
        for accnt in cust.accts[acc_type]:
            if accnt_nbr == accnt.acc_nbr:
                accnt.withdrawl(with_amnt)
                return True
        return False

    def create_accounts():
        for acc in range(123456, 1234567):
            yield acc

    def check_for_credentials(custm_list, name, pin):
        for custm in custm_list:
            if custm.name == name and custm.pin == pin:
                return custm
        return False