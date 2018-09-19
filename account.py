class BankAccount:
    def __init__(self):
        self.bal = 0
        self.is_open = False
    

    def open(self):
        self.is_open = True

    def get_balance(self ):
        if  not self.is_open:
            raise ValueError ('not recognised')

        return self.bal

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError ('account closed')

        if amount < 0:
            raise ValueError ('invalid input:-ve values not allowed')

        self.bal += amount


    def withdraw(self, amount):
        if not self.is_open :
            raise ValueError ('account closed')

        if amount < 0:
            raise ValueError ('invalid input')

        if amount > self.bal:
            raise ValueError ('insufficient bal')

        self.bal -= amount

    def close(self):
        self.is_open = False