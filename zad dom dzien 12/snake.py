class Zwierz():
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def mow(self):
        print(f"Zwierzak {self.nazwa} nic nie mówi")

    def ruszaj(self):
        print(f"Zwierzak {self.nazwa} się rusza")



class Waz(Zwierz):
    def __init__(self, nazwa, glowa, czlon):
        self.nazwa = nazwa
        self.glowa = glowa
        self.czlon = int(czlon)

    def glowa(self):
        if self.czlon == 1:
            print(f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlon.")
        elif self.czlon in range(2,4):
            print(f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlony.")
        else:
            print(f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlonów.")

    def czolgaj(self ):
        print(f"Waz {self.nazwa} się czolga")

    def dodaj_czlon(self, ile):
        self.ile = int(ile)
        self.czlon = self.czlon + ile
        # self.czlon +=1
        if self.czlon in range (2,4):
            print(f"Waz {self.nazwa} ma teraz {self.czlon} czlony.")
        else:
            print(f"Waz {self.nazwa} urósł i ma teraz {self.czlon} czlonow")

    def __str__(self):
        if self.czlon == 1:
            return f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlon"
        elif self.czlon in range(2, 4):
            return f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlony"
        else:
            return f"Waz {self.nazwa} ma glowe typu {self.glowa} oraz ma {self.czlon} czlonów"
