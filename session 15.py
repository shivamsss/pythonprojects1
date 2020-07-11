class User:
    def __init__(self):
        self.name = input("Enter Your name: ")
        self.phone = input("Enter your phoneno: ")
        self.email = input("Enter your email: ")

    def showdetails(self):
        print('{}\t{}\t{}\t'.format(self.name,self.phone,self.email))

    def savedata(self):
        file = open("data.csv","w")
        data = "{},{},{}\n".format(self.name, self.phone, self.email)
        file.write(data)
        file.close()
        print("data saved")




def main():
    user = User()
    user.showdetails()
    user.savedata()

if __name__ == '__main__':
    main()
