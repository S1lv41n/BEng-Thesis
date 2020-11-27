import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost', database='inżynierka', user='s1lv41n', password='S1lv41nftw!', auth_plugin='mysql_native_password')

db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)