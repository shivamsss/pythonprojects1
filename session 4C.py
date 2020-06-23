
# CRAVINGS: 40% Off upto Rs 100 | amount >=149
# JUMBO:    50% Off upto Rs 200 | amount >=500
# BINGO:    Flat 20% Off        | amount >=100
amount = int(input("Enter Amount Value: "))

if amount >= 100:

   discount1 = amount*0.40
   discount2 = amount*0.50
   discount3 = amount*0.20

   if amount>500:
     if discount1 > discount2:
         if discount1 > discount3:
            print("You should use CRAVINGS promo code")
         else:
            print('you should use BINGO promo code')

     else:
         if discount2 > discount3:
            print("you should apply JUMBO promo code")
         else:
            print('you should use BINGO promo code')

   elif amount>150:
       if discount1>discount3:
           print("you should apply CRAVINGS promo code")
       else:
           print("you should use BINGO promo code")
   elif amount>100:
       print("You should use BINGO  Promo code")
   else:
       print("You cannot use Any promo code")

   promoCode = input("Enter the Promo Code: ")




