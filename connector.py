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

action = input("""Co chcesz zrobić?\n 
1. Wyświetl bazę 
2. Dodaj rekord  
3. Usuń rekord 
4. Edytuj rekord\n""")

if action == "1":
    query = ("SELECT * FROM produkty")
    cursor.execute(query)
    rows = cursor.fetchall()
    result = len(rows)
    if result > 0:
        x = 0
        for row in rows:
            row = rows[x]
            prod_id, nazwa, ilosc = row[0], row[0], row[0]
            print (row)
            x = x + 1
        cursor.close()

if action == "2":
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


if action == "3":
    prod_id = (input("prod_id: "), )
    print("Wyświetlam obecne wartości przed ich usunięciem: ")
    sql_select_record = """SELECT * 
                        FROM produkty 
                        WHERE prod_id = %s"""
    cursor.execute(sql_select_record, prod_id)
    record = cursor.fetchall()
    print(record)

    confirmation = input("Czy napewno chcesz usunąć ten rekord? y/n \n")
    
    if confirmation == "y":
        sql_delete_record = """DELETE from produkty 
                            WHERE prod_id = %s"""
        cursor.execute(sql_delete_record, prod_id)
        connection.commit()
        cursor.close()
        print("Rekord został pomyślnie usunięty")
        
    if confirmation == "n":
        cursor.close()
        print ("Rekord nie został usunięty")

if action == "4":
    prod_id = (input("prod_id: "), )
    print("Wyświetlam obecne wartości przed ich edytowaniem: ")
    sql_select_record = """SELECT * 
                        FROM produkty 
                        WHERE prod_id = %s"""
    cursor.execute(sql_select_record, prod_id)
    record = cursor.fetchall()
    print(record)
    
    confirmation = input("Czy napewno chcesz edytować ten rekord? y/n \n")
    
    if confirmation == "y":
        print("Podaj nowe wartości rekordu: \n")
        prod_id = input("prod_id: ")
        nazwa = input("nazwa: ")
        ilosc = input("ilosc: ")
        dane = (nazwa, ilosc, prod_id)   
        sql_update_record = ("""UPDATE produkty 
                            SET nazwa = %s, ilosc = %s 
                            WHERE prod_id = %s""")
        cursor.execute(sql_update_record, (nazwa, ilosc, prod_id))
        connection.commit()
        cursor.close()  
        print("Rekord został pomyślnie edytowany")
        
    if confirmation == "n":
        cursor.close()
        print ("Rekord nie został edytowany")

else:
    print("Wybierz poprawną instrukcję")