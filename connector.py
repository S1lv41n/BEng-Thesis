import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost', database='inżynierka', user='s1lv41n', password='S1lv41nftw!', auth_plugin='mysql_native_password')

db_info = connection.get_server_info()
print("Connected to MySQL Server version ", db_info)
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("Połączyłeś się z bazą: ", record)

mySql_insert_record = """INSERT INTO produkty (prod_id, nazwa, ilosc, wlasciwosci, rodzaj)                          VALUES 
                           (1, 'Produkt A', 3, 'przykładowy Produkt A', 1)"""

cursor = connection.cursor()
cursor.execute(mySql_insert_record)
connection.commit()
print(cursor.rowcount, "Rekord został pomyślnie dodany do tabeli Produkty")
cursor.close()