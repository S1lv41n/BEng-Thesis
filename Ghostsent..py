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
        handlowiecMenu()
        
    elif mainMenuInput == '2':
        kierownikMenu()
        
    elif mainMenuInput == '3':
        menuMagazyn()
        
    elif mainMenuInput == '4':
        menuProdukty()
        
    elif mainMenuInput == '5':
        menuPracownicy()
        
    elif mainMenuInput == '6':
        menuMagazyn()       
        
    elif mainMenuInput == '7':
        menuMagazyn()
        
    else:
        print("\nWybierz poprawną opcję\n")

    main()


def welcome():
    db_info = connection.get_server_info()
    print("Wersja serwera MySQL:", db_info)
    cursor.execute("select database();")
    record = cursor.fetchone()
    print ("\nWitaj w aplikacji Ghostsent.")
    print ("Twoja rola to: Administrator\n")


def mainMenu():
    mainMenuInput = input("""Wybierz pracownika z którego roli chcesz skorzystać:\n 1. Handlowiec\n 2. Kierownik\n 3. Brygadzista\n 4. Magazynier\n 5. Kadrowy\n 6. Zarząd Firmy\n 7. Modyfikuj rolę pracownika\n 0. Wyjście z programu\n\n--> """)
    if mainMenuInput == '0':
        print("\nZakończono pracę z programem")
        sys.exit()
    return mainMenuInput

#*HANDLOWIEC
def handlowiecMenu():
    handlowiecMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl rejestr zleceń\n 2. Modyfikacja daty realizacji zlecenia\n 0. Wstecz\n\n--> """)
    if handlowiecMenuInput == "0":
        main()
        
    elif handlowiecMenuInput == "1":
        def handlowiecRegisterMenu():
            handlowiecRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n--> """)
            if handlowiecRegisterMenuInput == "0":
                handlowiecMenu()
                
            elif handlowiecRegisterMenuInput == "3":
                def handlowiecRegisterFilterMenu():
                    handlowiecRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n-->"""))
                    mySql_filter = ("""SELECT * FROM zamowienia WHERE status = %s""")
                    print("\n\n")
                    cursor.execute(mySql_filter, (handlowiecRegisterFilterMenuInput,))
                    rows = cursor.fetchall()
                    result = len(rows)
                    if result > 0:
                        x = 0
                        for row in rows:
                            row = rows[x]
                            print (row)
                            x = x + 1
                    print("\n\n")
                    handlowiecRegisterMenu()
                handlowiecRegisterFilterMenu()
                
            elif handlowiecRegisterMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                cursor.execute(query)
                rows = cursor.fetchall()
                result = len(rows)
                if result > 0:
                    x = 0
                    for row in rows:
                        row = rows[x]
                        print (row)
                        x = x + 1
                print("\n\n")
                handlowiecRegisterMenu()
                
            elif handlowiecRegisterMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                cursor.execute(query)
                rows = cursor.fetchall()
                result = len(rows)
                if result > 0:
                    x = 0
                    for row in rows:
                        row = rows[x]
                        print (row)
                        x = x + 1
                print("\n\n")
                handlowiecRegisterMenu()
                
            else:
                print ("Wybierz poprawną opcję")        

        handlowiecRegisterMenu()
        
    elif handlowiecMenuInput == "2":
        id_zamowienie = (input ("Podaj numer ID zlecenia do edycji daty realizacji:\n"), )
        print("Wyświetlam obecną datę realizacji zlecenia: \n")
        mySql_select_record = "SELECT data_realizacji FROM zamowienia WHERE id_zamowienie = %s"
        cursor.execute(mySql_select_record, id_zamowienie)
        record = cursor.fetchall()
        print(record[0])
        new_date = input("\nPoprawny format daty to RRRR-MM-DD\n")
        print("Nowa data realizacji zlecenia to:", new_date)
        selection = input("Potwierdzasz? t/n")
        if selection == "t":
            query = "UPDATE zamowienia SET data_realizacji = %s WHERE id_zamowienie = %s"
            cursor.execute (query, (new_date, id_zamowienie[0]), multi = True)
            connection.commit()
            
        elif selection == "n":
            print("Data realizacji nie została zaktualizowana")
            handlowiecMenu()
            
        else:
            print("Wybierz poprawną opcję")
            
#*HANDLOWIEC

#*KIEROWNIK
def kierownikMenu():
    kierownikMenuInput = input ("""Wybierz akcję:\n 1. Rejestr zleceń\n 2. Rejestr produktów\n 0. Wstecz\n\n--> """)
    if kierownikMenuInput == "0":
        main()
        
    elif kierownikMenuInput == "1":
        def kierownikZamowieniaMenu():
            kierownikZamowieniaMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl rejestr zleceń\n 2. Modyfikacja daty realizacji zlecenia\n 0. Wstecz\n\n--> """)
            if kierownikZamowieniaMenuInput == "0":
                kierownikMenu()
        
            elif kierownikZamowieniaMenuInput == "1":
                def kierownikZamowieniaRegisterMenu():
                    kierownikZamowieniaRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n--> """)
                    
                    if kierownikZamowieniaRegisterMenuInput == "0":
                        kierownikZamowieniaMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "3":
                        def kierownikZamowieniaRegisterFilterMenu():
                            kierownikZamowieniaRegisterFilterMenuInput = int (input ("""Wybierz status do   wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5.   Archiwalne\n\n-->"""))
                            mySql_filter = ("""SELECT * FROM zamowienia WHERE status = %s""")
                            print("\n\n")
                            cursor.execute(mySql_filter, (kierownikZamowieniaRegisterFilterMenuInput,))
                            rows = cursor.fetchall()
                            result = len(rows)
                            if result > 0:
                                x = 0
                                for row in rows:
                                    row = rows[x]
                                    print (row)
                                    x = x + 1
                            print("\n\n")
                            kierownikZamowieniaRegisterMenu()
                        kierownikZamowieniaRegisterFilterMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "2":
                        print("\n\n")
                        query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        result = len(rows)
                        if result > 0:
                            x = 0
                            for row in rows:
                                row = rows[x]
                                print (row)
                                x = x + 1
                        print("\n\n")
                        kierownikZamowieniaRegisterMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "1":
                        print("\n\n")
                        query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        result = len(rows)
                        if result > 0:
                            x = 0
                            for row in rows:
                                row = rows[x]
                                print (row)
                                x = x + 1
                        print("\n\n")
                        kierownikZamowieniaRegisterMenu()

                    else:
                        print ("Wybierz poprawną opcję")        

                kierownikZamowieniaRegisterMenu()

            elif kierownikZamowieniaMenuInput == "2":
                id_zamowienie = (input ("Podaj numer ID zlecenia do edycji daty realizacji:\n"), )
                print("Wyświetlam obecną datę realizacji zlecenia: \n")
                mySql_select_record = "SELECT data_realizacji FROM zamowienia WHERE id_zamowienie = %s"
                cursor.execute(mySql_select_record, id_zamowienie)
                record = cursor.fetchall()
                print(record[0])
                new_date = input("\nPoprawny format daty to RRRR-MM-DD\n")
                print("Nowa data realizacji zlecenia to:", new_date)
                selection = input("Potwierdzasz? t/n")
                if selection == "t":
                    query = "UPDATE zamowienia SET data_realizacji = %s WHERE id_zamowienie = %s"
                    cursor.execute (query, (new_date, id_zamowienie[0]), multi = True)
                    connection.commit()

                elif selection == "n":
                    print("Data realizacji nie została zaktualizowana")

            else:
                print("Wybierz poprawną opcję")
                
        kierownikZamowieniaMenu()        
    
    elif kierownikMenuInput == "2":
        def kierownikProduktyMenu():
            kierownikProduktyMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl rejestr produktów\n 2. Dodaj produkt\n 3. Edytuj produkt\n 4. Usuń produkt\n 0. Wstecz\n\n--> """)
            if kierownikProduktyMenuInput == "0":
                kierownikMenu()
        
            elif kierownikProduktyMenuInput == "1":
                def kierownikProduktyRegisterMenu():
                    kierownikProduktyRegisterMenuInput = input (""" 1. Wyświetl wszystkie produkty (Sortuj: ID)\n 2. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie\n 3. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie (Odwrotność))\n 0. Wstecz\n\n--> """)
                    
                    if kierownikProduktyRegisterMenuInput == "0":
                        kierownikProduktyMenu()

                    elif kierownikProduktyRegisterMenuInput == "1":
                        print("\n\n")
                        query = ("SELECT * FROM produkty ORDER BY id_produkt")
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        result = len(rows)
                        if result > 0:
                            x = 0
                            for row in rows:
                                row = rows[x]
                                print (row)
                                x = x + 1
                        print("\n\n")
                        kierownikProduktyRegisterMenu()


                    elif kierownikProduktyRegisterMenuInput == "2":
                        print("\n\n")
                        query = ("SELECT * FROM produkty ORDER BY nazwa")
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        result = len(rows)
                        if result > 0:
                            x = 0
                            for row in rows:
                                row = rows[x]
                                print (row)
                                x = x + 1
                        print("\n\n")
                        kierownikProduktyRegisterMenu()

                    elif kierownikProduktyRegisterMenuInput == "3":
                        print("\n\n")
                        query = ("SELECT * FROM produkty ORDER BY nazwa DESC")
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        result = len(rows)
                        if result > 0:
                            x = 0
                            for row in rows:
                                row = rows[x]
                                print (row)
                                x = x + 1
                        print("\n\n")
                        kierownikProduktyRegisterMenu()

                    else:
                        print ("Wybierz poprawną opcję")        

                kierownikProduktyRegisterMenu()

            elif kierownikProduktyMenuInput == "2":
                nazwa = input ("nazwa:\n-->")
                norma = input ("norma:\n-->")
                jm = input ("jm:\n-->")
                technologia = input ("technologia:\n-->")
                mySql_insert_record = """INSERT INTO produkty (nazwa, norma, jm, technologia)VALUES (%s, %s, %s, %s)"""
                cursor.execute(mySql_insert_record, (nazwa,  norma, jm, technologia), multi=True)
                connection.commit()
                print("Rekord został pomyślnie dodany do tabeli Produkty\n")
                kierownikProduktyMenu()

            elif kierownikProduktyMenuInput == "3":
                id_produkt = (input ("Podaj numer ID produktu do edycji:\n"), )
                print("Wyświetlam obecne dane produktu:\n")
                mySql_select_record = "SELECT * FROM produkty WHERE id_produkt = %s"
                cursor.execute(mySql_select_record, id_produkt)
                record = cursor.fetchall()
                print(record[0])
                confirmation = input("Czy napewno chcesz edytować ten produkt? t/n \n")
                    
                if confirmation == "t":
                    print("Podaj nowe wartości rekordu: \n")
                    nazwa = input("nazwa: ")
                    norma = input("norma: ")
                    jm = input("jm: ")
                    technologia = input("technologia: ")
                    id = id_produkt
                    mySql_update_record = ("""UPDATE produkty SET nazwa = %s, norma = %s, jm = %s, technologia = %s WHERE id_produkt = %s""")
                    cursor.execute(mySql_update_record, (nazwa, norma, jm, technologia, id[0]),multi = True)
                    connection.commit() 
                    print("Rekord został pomyślnie edytowany\n")
                    kierownikProduktyMenu()
                        
                if confirmation == "n":
                    print ("Rekord nie został edytowany\n")
                    kierownikProduktyMenu()
            
            elif kierownikProduktyMenuInput == "4":
                id_produkt = (input("Podaj ID produktu do usunięcia: "), )
                print("Wyświetlam dane produktu przed jego usunięciem: ")
                mySql_select_record = """SELECT * 
                                    FROM produkty 
                                    WHERE id_produkt = %s"""
                cursor.execute(mySql_select_record, id_produkt)
                record = cursor.fetchall()
                print(record)

                confirmation = input("Czy napewno chcesz usunąć ten rekord? t/n \n")

                if confirmation == "t":
                    mySql_delete_record = """DELETE from produkty 
                                        WHERE id_produkt = %s"""
                    cursor.execute(mySql_delete_record, id_produkt)
                    connection.commit()
                    print("Rekord został pomyślnie usunięty\n")
                    kierownikProduktyMenu()

                if confirmation == "n":
                    print ("Rekord nie został usunięty\n")
                    kierownikProduktyMenu()
            
            else:
                print("Wybierz poprawną opcję")
                
        kierownikProduktyMenu()
        
        
        
         
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




welcome()            
main()