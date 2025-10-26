from Bank_Account import *


Pardis = BankAccount(1000,"pardis")
Mahdi  = BankAccount(2000,"mahdi")


Pardis.getBalance()
Mahdi.getBalance()

Pardis.deposit(800)
Mahdi.deposit(300)


Pardis.withdrow(500)

Pardis.transfer(800,Mahdi)

Pardis = SavingAccount(1000,"pardis")
Pardis.transfer(500,Mahdi)
