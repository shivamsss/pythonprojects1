def name(name):
    print("My name is",name,id(name))

name('shivam')

def function1(num1,num2):
    num3 = num1+num2
    print('num3 is',num3)

function1(1,2)

name1 = name
print("name1 is ",name1,type(name1),id(name1))
name1('dave')