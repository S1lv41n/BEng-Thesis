import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    database='inżynierka', 
                                    user='s1lv41n', 
                                    password='S1lv41nftw!', 
                                    auth_plugin='mysql_native_password')
cursor = connection.cursor()

db_info = connection.get_server_info()
print("Connected to MySQL Server version ", db_info)
cursor.execute("select database();")
record = cursor.fetchone()
print("Połączyłeś się z bazą:", record)

action = input("Co chcesz zrobić? \n 1. Dodaj rekord \n 2. Usuń rekord\n")

if action == "1":
    #TODO Add new columns in 'produkty' table
    #TODO prod_id by auto_increment
    prod_id = input("prod_id: ")
    nazwa = input ("nazwa: ")
    ilosc = input ("ilosc: ")
    mySql_insert_record = """INSERT INTO produkty (prod_id, nazwa, ilosc) VALUES (%s, %s, %s)"""
    cursor.execute(mySql_insert_record, (prod_id, nazwa, ilosc), multi=True)
    connection.commit()
    print("Rekord został pomyślnie dodany do tabeli Produkty")
    cursor.close()

if action == "2":
    prod_id = (input("prod_id: "), )
    print("Wyświetlam obecne wartości przed ich usunięciem: ")
    sql_select_record = """SELECT * FROM produkty WHERE prod_id = %s"""
    cursor.execute(sql_select_record, prod_id)
    record = cursor.fetchall()
    print(record)

    confirmation = input("Czy napewno chcesz usunąć ten rekord? y/n \n")
    
    if confirmation == "y":
        sql_delete_record = """DELETE from produkty WHERE prod_id = %s"""
        cursor.execute(sql_delete_record, prod_id)
        connection.commit()
        cursor.close()
        print("Rekord został pomyślnie usunięty")
        
    if confirmation == "n":
        print ("Rekord nie został usunięty")
        cursor.close()