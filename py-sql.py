'''creating a basic login'''

from datetime import datetime


import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2004"
)

cursor = db.cursor()

def main_page(name):
    n = name
    print("main Page")
    msg = input("enter your message:")
    d = datetime.now()
    # insert = insert into %s values(%s,%s)
    # data = (d,msg)
    cursor.execute("insert into user.%s values('%s','%s')"%(n,d,msg))
    print("message savedsucessfully")
    


def sign_in():
    print("#"*100)
    print()
    print("sign-in\n")
    name = input("\nEnter your name:")
    pword = input("\nenter your password:")
    l=[];p=[]
    
    cursor.execute("select name from user.users")
    for i in cursor:
        l.extend(i)
    if name not in l:
        n = input("\ncheck your name \n 1.name \n 2.signup: \n")
        if(n=='1'):
            sign_in()
        else:
            signup()
    else:
        print("")
    statement = "select password from user.users where name='%s'"%name
    cursor.execute(statement)
    for i in cursor:
        # print(i[0])
        p.append(i[0])
        # print(p)
    if p[0]!=pword:
        # print(p[0])
        print("re-enter the password")
        n = input("want to signup\nyes \n2.signin")
        if(n=='2'):
            sign_in()
        else:
            signup()
    else:
        print("sign-in sucessfull") 
        
        print("Main Page")
        main_page(name)
            
            
def signup():
    print("#"*100)
    print()
    print("signUp")
    
    print("welcome to Notes\n")
    n = input("Are you want to \n1.sign_in(registered user) or \n2.sign_up(new user) \n")
    if(n=='1'):
        sign_in()
    else:
        print("\nSignUp")
        name = input("\nenter your name:\n")

        password = input("enter your password:\n")

        re_password = input("enter your password again:\n")
        
        if(password!=re_password):
            print("check again/n")
            signup()
        elif(password==re_password):
            insert = "insert into user.users(name,password,time) values(%s,%s,%s)"
            data = (name,password,datetime.now())
            cursor.execute(insert,data)
            print("signup sucessfully/n")
            statement_1 = "create table user.%s(time timestamp, msg varchar(200))"%name
            cursor.execute(statement_1)
        sign_in()
    
signup()
db.commit()
db.close()
