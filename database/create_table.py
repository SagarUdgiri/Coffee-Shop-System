import mysql.connector
q="create table Bill(order_id int(8),p_name varchar(30),price int(4),quan int(4),amnt int(8))"
q1="create table login(ID int(5),username varchar(20),password varchar(20))"
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database="Shop")
cur=con.cursor()
cur.execute(q)
cur.execute(q1)
con.commit()
print("created")
cur.close()
con.close()
