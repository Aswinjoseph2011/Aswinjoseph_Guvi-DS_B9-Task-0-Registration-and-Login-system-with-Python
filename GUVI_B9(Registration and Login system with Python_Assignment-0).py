import mysql.connector
con = mysql.connector.connect(host="localhost",user="root", password="",database="aswin")
cur = con.cursor()


def Registration():
    import re
    username = input("Enter the username: ")

    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if (re.search(regex, username)):
        print("User saved")
        Password = input("Enter the password:")
        if (len(Password) >= 16):
            print("Enter the correct password")
        elif not re.search("[a-z]", Password):
            print("Enter the correct password")
        elif not re.search("[A-Z]", Password):
            print("Enter the correct password")
        elif not re.search("[0-9]", Password):
            print("Enter the correct password")
        elif re.search("\s", Password):
            print("Enter the correct password")
        else:
            query = "insert into registration_and_login (User_creditional,Password) values (%s, %s)"

            data = (username, Password)
            cur.execute(query, data)
            con.commit()
            print("Password saved")
    else:
        print("Invalid Email Please enter with valid credential ")



def  forget_Password():
    username=input("Enter the User name:")
    import re
    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if (re.search(regex, username)):
        cur.execute("""select Password from registration_and_login where User_creditional =\"""" + username + """\";""")
        Password = cur.fetchone()
        print(Password)
        login()

    else:
        print("Invalid Email Please enter with valid credential ")
        Registration()



def Forget_Password1():
    while (True):
        print("1. Forget_Password")
        print("2. Register")
        a = int(input("Enter the number: "))
        if a == 1:
            forget_Password()
        elif a == 2:
            Registration()





def login():
    username=input("Enter the User name:")
    import re
    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if (re.search(regex,username)):
        cur.execute( """select User_creditional from registration_and_login where User_creditional =\"""" + username + """\";""")
        username = cur.fetchone()
        for i in username:
            a=i
            print(a)
            if a != None:
                Password = input("Enter the password:")
                if (len(Password) >= 16):
                    print("Enter the correct password")
                    Forget_Password1()
                elif not re.search("[a-z]", Password):
                    print("Enter the correct password")
                    Forget_Password1()
                elif not re.search("[A-Z]", Password):
                    print("Enter the correct password")
                    Forget_Password1()
                elif not re.search("[0-9]", Password):
                    print("Enter the correct password")
                    Forget_Password1()
                elif re.search("\s", Password):
                    print("Enter the correct password")
                    Forget_Password1()
                else:
                    cur.execute(
                        """select Password from registration_and_login where Password =\"""" + Password + """\";""")
                    Password = cur.fetchone()
                    if Password != None:
                        print("Login Sucessfull")
    else:
        print("Invalid Email Please enter with valid credential ")
        login()


while(True):
    print("1.Registration")
    print("2. Login")
    a= int(input("Enter_The_Number:"))
    if a==1:
        Registration()
    elif a==2:
        login()
    else:
        break



