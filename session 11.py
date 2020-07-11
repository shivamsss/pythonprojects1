#OOPs concept
class Payment:
    pass


payment1 = Payment()
payment2 = Payment()
print("Payment 1 is :",payment1,id(payment1))
print("Payment 2 is :",payment2,id(payment2))

payment3 = payment1
payment1.name = "Shivam"
payment1.amount = 5000
payment1.time = 19.00



print("Payment 1 is :",payment1.__dict__)
# print("Payment 3 is :",payment3,id(payment3))

payment1.amount = 7000
del payment1.time
print("Payment 1 is :",payment1.__dict__)
