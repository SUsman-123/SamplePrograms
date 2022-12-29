class Bank:
    def __init__(self,name,available_bal):
        self.name=name
        self.available_bal=available_bal
    def withdraw(self,amount):
        if amount > self.available_bal:
            try:
                0 / 0
            except:
                print("Not available balance")
        else:
            self.available_bal -= amount
            print("withdraw process completed")
    def deposit(self,amount):
        if amount > 1000:
            try:
                0 / 0
            except:
                print("limite exceed")
        else:
            self.available_bal +=amount
            print("deposit sucessfully")
    def balance(self):
        print("Total balance is {}".format(self.available_bal))
obj1=Bank('usman',700)
obj1.withdraw(500)
obj1.deposit(2000)
obj1.balance()







