#Function inside a function
def login_google():
    print("Login through google")

def login_instagram():
    print("Login through instagram")

def login_facebook():
    print("Login through Facebook")


def login(login_type):
    login_type


choice = int(input("ENTER YOUR CHOICE"))
if choice==1:
    login(login_google())
elif choice==2:
    login(login_instagram())
elif choice==3:
    login(login_facebook())

else:
    print("Enter Correct Choice")
