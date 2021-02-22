import sys
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    database='inżynierka', 
                                    user='s1lv41n', 
                                    password='S1lv41nftw!', 
                                    auth_plugin='mysql_native_password')
cursor = connection.cursor()


def main():    
    mainMenuInput = mainMenu() #! DONE
    if mainMenuInput == '1':
        handlowiecMenu()
        
    elif mainMenuInput == '2': #! DONE
        kierownikMenu()
        
    elif mainMenuInput == '3': #TODO Aktualizacja postępów produkcji
        brygadzistaMenu()
        
    elif mainMenuInput == '4': #! DONE
        magazynierMenu()
        
    elif mainMenuInput == '5': #! DONE
        kadrowyMenu()
        
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
    print ("\nWitaj w aplikacji Ghostsent.\n\n")


def mainMenu():
    print ("Twoja rola to: Administrator\n")
    mainMenuInput = input("""Wybierz pracownika z którego roli chcesz skorzystać:\n 1. Handlowiec\n 2. Kierownik\n 3. Brygadzista\n 4. Magazynier\n 5. Kadrowy\n 6. Zarząd Firmy\n 7. Modyfikuj rolę pracownika\n 0. Wyjście z programu\n\n--> """)
    if mainMenuInput == '0':
        print("\nZakończono pracę z programem")
        sys.exit()
    return mainMenuInput

#*HANDLOWIEC
def handlowiecMenu():
    print ("\n\nTwoja rola to: Handlowiec\n")
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
    print ("\n\nTwoja rola to: Kierownik\n")
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
#*KIEROWNIK

#*BRYGADZISTA
def brygadzistaMenu():
    print ("\n\nTwoja rola to: Brygadzista\n")
    brygadzistaMenuInput = input ("""Wybierz akcję:\n 1. Deleguj pracowników\n 2. Aktualizacja postępów produkcji\n 3. Wyświetl rejestr zleceń\n 0. Wstecz\n\n--> """)

    if brygadzistaMenuInput == "0":
        mainMenu()
        
    elif brygadzistaMenuInput == "1":
        id_zamowienie = (input ("Podaj numer ID zlecenia do delegowania pracowników:\n"), )
        print("Wyświetlam informacje o wybranym zleceniu: \n")
        mySql_select_record = "SELECT * FROM zamowienia WHERE id_zamowienie = %s"
        cursor.execute(mySql_select_record, id_zamowienie)
        record = cursor.fetchall()
        print(record[0])
        confirmation = input("\nCzy na pewno chcesz delegować pracowników do tego zamówienia? t/n\n")
        
        if confirmation == "t":
            employee_amount = input ("Podaj ilość pracowników do przypisania ich do zlecenia: \n")
            confirmation2 = input ("Czy wprowadzona ilość pracowników jest poprawna? t/n\n")
            
            if confirmation2 == "t":
                query = "UPDATE zamowienia SET ilosc_pracownik = %s WHERE id_zamowienie = %s"
                cursor.execute (query, (employee_amount, id_zamowienie[0]), multi = True)
                connection.commit()
                print("Nowa ilość pracowników oddeloegowanych do tego zmaówienia to:", employee_amount)
                
            elif confirmation2 == "n":
                print ("Ilość pracowników nie została zmieniona")
                brygadzistaMenu()
                
            else:
                print ("Wybierz poprawną opcję")
                brygadzistaMenu()
        
        elif confirmation == "n":
            brygadzistaMenu()
        
        else:
            print("Wybierz poprawną opcję")
            brygadzistaMenu()
        brygadzistaMenu()
        
    elif brygadzistaMenuInput == "2":
        def brygadzistaAktualizacjaMenu():
            print("Ta opcja nie została jeszcze zaimplementowana")
            brygadzistaMenu()
        brygadzistaAktualizacjaMenu()
    
    elif brygadzistaMenuInput == "3":
        def brygadzistaZamowieniaRegisterMenu():
            brygadzistaZamowieniaRegisterMenuInput = input (""" 1. Wyświetl wszystkie zasoby (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n--> """)
            if brygadzistaZamowieniaRegisterMenuInput == "0":
                brygadzistaMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "3":
                def brygadzistaZamowieniaRegisterFilterMenu():
                    brygadzistaZamowieniaRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n-->"""))
                    mySql_filter = ("""SELECT * FROM zamowienia WHERE status = %s""")
                    print("\n\n")
                    cursor.execute(mySql_filter, (brygadzistaZamowieniaRegisterFilterMenuInput,))
                    rows = cursor.fetchall()
                    result = len(rows)
                    if result > 0:
                        x = 0
                        for row in rows:
                            row = rows[x]
                            print (row)
                            x = x + 1
                    print("\n\n")
                    brygadzistaZamowieniaRegisterMenu()
                brygadzistaZamowieniaRegisterFilterMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "2":
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
                brygadzistaZamowieniaRegisterMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "1":
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
                brygadzistaZamowieniaRegisterMenu()
                
            else:
                print ("Wybierz poprawną opcję")        
                brygadzistaZamowieniaRegisterMenu()
                
        brygadzistaZamowieniaRegisterMenu()    
#*BRYGADZISTA

#*MAGAZYNIER
def magazynierMenu():
    print ("\n\nTwoja rola to: Magazynier\n")
    magazynierMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl stany magazynowe\n 2. Dodaj zasób\n 3. Modyfikuj zasób\n 0. Wstecz\n\n--> """)
    
    if magazynierMenuInput == "0":
        mainMenu()
        
    elif magazynierMenuInput == "1":
        def magazynierZasobyRegisterMenu():
            magazynierZasobyRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 4. Filtruj: ID Produktu\n 0. Wstecz\n\n--> """)
            if magazynierZasobyRegisterMenuInput == "0":
                magazynierMenu()
             
            elif magazynierZasobyRegisterMenuInput == "4":
                    magazynierZasobyRegisterFilterMenuInput = int (input ("""Podaj ID produktu\n\n-->"""))
                    mySql_filter = ("""SELECT * FROM magazyn WHERE id_produkt = %s""")
                    print("\n\n")
                    cursor.execute(mySql_filter, (magazynierZasobyRegisterFilterMenuInput,))
                    rows = cursor.fetchall()
                    result = len(rows)
                    if result > 0:
                        x = 0
                        for row in rows:
                            row = rows[x]
                            print (row)
                            x = x + 1
                    print("\n\n")
                    magazynierZasobyRegisterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "3":
                def magazynierZasobyRegisterFilterMenu():
                    magazynierZasobyRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zapas\n 2. Zarezerwowany\n 3. Niedostępny\n\n-->"""))
                    mySql_filter = ("""SELECT * FROM magazyn WHERE status = %s""")
                    print("\n\n")
                    cursor.execute(mySql_filter, (magazynierZasobyRegisterFilterMenuInput,))
                    rows = cursor.fetchall()
                    result = len(rows)
                    if result > 0:
                        x = 0
                        for row in rows:
                            row = rows[x]
                            print (row)
                            x = x + 1
                    print("\n\n")
                    magazynierZasobyRegisterMenu()
                magazynierZasobyRegisterFilterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji")
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
                magazynierZasobyRegisterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji DESC")
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
                magazynierZasobyRegisterMenu()
                
            else:
                print ("Wybierz poprawną opcję")        
                magazynierZasobyRegisterMenu()    
        magazynierZasobyRegisterMenu()    

    elif magazynierMenuInput == "2":
        id_produkt = input ("id_produkt:\n-->")
        ilosc = input ("ilosc:\n-->")
        data_produkcji = input ("data produkcji (poprawny format daty to RRRR-MM-DD):\n-->")
        id_zamowienie = input ("id_zamowienie (może pozostać puste):\n-->")
        status = input ("status: (domyślny 1. Wolny)\n-->")
        mySql_insert_record = """INSERT INTO magazyn (id_produkt, ilosc, data_produkcji, id_zamowienie, status) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(mySql_insert_record, (id_produkt, ilosc, data_produkcji, id_zamowienie, status), multi=True)
        connection.commit()
        print("Zasób został pomyślnie dodany do magazynu\n")
        magazynierMenu()

    elif kierownikProduktyMenuInput == "3":
        id_zasob = (input ("Podaj numer ID zasobu do edycji:\n"), )
        print("Wyświetlam obecne dane o zasobie:\n")
        mySql_select_record = "SELECT * FROM magazyn WHERE id_zasob = %s"
        cursor.execute(mySql_select_record, id_zasob)
        record = cursor.fetchall()
        print(record[0])
        confirmation = input("Czy napewno chcesz modyfikować ten zasob? t/n \n")
                    
        if confirmation == "t":
            print("Podaj nowe wartości zasobu: \n")
            id_produkt = input ("id_produkt:\n-->")
            ilosc = input ("ilosc:\n-->")
            data_produkcji = input ("data produkcji (poprawny format daty to RRRR-MM-DD):\n-->")
            id_zamowienie = input ("id_zamowienie (może pozostać puste):\n-->")
            status = input ("status: ()\n-->")
            mySql_update_record = ("""UPDATE magazyn SET id_produkt = %s, ilosc = %s, data_produkcji = %s, id_zamowienie = %s, status = %s WHERE id_produkt = %s""")
            cursor.execute(mySql_update_record, (id_produkt, ilosc, data_produkcji, id_zamowienie, status),multi = True)
            connection.commit() 
            print("Rekord został pomyślnie edytowany\n")
            kierownikProduktyMenu()
                        
        elif confirmation == "n":
            print ("Rekord nie został edytowany\n")
            kierownikProduktyMenu()
            
        else:
            print("Wybierz poprawną opcję")
            kierownikProduktyMenu()
    magazynierMenu()
#*MAGAZYNIER

#*KADROWY
def kadrowyMenu():
    kadrowyMenuInput = input("Wybierz opcję:\n 1. Wyświetl spis pracowników\n 2. Dodaj pracownika\n 3. Edytuj pracownika\n 4. Usuń pracownika\n 0. Wstecz\n\n--> ")
    
    if kadrowyMenuInput == "0":
        mainMenu()
        
    elif kadrowyMenuInput == "1":
        def kadrowyPracownicyMenu():
            kadrowyPracownicyMenuInput = input("Wybierz opcję:\n 1. Sortuj: ID\n 2. Sortuj: Nazwisko\n 0. Wstecz\n\n--> ")
            
            if kadrowyPracownicyMenuInput == "0":
                kadrowyMenu()
                
            elif kadrowyPracownicyMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY id_pracownik")
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
                kadrowyPracownicyMenu()
                
            elif kadrowyPracownicyMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY nazwisko")
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
                kadrowyPracownicyMenu()
        kadrowyPracownicyMenu()
        
    elif kadrowyMenuInput == "2":
        imie = input ("imie:\n-->")
        nazwisko = input ("nazwisko:\n-->")
        mySql_insert_record = """INSERT INTO pracownicy (imie, nazwisko)VALUES (%s, %s)"""
        cursor.execute(mySql_insert_record, (imie, nazwisko), multi=True)
        connection.commit()
        print("Pracownik został pomyślnie dodany do spisu pracowników\n")
        kadrowyMenu()

    elif kadrowyMenuInput == "3":
        id_pracownik = (input ("Podaj numer ID pracownika do edycji:\n"), )
        print("Wyświetlam obecne dane pracownika:\n")
        mySql_select_record = "SELECT * FROM pracownicy WHERE id_pracownik = %s"
        cursor.execute(mySql_select_record, id_pracownik)
        record = cursor.fetchall()
        print(record[0])
        confirmation = input("Czy napewno chcesz edytować tego pracownika? t/n \n")
            
        if confirmation == "t":
            print("Podaj nowe dane pracownika: \n")
            imie = input("imie: ")
            nazwisko = input("nazwisko: ")
            print (imie)
            print (nazwisko)
            mySql_update_record = ("""UPDATE pracownicy SET imie = %s, nazwisko = %s WHERE id_pracownik = %s""")
            cursor.execute(mySql_update_record, (imie, nazwisko, id_pracownik[0]),multi = True)
            connection.commit() 
            print("Pracownik został pomyślnie edytowany\n")
            kadrowyMenu()
                
        elif confirmation == "n":
            print ("Pracownik nie został edytowany\n")
            kadrowyMenu()
        
        else:
            print ("Wybierz poprawną opcję")
            kadrowyMenu()
            
    elif kadrowyMenuInput == "4":
        id_pracownik = (input("Podaj ID pracownika do usunięcia: "), )
        print("Wyświetlam informację o pracowniku przed jego usunięciem: ")
        mySql_select_record = """SELECT * 
                            FROM pracownicy
                            WHERE id_pracownik = %s"""
        cursor.execute(mySql_select_record, id_pracownik)
        record = cursor.fetchall()
        print(record)
        confirmation = input("Czy napewno chcesz usunąć ten rekord? t/n \n")
        
        if confirmation == "t":
            mySql_delete_record = """DELETE from pracownicy 
                                WHERE id_pracownik = %s"""
            cursor.execute(mySql_delete_record, id_pracownik)
            connection.commit()
            print("Pracownik został pomyślnie usunięty\n")
            kadrowyMenu()
            
        elif confirmation == "n":
            print ("Pracownik nie został usunięty\n")
            kadrowyMenu()
    
        else:
            print("Wybierz poprawną opcję")
            kadrowyMenu()
    
    kadrowyMenu()    
            
    

#*KADROWY

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