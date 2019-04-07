import sys
import os

class Kangur():

    def __init__(self, imie, torba):
        self.imie = imie
        self.torba = list(torba)

    def put_in(self, item):
        self.item = item
        self.torba.append(self.item)

    def __str__(self):
        napis = (f"Kangur {self.imie} ma w torbie {self.torba}")
        return napis


Kan = Kangur(imie = "Kan", torba = ["chleb"])
Gur = Kangur(imie = "Gur", torba = [])

print(Kan)
print(Gur)

Kan.put_in("bułki")
Gur.put_in("monitor")
print(Kan)
print(Gur)




