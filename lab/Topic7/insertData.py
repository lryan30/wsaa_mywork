import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()
sql = " insert into student (name, age) values (%s, %s)"
val = ("Mary", 21)

cursor.execute(sql, val)
db.commit()
print(cursor.lastrowid, "record inserted.")

cursor.close()
db.close()            
#connection.close()  