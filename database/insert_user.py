import mysql.connector,random
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database="Shop")
user=input("Enter user Name:")
passw=input("Password:")
Id=random.randrange(1,100)
q=f"insert into login values({Id},'{user}','{passw}')"
cur=con.cursor()
cur.execute(q)
con.commit()
print("inserted")
cur.close()
con.close()
