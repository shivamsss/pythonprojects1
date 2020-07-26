class Product:
    def __init__(self,name,brand,price):
        self.name=name
        self._brand = brand
        self.__price = price
    # def __showproduct(self):
    #     print('{}\t{}\t{}\t'.format(self.name,self.brand,self.price))

    def __str__(self):
        return "{} | {} | {}".format(self.name, self._brand, self.__price)



def main():
    pref = Product('xa','APPLE','55000')
    print(Product.__dict__)
#    pref._Product__showproduct()
    # pref.__showproduct()# cannot accessdue to private access modifiers
    print(pref.__dict__)
    #print(pref._brand)
    print(pref)


if __name__ == '__main__':
    main()