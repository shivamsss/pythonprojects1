class Shoe:
    def __init__(self,name,size,color,code):
        self.name = name
        self.size = size
        self.color = color
        self.code = code

    def showdetails(self):
        print("{}\n{}\n{}\n{}\n".format(self.name,self.size,self.color,self.code))



shoe1 = Shoe('nike',8,'red','111')
print(shoe1)
print(shoe1.__dict__)

shoe2 = Shoe()
# shoe2.showdetails()
# shoe1.brand = "Addidas"
# shoe1.size = 8
# shoe1.color = "black"
# shoe1.code = 101
#
# print("shoe1 are ",shoe1.__dict__)