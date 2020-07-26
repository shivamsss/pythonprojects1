import datetime as dt
class Fee:
    def __init__(self,rollno,amount):
        self.rollno = rollno
        self.amount = amount
        self.datetime = dt.datetime.today()

    def show_fee(self):
        print("{} | {} | {}".format(self.rollno, self.amount, self.datetime))


def main():
    fref1= Fee("101","2000")
    fref2 = Fee("102","3000")
    fref1.show_fee()
    fref2.show_fee()


if __name__ == '__main__':
  main()