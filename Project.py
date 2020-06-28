print("++++++++++++++++++WELCOME TO ICE CREAM STUDIO++++++++++++++++++++++++++++++")
print()
print("============MENU=======================")

Menu = {
    'ChocolateOreo':150,
    'MangoMania':160,
    'ChocoChip':200,
    'KitKat':   120,
    'MintOreo':170,
    'MangoIC':200,
    'Blackcurrent':220
}
for key in Menu:
    value = Menu[key]

    print("{}\t{}".format(key, value))

print()
order = input(" Enter your Order ")
#print(" Your Order is",order)

quantity = int(input((" Enter Quantity of Item ")))


item_cart = []
item_cart.append(Menu[order]*quantity)
print("Your Cart Price is :",item_cart)
print("Do you Want To Enter More Press yes If ")

choice = input("")
while choice =="yes":
    order1 = input('Enter Your Order :')
    quantity = int(input((" Enter Quantity of Item ")))
    item_cart.append(Menu[order1]*quantity)
    choice = input("Would You Like to Add Another Item?  (yes/no): ")

print(item_cart)
pay_bill = 0
for i in item_cart:
    pay_bill = pay_bill+i

promocode = input("Do you Have Any promo code: ")

if(promocode == 'NEWUSER'):
    print("Your Payable Amount is :",(pay_bill-50))

elif(promocode == 'GOLDDAYS'):
    print("your Payable Amount is :",(pay_bill-70))

else:
    print("Your Payable Amount is :",pay_bill)


if pay_bill>350:
    print("You Get A Free Cup of choclate Ice Cream")
else:
    print('Thank You')