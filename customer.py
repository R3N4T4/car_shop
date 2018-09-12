class customer_class():
    def __init__(self, first_name, last_name, bank_account):
        self.first_name = first_name
        self.last_name = last_name
        self.bank_account = bank_account
        self.orderlist = []

class order():
    def __init__(self,model,amount,ordernumber):
        self.model = model
        self.amount = amount
        self.ordernumber = ordernumber
    # def __repr__(self):
    #     return 'order' + self.ordernumber

