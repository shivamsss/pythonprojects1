import mysql.connector as db
class User:
    def __init__(self):
        pass

    # def registerUser(self):
    #     self.name = input("Enter your name : ")
    #     self.phone = input("Enter your phone : ")
    #     self.email = input("Enter your email : ")
    #
    #     sql = "insert into user1 values(null,'{}','{}','{}')".format(self.name,self.phone,self.email)
    #     connection = db.connect(user="root",password="",database="session16",host="127.0.0.1", port="3306")
    #     cursor = connection.cursor()
    #     cursor.execute(sql)
    #     connection.commit()
    #     print("User saved in database")
    def updateUser(self):
        self.uid = int(input("Enter User's UID: "))
        self.name = input("Update Name")
        self.phone = input("update Phone")
        self.email = input("update email")

        sql = "update user1 set name='{}',phone='{}',email='{}'where uid={}".format(self.name,self.phone,self.email,self.uid
                                                            )

        connection = db.connect(user="root", password="", database="session16", host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print("User updated in database")

    def fetchuser(self):
        sql = "select * from user1"
        connection = db.connect(user="root", password="", database="session16", host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0],row[1],row[2],row[3])
    def show(self):
        print('{}\t{}\t{}\t'.format(self.name,self.phone,self.email))


def main():
    user = User()
#    user.registerUser()
#    user.updateUser()
    user.fetchuser()
    user.show()

if __name__ == '__main__':
   main()
