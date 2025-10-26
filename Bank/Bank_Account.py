
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initalAmount, actName):  # ایجاد سپرده
        self.balance = initalAmount
        self.name = actName
        print(f"\nAccount {self.name} create.\nbalance = {self.balance:.2f}")

    def getBalance(self):                      # موجودی حساب
        print(f"\nAccount {self.name} balance = {self.balance:.2f}")

    def deposit(self, amount):         # اضافه شدن مبلغ جدید به حساب(واریز)
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def checktransaction(self, amount):       # چک کردن موجودی حساب
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry account {self.name} only has balance of %{self.balance}")

    def withdrow(self, amount):       # برداشت از حساب
        try:
            self.checktransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdrow is completed")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdrow is intrrupted:{error}")

    def transfer(self, amount, accName):  # واریز به حساب شخص دیگر
        try:
            print("\n*****************\n")
            self.checktransaction(amount)
            self.withdrow(amount)
            accName.deposit(amount)
            print("\n****************\nTransfer completed")
        except BalanceException as error:
            print(f"\ntransfer is intrrupted:{error}")


# اضافه کردن 5درصد سود به موجودی کارت در صورت واریز مبلغ
class IntrestRewardAccount(BankAccount):

    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit Completed")
        self.getBalance()


class SavingAccount(IntrestRewardAccount):  # درصورت واریزی 5 درصد از حساب کسر شود
    def __init__(self, initalAmount, actName):
        super().__init__(initalAmount, actName)
        self.fee = 5

    def transfer(self, amount, accName):
        try:
            print("\n*****************\n")
            self.checktransaction(amount + self.fee)
            self.withdrow(amount + self.fee)
            accName.deposit(amount)
            print("\n*****************\n")
        except BalanceException as error:
            print(f"\nTransfer is intrrupted:{error}")
