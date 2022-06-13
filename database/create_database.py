import mysql.connector
q="create database Shop"
con=mysql.connector.connect(host='localhost',user='root',passwd='root')
cur=con.cursor()
cur.execute(q)
con.commit()
print("created")
cur.close()
con.close()
