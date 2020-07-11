#Modules In Python

print("1 Hello ")
print("1 Name is ",__name__)
name = "Shivam"
def subtract(num1,num2):
    num3 = num1-num2
    return num3

class Mod:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        print("User Object Constructed")

    def show(self):
        print('{}\t{}\t{}\t'.format(self.name,self.phone,self.email))

def main():
    print("2 Hello ")
    print("2 Name is ", __name__)
    m1 = Mod("Shivam","897897456","Shivam@example.com")
    m1.show()

if __name__ == '__main__':
    main()
