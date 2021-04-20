import sys
import mysql.connector
import datetime

connection = mysql.connector.connect(host='localhost',
                                    database='praca_inżynierska', 
                                    user='s1lv41n', 
                                    password='S1lv41nftw!', 
                                    auth_plugin='mysql_native_password')
cursor = connection.cursor(buffered=True)


def main():    
    mainMenuInput = mainMenu()
    if mainMenuInput == '1':
        handlowiecMenu()
        
    elif mainMenuInput == '2':
        kierownikMenu()
        
    elif mainMenuInput == '3':
        brygadzistaMenu()
        
    elif mainMenuInput == '4':
        magazynierMenu()
        
    elif mainMenuInput == '5':
        kadrowyMenu()
        
    elif mainMenuInput == '6':
        zarzadMenu()       
        
    elif mainMenuInput == '7':
        print("Ta opcja nie została jeszcze zaimplementowana")
        
    else:
        print("\nWybierz poprawną opcję\n")

    main()


def welcome():
    db_info = connection.get_server_info()
    print("\n\nWersja serwera MySQL:", db_info)
    cursor.execute("select database();")
    #record = cursor.fetchone()
    print("\nWitaj w aplikacji Ghostsent.")


def mainMenu():
    print("Twoja rola to: Administrator\n")
    mainMenuInput = input("""Wybierz pracownika z którego roli chcesz skorzystać:\n 1. Handlowiec\n 2. Kierownik\n 3. Brygadzista\n 4. Magazynier\n 5. Kadrowy\n 6. Zarząd Firmy\n 7. Modyfikuj rolę pracownika\n 0. Wyjście z programu\n\n❯ """)
    if mainMenuInput == '0':
        print("\nZakończono pracę z programem.")
        sys.exit()
    return mainMenuInput

#*HANDLOWIEC
def handlowiecMenu():
    print("\nTwoja rola to: Handlowiec\n")
    handlowiecMenuInput = input("""Wybierz akcję:\n 1. Wyświetl rejestr zleceń\n 2. Modyfikacja daty realizacji zlecenia\n 0. Wstecz\n\n❯ """)
    print("\n")
    if handlowiecMenuInput == "0":
        main()
        
    elif handlowiecMenuInput == "1":
        def handlowiecRegisterMenu():
            handlowiecRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n❯ """)
            if handlowiecRegisterMenuInput == "0":
                handlowiecMenu()
                
            elif handlowiecRegisterMenuInput == "3":
                def handlowiecRegisterFilterMenu():
                    print("\n")
                    handlowiecRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n❯ """))
                    query = ("""SELECT * FROM zamowienia WHERE status = %s""")
                    print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                    cursor.execute(query, (handlowiecRegisterFilterMenuInput,))
                    for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                        print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                    print("\n\n")
                    handlowiecRegisterMenu()
                handlowiecRegisterFilterMenu()
                
            elif handlowiecRegisterMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
                handlowiecRegisterMenu()
            
            elif handlowiecRegisterMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
                handlowiecRegisterMenu()
                
            else:
                print("Wybierz poprawną opcję")        

        handlowiecRegisterMenu()
        
    elif handlowiecMenuInput == "2":
        id_zamowienie = (input ("Podaj numer ID zlecenia do edycji daty realizacji:\n❯ "), )
        print("Wyświetlam obecną datę realizacji zlecenia: \n")
        query = "SELECT data_realizacji FROM zamowienia WHERE id_zamowienie = %s"
        cursor.execute(query, id_zamowienie)
        record = cursor.fetchone()
        print(record[0])
        new_date = input("\nPoprawny format daty to RRRR-MM-DD\n❯ ")
        print("\nNowa data realizacji zlecenia to:", new_date)
        selection = input("Potwierdzasz? t/n\n❯")
        if selection == "t":
            query = ("UPDATE zamowienia SET data_realizacji = %s WHERE id_zamowienie = %s")
            cursor.execute (query, (new_date, id_zamowienie[0]), multi = True)
            connection.commit()
            
        elif selection == "n":
            print("\nData realizacji nie została zaktualizowana")
            handlowiecMenu()
            
        else:
            print("\nWybierz poprawną opcję")            
            handlowiecMenu()
#*HANDLOWIEC

#*KIEROWNIK
def kierownikMenu():
    print("\nTwoja rola to: Kierownik\n")
    kierownikMenuInput = input ("""Wybierz akcję:\n 1. Rejestr zleceń\n 2. Rejestr produktów\n 0. Wstecz\n\n❯ """)
    if kierownikMenuInput == "0":
        main()
        
    elif kierownikMenuInput == "1":
        def kierownikZamowieniaMenu():
            kierownikZamowieniaMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl rejestr zleceń\n 2. Modyfikacja daty realizacji zlecenia\n 0. Wstecz\n\n❯ """)
            if kierownikZamowieniaMenuInput == "0":
                kierownikMenu()
        
            elif kierownikZamowieniaMenuInput == "1":
                def kierownikZamowieniaRegisterMenu():
                    kierownikZamowieniaRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n❯ """)
                    
                    if kierownikZamowieniaRegisterMenuInput == "0":
                        kierownikZamowieniaMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "3":
                        def kierownikZamowieniaRegisterFilterMenu():
                            kierownikZamowieniaRegisterFilterMenuInput = int (input ("""Wybierz status do   wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n❯ """))
                            query = ("""SELECT * FROM zamowienia WHERE status = %s""")
                            print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                            cursor.execute(query, (kierownikZamowieniaRegisterFilterMenuInput,))
                            for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                                print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                            print("\n\n")
                            kierownikZamowieniaRegisterMenu()
                        kierownikZamowieniaRegisterFilterMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "2":
                        print("\n\n")
                        query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                        print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                        cursor.execute(query)
                        for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                            print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                        print("\n\n")
                        kierownikZamowieniaRegisterMenu()

                    elif kierownikZamowieniaRegisterMenuInput == "1":
                        print("\n\n")
                        query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                        print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                        cursor.execute(query)
                        for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                            print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                        print("\n\n")
                        kierownikZamowieniaRegisterMenu()
                        

                    else:
                        print("Wybierz poprawną opcję\n")        
                        kierownikZamowieniaRegisterMenu()
                kierownikZamowieniaRegisterMenu()

            elif kierownikZamowieniaMenuInput == "2":
                id_zamowienie = (input ("Podaj numer ID zlecenia do edycji daty realizacji:\n"), )
                print("Wyświetlam obecną datę realizacji zlecenia:\n")
                query = "SELECT data_realizacji FROM zamowienia WHERE id_zamowienie = %s"
                cursor.execute(query, id_zamowienie)
                record = cursor.fetchone()
                print(record[0])
                new_date = input("\nPoprawny format daty to RRRR-MM-DD\n❯ ")
                print("Nowa data realizacji zlecenia to:", new_date)
                selection = input("Potwierdzasz? t/n\n❯ ")
                if selection == "t":
                    query = "UPDATE zamowienia SET data_realizacji = %s WHERE id_zamowienie = %s"
                    cursor.execute (query, (new_date, id_zamowienie[0]), multi = True)
                    connection.commit()
                    kierownikZamowieniaMenu()

                elif selection == "n":
                    print("Data realizacji nie została zaktualizowana\n")
                    kierownikZamowieniaMenu()

            else:
                print("Wybierz poprawną opcję")
                kierownikZamowieniaMenu()
                
        kierownikZamowieniaMenu()        
    
    elif kierownikMenuInput == "2":
        def kierownikProduktyMenu():
            kierownikProduktyMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl rejestr produktów\n 2. Dodaj produkt\n 3. Edytuj produkt\n 4. Usuń produkt\n 0. Wstecz\n\n❯ """)
            if kierownikProduktyMenuInput == "0":
                kierownikMenu()
        
            elif kierownikProduktyMenuInput == "1":
                def kierownikProduktyRegisterMenu():
                    kierownikProduktyRegisterMenuInput = input (""" 1. Wyświetl wszystkie produkty (Sortuj: ID)\n 2. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie\n 3. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie (Odwrotność))\n 0. Wstecz\n\n❯ """)
                    
                    if kierownikProduktyRegisterMenuInput == "0":
                        kierownikProduktyMenu()

                    elif kierownikProduktyRegisterMenuInput == "1":
                        print("\n\n")
                        print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                        query = ("SELECT * FROM produkty ORDER BY id_produkt")
                        cursor.execute(query)
                        for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                                print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                        print("\n\n")
                        kierownikProduktyRegisterMenu()


                    elif kierownikProduktyRegisterMenuInput == "2":
                        print("\n\n")
                        print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                        query = ("SELECT * FROM produkty ORDER BY nazwa")
                        cursor.execute(query)
                        for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                                print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                        print("\n\n")
                        kierownikProduktyRegisterMenu()

                    elif kierownikProduktyRegisterMenuInput == "3":
                        print("\n\n")
                        print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                        query = ("SELECT * FROM produkty ORDER BY nazwa DESC")
                        cursor.execute(query)
                        for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                                print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                        print("\n\n")
                        kierownikProduktyRegisterMenu()

                    else:
                        print("Wybierz poprawną opcję")        
                        kierownikProduktyRegisterMenu()
                kierownikProduktyRegisterMenu()

            elif kierownikProduktyMenuInput == "2":
                nazwa = input ("nazwa:\n❯ ")
                norma = input ("norma:\n❯ ")
                jm = input ("jm:\n❯ ")
                technologia = input ("technologia:\n❯ ")
                query = """INSERT INTO produkty (nazwa, norma, jm, technologia) VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, (nazwa,  norma, jm, technologia), multi=True)
                connection.commit()
                print("Rekord został pomyślnie dodany do tabeli Produkty\n")
                kierownikProduktyMenu()

            elif kierownikProduktyMenuInput == "3":
                id_produkt = (input ("Podaj numer ID produktu do edycji:\n❯ "), )
                print("Wyświetlam obecne dane produktu:\n")
                print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                query = "SELECT * FROM produkty WHERE id_produkt = %s"
                cursor.execute(query, id_produkt)
                record = cursor.fetchone()
                print("{}    |{}     |{}           |{}         |{}".format(record[0], record[1], record[2], record[3], record[4]))
                confirmation = input("Czy napewno chcesz edytować ten produkt? t/n\n❯ ")
                    
                if confirmation == "t":
                    print("Podaj nowe wartości rekordu:\n")
                    nazwa = input("nazwa:\n❯ ")
                    norma = input("norma:\n❯ ")
                    jm = input("jm: ")
                    technologia = input("technologia: ")
                    id = id_produkt
                    mySql_update_record = ("""UPDATE produkty SET nazwa = %s, norma = %s, jm = %s, technologia = %s WHERE id_produkt = %s""")
                    cursor.execute(mySql_update_record, (nazwa, norma, jm, technologia, id[0]),multi = True)
                    connection.commit() 
                    print("Rekord został pomyślnie edytowany\n")
                    kierownikProduktyMenu()
                        
                if confirmation == "n":
                    print("Rekord nie został edytowany\n")
                    kierownikProduktyMenu()
            
            elif kierownikProduktyMenuInput == "4":
                id_produkt = (input("Podaj ID produktu do usunięcia:\n❯ "), )
                print("Wyświetlam dane produktu przed jego usunięciem: ")
                print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                query = """SELECT * FROM produkty WHERE id_produkt = %s"""
                cursor.execute(query, id_produkt)
                record = cursor.fetchone()
                print("{}    |{}     |{}           |{}         |{}".format(record[0], record[1], record[2], record[3], record[4]))

                confirmation = input("Czy napewno chcesz usunąć ten produkt? t/n\n❯ ")

                if confirmation == "t":
                    mySql_delete_record = """DELETE from produkty 
                                        WHERE id_produkt = %s"""
                    cursor.execute(mySql_delete_record, id_produkt)
                    connection.commit()
                    print("Produkt został pomyślnie usunięty\n")
                    kierownikProduktyMenu()

                elif confirmation == "n":
                    print("Produkt nie został usunięty\n")
                    kierownikProduktyMenu()
                    
                else:
                    print("Podaj poprawną opcję")
                    kierownikProduktyMenu()
            
            else:
                print("Wybierz poprawną opcję")
                kierownikProduktyMenu()
        kierownikProduktyMenu()
#*KIEROWNIK

#*BRYGADZISTA
def brygadzistaMenu():
    print("\nTwoja rola to: Brygadzista\n")
    brygadzistaMenuInput = input ("""Wybierz akcję:\n 1. Deleguj pracowników\n 2. Aktualizacja postępów produkcji\n 3. Wyświetl rejestr zleceń\n 0. Wstecz\n\n❯ """)

    if brygadzistaMenuInput == "0":
        mainMenu()
        
    elif brygadzistaMenuInput == "1":
        id_zamowienie = (input ("Podaj numer ID zlecenia do delegowania pracowników:\n❯ "), )
        print("Wyświetlam informacje o wybranym zleceniu: \n")
        print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
        query = "SELECT * FROM zamowienia WHERE id_zamowienie = %s"
        cursor.execute(query, id_zamowienie)
        record = cursor.fetchone()
        print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        confirmation = input("\nCzy na pewno chcesz delegować pracowników do tego zamówienia? t/n\n❯ ")
        
        if confirmation == "t":
            employee_amount = input ("Podaj ilość pracowników do przypisania ich do zlecenia:\n❯ ")
            confirmation2 = input ("Czy wprowadzona ilość pracowników jest poprawna? t/n\n❯ ")
            
            if confirmation2 == "t":
                query = "UPDATE zamowienia SET ilosc_pracownik = %s WHERE id_zamowienie = %s"
                cursor.execute (query, (employee_amount, id_zamowienie[0]), multi = True)
                connection.commit()
                print("Nowa ilość pracowników oddeloegowanych do tego zmaówienia to:", employee_amount)
                
            elif confirmation2 == "n":
                print("Ilość pracowników nie została zmieniona")
                brygadzistaMenu()
                
            else:
                print("Wybierz poprawną opcję")
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
            brygadzistaZamowieniaRegisterMenuInput = input (""" 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n❯ """)
            
            if brygadzistaZamowieniaRegisterMenuInput == "0":
                brygadzistaMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "3":
                def brygadzistaZamowieniaRegisterFilterMenu():
                    brygadzistaZamowieniaRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n❯ """))
                    query = ("""SELECT * FROM zamowienia WHERE status = %s""")
                    print("\n\n")
                    print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                    cursor.execute(query, (brygadzistaZamowieniaRegisterFilterMenuInput,))
                    for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                        print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                    print("\n\n")
                    brygadzistaZamowieniaRegisterMenu()
                brygadzistaZamowieniaRegisterFilterMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
                brygadzistaZamowieniaRegisterMenu()
                
            elif brygadzistaZamowieniaRegisterMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
                brygadzistaZamowieniaRegisterMenu()
                
            else:
                print("Wybierz poprawną opcję")        
                brygadzistaZamowieniaRegisterMenu()
        brygadzistaZamowieniaRegisterMenu()
#*BRYGADZISTA

#*MAGAZYNIER
def magazynierMenu():
    print("\nTwoja rola to: Magazynier\n")
    magazynierMenuInput = input ("""Wybierz akcję:\n 1. Wyświetl stany magazynowe\n 2. Dodaj zasób\n 3. Modyfikuj zasób\n 0. Wstecz\n\n❯ """)
    
    if magazynierMenuInput == "0":
        mainMenu()
        
    elif magazynierMenuInput == "1":
        def magazynierZasobyRegisterMenu():
            magazynierZasobyRegisterMenuInput = input (""" 1. Wyświetl wszystkie stany magazynowe (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie stany magazynowe (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 4. Filtruj: ID Produktu\n 0. Wstecz\n\n❯ """)
            if magazynierZasobyRegisterMenuInput == "0":
                magazynierMenu()
             
            elif magazynierZasobyRegisterMenuInput == "4":
                magazynierZasobyRegisterFilterMenuInput = int (input ("""Podaj ID produktu\n\n❯ """))
                query = ("""SELECT * FROM magazyn WHERE id_produkt = %s""")
                print("\n\n")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query, (magazynierZasobyRegisterFilterMenuInput,))
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                magazynierZasobyRegisterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "3":
                def magazynierZasobyRegisterFilterMenu():
                    magazynierZasobyRegisterFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zapas\n 2. Zarezerwowany\n 3. Niedostępny\n\n❯ """))
                    query = ("""SELECT * FROM magazyn WHERE status = %s""")
                    print("\n\n")
                    print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                    cursor.execute(query, (magazynierZasobyRegisterFilterMenuInput,))
                    for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                        print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                    print("\n\n")
                    magazynierZasobyRegisterMenu()
                magazynierZasobyRegisterFilterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query)
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                magazynierZasobyRegisterMenu()
                
            elif magazynierZasobyRegisterMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji DESC")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query)
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                magazynierZasobyRegisterMenu()
                
            else:
                print("Wybierz poprawną opcję")        
                magazynierZasobyRegisterMenu()    
        magazynierZasobyRegisterMenu()    

    elif magazynierMenuInput == "2":
        id_produkt = input ("id_produkt:\n❯ ")
        ilosc = input ("ilosc:\n❯ ")
        data_produkcji = input ("data produkcji (poprawny format daty to RRRR-MM-DD):\n❯ ")
        id_zamowienie = input ("id_zamowienie:\n❯ ")
        status = input ("status:\n❯ ")
        query = """INSERT INTO magazyn (id_produkt, ilosc, data_produkcji, id_zamowienie, status) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (id_produkt, ilosc, data_produkcji, id_zamowienie, status), multi=True)
        connection.commit()
        print("Zasób został pomyślnie dodany do magazynu\n")
        magazynierMenu()

    elif magazynierMenuInput == "3":
        id_zasob = (input ("Podaj numer ID zasobu do edycji:\n❯ "), )
        print("Wyświetlam obecne dane o zasobie:\n")
        print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
        query = "SELECT * FROM magazyn WHERE id_zasob = %s"
        cursor.execute(query, id_zasob)
        record = cursor.fetchone()
        print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(record[0], record[1], record[2], record[3], record[4], record[5]))
        confirmation = input("Czy napewno chcesz modyfikować ten zasob? t/n\n❯ ")
                    
        if confirmation == "t":
            print("Podaj nowe wartości zasobu:\n❯ ")
            id_produkt = input ("id_produkt:\n❯ ")
            ilosc = input ("ilosc:\n❯ ")
            data_produkcji = input ("data produkcji (poprawny format daty to RRRR-MM-DD):\n❯ ")
            id_zamowienie = input ("id_zamowienie (może pozostać puste):\n❯ ")
            status = input ("status: ()\n❯ ")
            query = ("""UPDATE magazyn SET id_produkt = %s, ilosc = %s, data_produkcji = %s, id_zamowienie = %s, status = %s WHERE id_produkt = %s""")
            cursor.execute(query, (id_produkt, ilosc, data_produkcji, id_zamowienie, status),multi = True)
            connection.commit() 
            print("Rekord został pomyślnie edytowany\n")
            magazynierMenu()
                        
        elif confirmation == "n":
            print("Rekord nie został edytowany\n")
            magazynierMenu()
            
        else:
            print("Wybierz poprawną opcję")
            magazynierMenu()
#*MAGAZYNIER

#*KADROWY
def kadrowyMenu():
    print("\nTwoja rola to: Kadrowy\n")
    kadrowyMenuInput = input("Wybierz opcję:\n 1. Wyświetl spis pracowników\n 2. Dodaj pracownika\n 3. Edytuj pracownika\n 4. Usuń pracownika\n 0. Wstecz\n\n❯ ")
    
    if kadrowyMenuInput == "0":
        mainMenu()
        
    elif kadrowyMenuInput == "1":
        def kadrowyPracownicyMenu():
            kadrowyPracownicyMenuInput = input("Wybierz opcję:\n 1. Sortuj: ID\n 2. Sortuj: Nazwisko\n 0. Wstecz\n\n❯ ")
            
            if kadrowyPracownicyMenuInput == "0":
                kadrowyMenu()
                
            elif kadrowyPracownicyMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY id_pracownik")
                print("ID    |IMIĘ       |NAZWISKO    |ROLA")
                cursor.execute(query)
                for (id_pracownik, imie, nazwisko, rola) in cursor:
                    print("{}     |{}     |{}    |{}".format(id_pracownik, imie, nazwisko, rola))
                print("\n\n")
                kadrowyPracownicyMenu()
                
            elif kadrowyPracownicyMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY nazwisko")
                print("ID    |IMIĘ       |NAZWISKO    |ROLA")
                cursor.execute(query)
                for (id_pracownik, imie, nazwisko, rola) in cursor:
                    print("{}     |{}     |{}    |{}".format(id_pracownik, imie, nazwisko, rola))
                print("\n\n")
                kadrowyPracownicyMenu()
        kadrowyPracownicyMenu()
        
    elif kadrowyMenuInput == "2":
        imie = input ("imię:\n❯ ")
        nazwisko = input ("nazwisko:\n❯ ")
        query = """INSERT INTO pracownicy (imie, nazwisko)VALUES (%s, %s)"""
        cursor.execute(query, (imie, nazwisko), multi=True)
        connection.commit()
        print("Pracownik został pomyślnie dodany do spisu pracowników\n")
        kadrowyMenu()

    elif kadrowyMenuInput == "3":
        id_pracownik = (input ("Podaj numer ID pracownika do edycji:\n❯ "), )
        print("Wyświetlam obecne dane pracownika:\n")
        print("ID    |IMIĘ       |NAZWISKO    |ROLA")
        query = "SELECT * FROM pracownicy WHERE id_pracownik = %s"
        cursor.execute(query, id_pracownik)
        record = cursor.fetchone()
        print("{}     |{}     |{}    |{}".format(record[0],record[1],record[2],record[3]))
        confirmation = input("Czy napewno chcesz edytować tego pracownika? t/n\n❯ ")
            
        if confirmation == "t":
            print("Podaj nowe dane pracownika: \n")
            imie = input("imie:\n❯ ")
            nazwisko = input("nazwisko:\n❯ ")
            query = ("""UPDATE pracownicy SET imie = %s, nazwisko = %s WHERE id_pracownik = %s""")
            cursor.execute(query, (imie, nazwisko, id_pracownik[0]),multi = True)
            connection.commit() 
            print("Pracownik został pomyślnie edytowany\n")
            kadrowyMenu()
                
        elif confirmation == "n":
            print("Pracownik nie został edytowany\n")
            kadrowyMenu()
        
        else:
            print("Wybierz poprawną opcję")
            kadrowyMenu()
            
    elif kadrowyMenuInput == "4":
        id_pracownik = (input("Podaj ID pracownika do usunięcia:\n❯ "), )
        print("Wyświetlam informację o pracowniku przed jego usunięciem: ")
        print("ID    |IMIĘ       |NAZWISKO    |ROLA")
        query = """SELECT * FROM pracownicy WHERE id_pracownik = %s"""
        cursor.execute(query, id_pracownik)
        record = cursor.fetchone()
        print("{}     |{}     |{}    |{}".format(record[0],record[1],record[2],record[3]))
        confirmation = input("Czy napewno chcesz usunąć tego pracownika? t/n\n❯ ")
        
        if confirmation == "t":
            mySql_delete_record = """DELETE from pracownicy 
                                WHERE id_pracownik = %s"""
            cursor.execute(mySql_delete_record, id_pracownik)
            connection.commit()
            print("Pracownik został pomyślnie usunięty\n")
            kadrowyMenu()
            
        elif confirmation == "n":
            print("Pracownik nie został usunięty\n")
            kadrowyMenu()
    
        else:
            print("Wybierz poprawną opcję")
            kadrowyMenu()
#*KADROWY

#*ZARZĄD
def zarzadMenu():
    print("\nTwoja rola to: Zarząd Firmy\n\n")
    zarzadMenuInput = input("Wybierz opcję:\n 1. Wyświetl rejestr zleceń\n 2. Wyświetl rejestr produktów\n 3. Wyświetl stany magazynowe\n 4. Wyświetl spis pracowników\n 5. Statystyki\n 0. Wstecz\n\n❯ """)
    
    if zarzadMenuInput == "0":
        mainMenu()

    elif zarzadMenuInput == "1":
        def zarzadZleceniaMenu():
            zarzadZleceniaMenuInput = input("Wybierz opcję:\n 1. Wyświetl wszystkie zlecenia (Sortuj: od najstarszego)\n 2. Wyświetl wszystkie zlecenia (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 0. Wstecz\n\n❯ ")
            
            if zarzadZleceniaMenuInput == "0":
                zarzadMenu()
                
            elif zarzadZleceniaMenuInput == "3":
                def zarzadZleceniaFilterMenu():
                    zarzadZleceniaFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zrealizowane\n 2. W toku\n 3. Oczekujące\n 4. Opóźnione\n 5. Archiwalne\n\n❯"""))
                    query = ("""SELECT * FROM zamowienia WHERE status = %s""")
                    print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                    cursor.execute(query, (zarzadZleceniaFilterMenuInput,))
                    for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                        print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                    print("\n\n")
                zarzadZleceniaFilterMenu()
                
            elif zarzadZleceniaMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
                
            elif zarzadZleceniaMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM zamowienia ORDER BY data_zamow DESC")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA ZAMÓWIENIA    |DATA REALIZACJI    |ILOŚĆ PRAC.    |WEWNĘTRZNE    |STATUS    |ID KLIENTA")
                cursor.execute(query)
                for (id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{:%d %b %Y}        |{}              |{}             |{}         |{}".format(id_zamowienie, id_produkt, ilosc_zamow, data_zamow, data_realizacji, ilosc_pracownik, wewnetrzne, status, id_klient))
                print("\n\n")
            
            else:
                print("Wybierz poprawną opcję")
            zarzadZleceniaMenu()
        zarzadZleceniaMenu()
    
    elif zarzadMenuInput == "2":
        def zarzadProduktyMenu():
            zarzadProduktyMenuInput = input (""" 1. Wyświetl wszystkie produkty (Sortuj: ID)\n 2. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie\n 3. Wyświetl wszystkie produkty (Sortuj: Nazwa - Alfabetycznie (Odwrotność))\n 0. Wstecz\n\n❯ """)
            
            if zarzadProduktyMenuInput == "0":
                mainMenu()
                
            elif zarzadProduktyMenuInput == "1":
                print("\n\n")
                print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                query = ("SELECT * FROM produkty ORDER BY id_produkt")
                cursor.execute(query)
                for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                    print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                print("\n\n")
                zarzadProduktyMenu()
                
            elif zarzadProduktyMenuInput == "2":
                print("\n\n")
                print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                query = ("SELECT * FROM produkty ORDER BY nazwa")
                cursor.execute(query)
                for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                    print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                print("\n\n")
                zarzadProduktyMenu()
                
            elif zarzadProduktyMenuInput == "3":
                print("\n\n")
                query = ("SELECT * FROM produkty ORDER BY nazwa DESC")
                print("ID   |NAZWA         |NORMA/H        |JM         |TECHNOLOGIA")
                cursor.execute(query)
                for (id_produkt, nazwa, norma, jm, technologia) in cursor:
                    print("{}    |{}     |{}           |{}         |{}".format(id_produkt, nazwa, norma, jm, technologia))
                print("\n\n")
                zarzadProduktyMenu()
        zarzadProduktyMenu()
        
    elif zarzadMenuInput == "3":
        def zarzadMagazynMenu():
            zarzadMagazynMenuInput = input(""" 1. Wyświetl stany magazynowe (Sortuj: od najstarszego)\n 2. Wyświetl stany magazynowe (Sortuj: od najnowszego)\n 3. Filtruj: Status\n 4. Filtruj: ID Produktu\n 0. Wstecz\n\n❯ """)
            
            if zarzadMagazynMenuInput == "0":
                zarzadMenu()
                
            elif zarzadMagazynMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query)
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                zarzadMagazynMenu()
        
            elif zarzadMagazynMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM magazyn ORDER BY data_produkcji DESC")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query)
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                zarzadMagazynMenu()
                
            elif zarzadMagazynMenuInput == "3":
                def zarzadMagazynFilterMenu():
                    zarzadMagazynFilterMenuInput = int (input ("""Wybierz status do wyświetlenia:\n 1. Zapas\n 2. Zarezerwowany\n 3. Niedostępny\n\n❯ """))
                    query = ("""SELECT * FROM magazyn WHERE status = %s""")
                    print("\n\n")
                    print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                    cursor.execute(query, (zarzadMagazynFilterMenuInput,))
                    for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                        print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                    print("\n\n")
                    zarzadMagazynMenu()
                zarzadMagazynFilterMenu()
                
            elif zarzadMagazynMenuInput == "4":                
                zarzadMagazynRegisterFilterMenuInput = int (input ("""Podaj ID produktu\n\n❯"""))
                query = ("""SELECT * FROM magazyn WHERE id_produkt = %s""")
                print("\n\n")
                print("ID    |PRODUKT    |ILOŚĆ    |DATA PRODUKCJI     |ID ZAMÓWIENIA    |STATUS")
                cursor.execute(query, (zarzadMagazynRegisterFilterMenuInput,))
                for (id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status) in cursor:
                    print("{}     |{}          |{}     |{:%d %b %Y}        |{}                |{}".format(id_zasob, id_produkt, ilosc, data_produkcji, id_zamowienie, status))
                print("\n\n")
                print("\n\n")
                zarzadMagazynMenu()
                
            else:
                print("Wybierz poprawną opcję")
                zarzadMagazynMenu()
        zarzadMagazynMenu()
        
    elif zarzadMenuInput == "4":
        def zarzadPracownicyMenu():
            zarzadPracownicyMenuInput = input ("Wybierz opcję:\n 1. Sortuj: ID\n 2. Sortuj: Nazwisko\n 0. Wstecz\n\n❯ ")
            
            if zarzadPracownicyMenuInput == "0":
                zarzadMenu()
                
            elif zarzadPracownicyMenuInput == "1":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY id_pracownik")
                print("ID    |IMIĘ       |NAZWISKO    |ROLA")
                cursor.execute(query)
                for (id_pracownik, imie, nazwisko, rola) in cursor:
                    print("{}     |{}     |{}    |{}".format(id_pracownik, imie, nazwisko, rola))
                print("\n\n")
                zarzadPracownicyMenu()
                
            elif zarzadPracownicyMenuInput == "2":
                print("\n\n")
                query = ("SELECT * FROM pracownicy ORDER BY nazwisko")
                print("ID    |IMIĘ       |NAZWISKO    |ROLA")
                cursor.execute(query)
                for (id_pracownik, imie, nazwisko, rola) in cursor:
                    print("{}     |{}     |{}    |{}".format(id_pracownik, imie, nazwisko, rola))
                print("\n\n")
                zarzadPracownicyMenu()
                
            else:
                print("Podaj poprawną opcję")
                zarzadPracownicyMenu()
        zarzadPracownicyMenu()
        
    elif zarzadMenuInput == "5":
        print("Ta opcja nie została jeszcze zaimplementowana\n\n")
#*ZARZĄD

welcome()            
main()
