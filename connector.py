import mysql.connector

connection = mysql.connector.connect(host='localhost', database='inżynierka', user='s1lv41n', password='S1lv41nftw!', auth_plugin='mysql_native_password')
cursor = connection.cursor()

db_info = connection.get_server_info()
print("Connected to MySQL Server version ", db_info)
cursor.execute("select database();")
record = cursor.fetchone()
print("Połączyłeś się z bazą:", record)

action = input("Co chcesz zrobić? \n 1. Dodaj rekord \n 2. Usuń rekord\n")

if action == "1":
    values = input("Podaj wartości rekordu: ")
    mySql_insert_record = "INSERT INTO produkty (prod_id, nazwa, ilosc, wlasciwosci, rodzaj) VALUES (1, 'Produkt A', 3, 'przykładowy Produkt A', 1)"
    cursor.execute(mySql_insert_record)
    connection.commit()
    print(cursor.rowcount, "Rekord został pomyślnie dodany do tabeli Produkty")
    cursor.close()

if action == "2":
    print("Wyświetlam obecne wartości przed ich usunięciem: ")
    sql_select_record = """SELECT * FROM produkty WHERE prod_id = 1"""
    cursor.execute(sql_select_record)
    record = cursor.fetchone()
    print(record)

    sql_delete_record = """DELETE from produkty WHERE prod_id = 1"""
    cursor.execute(sql_delete_record)
    connection.commit()

    cursor.execute(sql_select_record)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Rekord został pomyślnie usunięty")