from database import get_connection


def add_users():
            conn=get_connection()
            cursor=conn.cursor()
            username=input("Enter your username : ")
            password=input("Ente your password : ")
            role=input("Enter your role : ").lower()
            query="insert into users (username,password,role) values (%s,%s,%s)"
            values=(username,password,role)
            cursor.execute(query,values)
            conn.commit()
            print("User added successfully...")

def login():
      conn=get_connection()
      cursor=conn.cursor()
      username=input("Enter your username : ")
      password=input("Enter your password : ")
      query="select * from users where username=%s and password=%s"
      values=(username,password)
      cursor.execute(query,values)
      row=cursor.fetchone()
       
      if row:
            print("Login Successfull...")
            return row[3]
                 
      else:
            print("Invalid Credentials!!!")
            return None
     

