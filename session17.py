import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("user.json")
firebase_admin.initialize_app(cred)

class Pass:
    def __init__(self,name,phone,email,fromlocation,tolocation,ispassgranted,familymembers,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.fromlocation = fromlocation
        self.tolocation = tolocation
        self.ispassgranted = ispassgranted
        self.familymembers = familymembers
        self.address = address

    def show(self):
        pass

def main():
    familymembers = ['kia','fionna']
    address={
        "line":8,
        "area":"Haibowal Kalan",
        "city":"Ludhiana"
    }

    pref  = Pass("shivam","8968263480","shivam@example.com","ludhiana","Jalandhar",True,familymembers,address)
    pref_dictionary = pref.__dict__
    print(pref_dictionary)

    db =firestore.client()
    db.collection('users').document(pref.phone).set(pref_dictionary)
    print("Data Saved")

if __name__ == '__main__':
    main()