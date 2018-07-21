def menu():
    print('\nSistema Magazzino Libri v1.0')
    print('+--------------------------+')
    print('1. Ricerca ed acquisto libro')
    print('2. Ordina libro da fornitore')
    print('3. Aggiorna magazzino da ordini\n')

def giacenza(titolo):
    if titolo in magazzino:
        print('In magazzino il libro', titolo, 'è presente ---> Quantità =', magazzino[titolo])
        print('')
        return True
    else:
        print('Libro non presente in magazzino.\n')
        return False

def acquisto(titolo):
    print("")
    test=False
    if magazzino[titolo]>0:
        while test==False:
            b=input("Vuoi comprare questo libro?(s/n)")
            if b in l_si:    
                magazzino[titolo]-=1
                print(magazzino)
                test=True
            elif b in l_no:
                print('Acquisto annullato')
                test=True
            else:
                print('Scelta non valida. Inserisci si o no')
    else:
        print('Non si può procedere ad acquistare il libro')
        print('Le copie del titolo sono finite.')

def ordinazione(titolo):
    global lista_ordini
    ok=True
    print("\nIl titolo del libro selezionato è:")
    print("--->",  titolo)
    test=input("Confermi di voler ordinare il titolo dal fornitore?(s/n)")
    while ok==True:
        if test in l_si:
            copie=eval(input("\nInserisci quante copie del titolo ordinare:"))
            lista_ordini[titolo]=copie
            ok=False
        elif test in l_no:
            print('Ordinazione titolo annullato')
            ok=False
        else:
            print('Scelta non valida. Scegli si o no.')

def aggiorna_magazzino(lista_ordini):
    global magazzino
    lista_ordini_inseriti={}
    l_opz2=["1", "2", "3", "4"]
    print('\nAcquisizione Ordine')
    print('+--------------------------+')
    print('1. Acquisizione singola')
    print('2. Acquisizione complessiva')
    print('3. Cancellazione ordine')
    print('4. Torna al menù principale\n')
    opzione=input('Scegli il numero dell\'opzione: ')
    if opzione in l_opz2:
        if opzione=="1":
            a=0
            i=len(lista_ordini)
            while a<i:
                print(lista_ordini[a])
                b=input('Vuoi inserire il libro in magazzino?')
                if b in l_si:
                    magazzino=magazzino+lista_ordini[a]
                    lista_ordini_inseriti=lista_ordini_inseriti+lista_ordini[a]
                else:
                    print('Libro non inserito')
                lista_ordini=lista_ordini-lista_ordini_inseriti
            aggiorna_magazzino(lista_ordini)
        elif opzione=="2":
            aggiorna_magazzino(lista_ordini)
            pass
        elif opzione=="3":
            aggiorna_magazzino(lista_ordini)
            pass
        else:
            input('Ritorno al menù principale. Premi invio.')
    else:
        aggiorna_magazzino(lista_ordini)

    


l_si=["s", "S", "si", "SI", "Si", "sI"]
l_no=["n", "N", "no", "NO", "No", "nO"]
l_opz=["1", "2", "3"]
magazzino={"test":1}
opzione="1"
lista_ordini={"ciao":2}

while True:
    menu()
    opzione=input('Scegli una opzione dal menù: ')
    print("")
    if opzione in l_opz:
        if opzione=="1":
            titolo=input('Inserisci il titolo: ')
            if giacenza(titolo)==True:
                acquisto(titolo)
            else:
                ordinazione(titolo)
            input("Premi invio per continuare.")
        elif opzione=="2":
            pass
            ordinazione(input("Inserisci il titolo del libro che vuoi ordinare: "))
            print(lista_ordini)
        else:
            aggiorna_magazzino(lista_ordini)
    else:
        print('\nScelta non riconosciuta. Riprovare')

