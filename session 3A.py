products = {
    "iphone": 50000,
    "usb": 500,
    "charger": 1200,
    "chips": 50,
    "shoe": 3000,
    "jeans": 1000,
    "tshirt": 800
}

menu = {
    "dal": 200,
    "paneer": 400,
    "noodles": 200,
    "manchurian": 250,
    "sandwich": 100
}
cart = []
product = input("Enter Product of Your Choice:")
cart.append(products[product])
product = input("Enter Product of Your Choice:")
cart.append(products[product])
print("Cart:", cart)