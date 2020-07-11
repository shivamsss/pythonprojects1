class Customer:
    def __init__(self,name,email,password):
       self.name = name;
       self.email =email;
       self.password= password;

    def show(self):
        print('{}\t{}\t{}\t'.format(self.name,self.email,self.password))


class PrimeCustomer(Customer):
    def __init__(self,customer):
        customer.prime = True
        customer.tilldate = "21/02/21"
