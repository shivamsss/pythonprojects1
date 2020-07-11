menu = {
    101: 30, # Samsosa
    201: 50, # Tikki
    301: 100,# Noodles
    401: 120,# Burger
    501: 150 # Manchurian
}

class Order:
    order_id = 0
    def __init__(self):
        Order.order_id +=1
        self.oid = Order.order_id
        self.customer_name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.order_items = []
        choice = "yes"
        while choice =="yes":
            id = int(input("Enter Item ID: "))
            self.order_items.append('{}:{}'.format(id,menu[id]))
            choice = input("Do you want to Add more items yes/no")
    def showOrder(self):
        print('{}\t{}\t{}\t'.format(self.oid,self.customer_name,self.phone))
        print(self.order_items)
    def saveorder(self):
        file = open('customer.csv',"a")
        data = '{},{},{},{}\n'.format(self.oid,self.customer_name,self.phone,self.order_items)
        file.write(data)
        file.close()
        print("order saved")

    def readorder(self):
        file = open("customer.csv","r")
        lines = file.readline()
        for line in lines:
            data = line.split(",")
            for i in range(0, len(data)):
                print(data[i], end=" ")

            print()
        print("Order read")
        file.close()

choice = "yes"
while choice == "yes":
  order1 = Order()
  order1.showOrder()
  order1.saveorder()
  order1.readorder()
  choice = input("Add Next Order (yes/no):")



