one_plus_day_1_sales = 100
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profite_of_amazon_on_oneplus = 200.27
disc_from_sbi_to_oneplus = 3000.12

home_app1_day_sale = 120
home_appl_day2_sales = 220
home_appl_day3_sales = 180

profits_to_amazon_from_home_appl = 50

discounts_from_sbi_to_home_appl = 3000.12

total_oneplus_profits = (one_plus_day_1_sales+one_plus_day_2_sales+one_plus_day_3_sales)*profite_of_amazon_on_oneplus

print("total profits by amazon on oneplus",total_oneplus_profits)

total_homeapp_profits = (home_app1_day_sale+home_appl_day2_sales+home_appl_day3_sales)*profits_to_amazon_from_home_appl

print("total profits by amazon on homeapp",total_homeapp_profits)


total_sales_of_oneplus = one_plus_day_1_sales+one_plus_day_2_sales+one_plus_day_3_sales
total_sales_of_homeapp = home_app1_day_sale+home_appl_day2_sales+home_appl_day3_sales

if total_sales_of_oneplus>total_sales_of_homeapp:
    print("Sbi should invest in selling credit cards to mobile shops")
else:
    print("sbi should invest in selling credit cards to home appliances shopes")






