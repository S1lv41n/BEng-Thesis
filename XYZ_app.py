import sys
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    database='inżynierka', 
                                    user='s1lv41n', 
                                    password='S1lv41nftw!', 
                                    auth_plugin='mysql_native_password')
cursor = connection.cursor()


def main():    
    mainMenuInput = mainMenu()
    if mainMenuInput == 1:
        menuProdukty()
        
    elif mainMenuInput == 2:
        menuPracownicy()
        
    elif mainMenuInput == 3:
        menuMagazyn()
        
    else:
        print("\nWybierz poprawną opcję\n")
        main()


def welcome():
    print ("Witamy w aplikacji XYZ")
    db_info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_info)
    cursor.execute("select database();")
    record = cursor.fetchone()


def mainMenu():
    mainMenuInput = int(input("""Wybierz rejestr:\n 1. Rejestr produktów\n 2. Rejestr pracowników\n 3. Rejestr magazynowy\n 0. Wyjście z programu\n"""))
    if mainMenuInput == 0:
        print("\nZakończone pracę z programem")
        sys.exit()
    return mainMenuInput

def menuProdukty():
    menuProduktyInput = int(input("""Wybierz akcję:\n 1. Wyświetlenie tabeli produktów\n 2. Dodawanie produkt\n 3. Edycja produkt\n 0. Wstecz\n"""))
    if menuProduktyInput == 0:
        mainMenu()
        
    elif menuProduktyInput == 1:
        print("\n\n")
        query = ("SELECT prod_id, nazwa, norma, skladowe, jm, prog_bezpieczny FROM produkty")
        cursor.execute(query)
        rows = cursor.fetchall()
        result = len(rows)
        print ("PROD_ID  NAZWA  NORMA/H   SKŁADOWE   JM   PRÓG BEZPIECZNY")
        if result > 0:
            x = 0
            for row in rows:
                row = rows[x]
                prod_id, nazwa, norma = row[0], row[0], row[0]
                print (row)
                x = x + 1
        print("\n\n")
        menuProdukty()
        
    elif menuProduktyInput == 2:
        #TODO Add new columns in 'produkty' table
        nazwa = input ("nazwa: ")
        norma = input ("norma: ")
        skladowe = input ("skladowe: ")
        jm = input ("jm: ")
        prog_bezpieczny = input ("prog_bezpieczny: ")
        mySql_insert_record = """INSERT INTO produkty (nazwa, norma, skladowe, jm, prog_bezpieczny)VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(mySql_insert_record, (nazwa,  norma, skladowe, jm, prog_bezpieczny), multi=True)
        connection.commit()
        print("Rekord został pomyślnie dodany do tabeli Produkty\n")
        
    else:
        return menuProduktyInput

def menuPracownicy():
    menuPracownicyInput = int(input("""Wybierz akcję:\n 1. Wyświetlenie tabeli pracowników\n 2. Dodawanie pracownika\n 3. Edytuj pracownika\n 0. Wstecz\n"""))
    if menuPracownicyInput == 0:
        mainPracownicy()
        
    else:    
        return menuPracownicyInput

def menuMagazyn():
    menuMagazynInput = int(input("""Wybierz akcję:\n 1. Wyświetlenie stanów magazynowych\n 2. Dodawanie stanu magazynowego\n 3. Edycja stanu magazynowego\n 0. Wstecz\n"""))
    if menuMagazynInput == 0:
        mainMagazyn()
        
    else:    
        return menuMagazynInput

##def program(action):
##    if action == 1:
##        print("\n\n")
##        query = ("SELECT prod_id, nazwa, norma, ilosc FROM produkty JOIN magazyn ON produkty.id_zasobu=magazyn.id_zasobu")
##        cursor.execute(query)
##        rows = cursor.fetchall()
##        result = len(rows)
##        print ("PROD_ID  NAZWA  NORMA/H   ILOŚĆ ")
##        if result > 0:
##            x = 0
##            for row in rows:
##                row = rows[x]
##                prod_id, nazwa, norma = row[0], row[0], row[0]
##                print (row)
##                x = x + 1
##        print("\n\n")
#
#    if action == 3:
#        prod_id = (input("prod_id: "), )
#        print("Wyświetlam obecne wartości przed ich usunięciem: ")
#        mySql_select_record = """SELECT * 
#                            FROM produkty 
#                            WHERE prod_id = %s"""
#        cursor.execute(mySql_select_record, prod_id)
#        record = cursor.fetchall()
#        print(record)
#
#        confirmation = input("Czy napewno chcesz usunąć ten rekord? y/n \n")
#        
#        if confirmation == "y":
#            mySql_delete_record = """DELETE from produkty 
#                                WHERE prod_id = %s"""
#            cursor.execute(mySql_delete_record, prod_id)
#            connection.commit()
#            print("Rekord został pomyślnie usunięty\n")
#            
#        if confirmation == "n":
#            print ("Rekord nie został usunięty\n")
#
#    #TODO Editing
#    if action == 4:
#        prod_id = (input("prod_id: "), )
#        print("Wyświetlam obecne wartości przed ich edytowaniem: ")
#        mySql_select_record = """SELECT * 
#                            FROM produkty 
#                            WHERE prod_id = %s"""
#        cursor.execute(mySql_select_record, prod_id)
#        record = cursor.fetchall()
#        print(record)
#        
#        confirmation = input("Czy napewno chcesz edytować ten rekord? y/n \n")
#        
#        if confirmation == "y":
#            print("Podaj nowe wartości rekordu: \n")
#            prod_id = input("prod_id: ")
#            nazwa = input("nazwa: ")
#            norma = input(" norma: ")
#            dane = (nazwa, norma, prod_id)   
#            mySql_update_record = ("""UPDATE produkty 
#                                SET nazwa = %s, norma = %s 
#                                WHERE prod_id = %s""")
#            cursor.execute(mySql_update_record, (nazwa, norma, prod_id))
#            connection.commit() 
#            print("Rekord został pomyślnie edytowany\n")
#            
#        if confirmation == "n":
#            print ("Rekord nie został edytowany\n")
#
welcome()            
main()