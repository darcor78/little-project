class Libro:

    def __init__(self, titolo, quantita):
        self.titolo = titolo
        self.quantita = quantita

    def scheda_libro(self):
        print("Scheda libro")
        print("     Titolo  :", self.titolo)
        print("     Quantità:", self.quantita)



check = False

titolo=input("Inserisci il titolo:")
while check==False:
    try:
        quantita=eval(input("Inserisci quanti ne hai:"))
        check=True
    except:
        print("Non hai inserito un numero intero")

a = Libro(titolo, quantita)
a.scheda_libro()
