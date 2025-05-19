import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()
sql = "DELETE FROM student where id = %s"
val = (4,)

cursor.execute(sql, val)
db.commit()
print('deleted', cursor.rowcount, "record(s)")
cursor.close()
db.close()
