import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sdutta",
  password="pass"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)