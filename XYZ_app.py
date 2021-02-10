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
    if mainMenuInput == '1':
        menuProdukty()
        
    elif mainMenuInput == '2':
        menuPracownicy()
        
    elif mainMenuInput == '3':
        menuMagazyn()
        
    else:
        print("\nWybierz poprawną opcję\n")

    main()


def welcome():
    print ("Witamy w aplikacji XYZ")
    db_info = connection.get_server_info()
    print("Wersja serwera MySQL ", db_info)
    cursor.execute("select database();")
    record = cursor.fetchone()


def mainMenu():
    mainMenuInput = input("""Wybierz rejestr:\n 1. Obsługa rejestru produktów\n 2. Zarządzanie pracownikami\n 3. Zarządzanie stanami magazynowymi\n 0. Wyjście z programu\n\n--> """)
    if mainMenuInput == '0':
        print("\nZakończone pracę z programem")
        sys.exit()
    return mainMenuInput

def menuProdukty():
    menuProduktyInput = input("""Wybierz akcję:\n 1. Wyświetl wszystkie produkty w bazie\n 2. Dodaj produkt\n 3. Edytuj produkt\n 0. Wstecz\n\n--> """)
    if menuProduktyInput == '0':
        main()
        
    elif menuProduktyInput == '1':
        print("\n\n")
        query = ("SELECT prod_id, nazwa, norma, skladowe, jm, prog_bezpieczny FROM produkty")
        cursor.execute(query)
        rows = cursor.fetchall()
        result = len(rows)
        print ("ID  NAZWA  NORMA/H   SKŁADOWE   JM   PRÓG BEZPIECZNY")
        if result > 0:
            x = 0
            for row in rows:
                row = rows[x]
                prod_id, nazwa, norma = row[0], row[0], row[0]
                print (row)
                x = x + 1
        print("\n\n")
        menuProdukty()
        
    elif menuProduktyInput == '2':
        #TODO Add new columns in 'produkty' table
        nazwa = input ("nazwa:\n-->")
        norma = input ("norma:\n-->")
        skladowe = input ("skladowe:\n-->")
        jm = input ("jm:\n-->")
        prog_bezpieczny = input ("prog_bezpieczny:\n-->")
        mySql_insert_record = """INSERT INTO produkty (nazwa, norma, skladowe, jm, prog_bezpieczny)VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(mySql_insert_record, (nazwa,  norma, skladowe, jm, prog_bezpieczny), multi=True)
        connection.commit()
        print("Rekord został pomyślnie dodany do tabeli Produkty\n")
        
    else:
        print("\nWybierz poprawną opcję\n")
        return menuProdukty()

def menuPracownicy():
    menuPracownicyInput = input("""\nWybierz akcję:\n 1. Wyświetl wszystkich pracowników\n 2. Dodaj pracownika\n 3. Edytuj pracownika\n 0. Wstecz\n\n--> """)
    if menuPracownicyInput == '0':
        main()
        
    elif menuPracownicyInput == '1':
        print("\n\n")
        query = ("SELECT * FROM pracownicy")
        cursor.execute(query)
        rows = cursor.fetchall()
        result = len(rows)
        print ("ID   IMIĘ   NAZWISKO   CZAS PRACY   ZMIANA   OBECNE ZAMOWIENIE   ROLA")
        if result > 0:
            x = 0
            for row in rows:
                row = rows[x]
                prod_id, nazwa, norma = row[0], row[0], row[0]
                print (row)
                x = x + 1
        print("\n\n")
        menuProdukty()
        
    elif menuProduktyInput == '2':
        imie = input ("imię:\n-->")
        nazwisko = input ("nazwisko:\n-->")
        czas_pracy = input ("czas pracy:\n-->")
        zmiana = input ("zmiana\n-->")
        obecne_zamowienie = input ("obecne zamówienie:\n-->")
        rola = input ("rola:\n-->")
        mySql_insert_record = """INSERT INTO pracownicy (imie, nazwisko, czas_pracy, zmiana, obecne_zamowienie, rola)VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(mySql_insert_record, (imie, nazwisko, czas_pracy, zmiana, obecne_zamowienie, rola), multi=True)
        connection.commit()
        print("Rekord został pomyślnie dodany do tabeli Produkty\n")
        
    else:    
        print("\nWybierz poprawną opcję\n")
        return menuPracownicy()

def menuMagazyn():
    menuMagazynInput = input("""\nWybierz akcję:\n 1. Wyświetlenie wszystkie stany magazynowe\n 2. Dodaj stan magazynowy\n 3. Edytuj stan magazynowy\n 0. Wstecz\n\n--> """)
    if menuMagazynInput == '0':
        main()
        
    elif menuMagazynInput == '1':
        print("\n\n")
        query = ("SELECT * FROM magazyn")
        cursor.execute(query)
        rows = cursor.fetchall()
        result = len(rows)
        #TODO
        print ("ID   IMIĘ   NAZWISKO   CZAS PRACY   ZMIANA   OBECNE ZAMOWIENIE   ROLA")
        if result > 0:
            x = 0
            for row in rows:
                row = rows[x]
                prod_id, nazwa, norma = row[0], row[0], row[0]
                print (row)
                x = x + 1
        print("\n\n")
        menuProdukty()

    else:    
        print("\nWybierz poprawną opcję\n")
        return menuMagazyn()
    
#! SKŁADNIA JOIN
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

#! USUWANIE REKORDU
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

#TODO Editing
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