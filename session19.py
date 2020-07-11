#map
def discount(amount):
    return amount -amount*0.20

product_prices = [100,200,300,400]

lref1= lambda amount:amount - amount*0.20

for price in product_prices:
    print(lref1(price))

print("=========================================")
result = map(discount,product_prices)
print(result)

result = map(lref1,product_prices)
print(result)
print(list(result))

print("++++++++++++++++++++++++++++++++++++++++++++")

numbers = list(range(10,21))
print(numbers)

l1 = lambda num1:num1%2 ==0
l2 = lambda num1:num1%2 !=0
print(list(map(l1,numbers)))
print(list(map(l2,numbers)))
print("-----------------------------------------------------")

print(list(filter(l1,numbers)))
print(list(filter(l2,numbers)))


l3 = lambda X, Y: X + Y
from functools import reduce

nums = [10, 20, 30, 40, 50]
result = reduce(l3, nums)
print(result)
