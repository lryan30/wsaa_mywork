import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

sql = "SELECT * FROM student where id = %s"
val = (1,)

cursor.execute(sql, val)
result = cursor.fetchall()
for x in result:
    print(x)

