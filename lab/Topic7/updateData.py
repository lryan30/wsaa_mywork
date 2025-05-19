import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()
sql = "UPdATE student SET name = %s, age = %s WHERE id = %s"
val = ("Mary", 22, 1)
cursor.execute(sql, val)
db.commit()
print('updated', cursor.rowcount, "record(s)")
cursor.close()
db.close()
# connection.close()
