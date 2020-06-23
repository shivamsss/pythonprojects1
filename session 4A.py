username = "shivam.ss2727@gmail.com"
password = "shivam"

print("user authentication 1",(username == "shivam.ss2727@gmail.com"))
print("user authentication 2",password == "shivam")

otp = "1234"
userotp = input("enter Otp ")

print("otp is",(otp == userotp))

# Assignment 2

name = "shivam"
my_name ="shivam"
# in this case both the value have same id so both value are true
# == checks equality where as is operator checks the hashcode or object reference
print(id(name))
print(id(my_name))

if my_name == name:
    print('true')
else:
    print("false")

if my_name is name:
    print('true')
else:
    print('false')
