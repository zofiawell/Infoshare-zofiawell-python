# 1. napisz program sumujący wszystkie elementy w liscie

lista = [4,5,6,8,10, 20, -1]
suma = sum(lista[0:])
print(suma)

# 2. znajdz najwiekszy / najmniejszy element w liscie

min = min(lista[:])
maks = max(lista[:])

print(min)
print(maks)

# 3. program wydający resztę z podanych monet []
# (czyli teraz uzytkownik moze podac monety),
# wczytujemy dostępne monety z input'a dopóki nie dostaniemy znaku "Q"


monety = (input("jakie masz monety? Jeśli skończyłeś podawać wpisz 'q'"))
dost_monety = []

while monety != 'q':
    for moneta in monety:
        moneta = int(moneta)
        dost_monety.append(moneta)

    monety = (input("jakie masz monety? Jeśli skończyłeś podawać wpisz 'q'"))

if monety == 'q':
    pass

print("Twoje monety to", dost_monety)

reszta_monety = []
reszta_kwota = 5
do_wydania = 5
print("Do wydania jest", do_wydania, "zł")

if sum(dost_monety[:]) < do_wydania:
    print("nie mogę wydać reszty")

for moneta in dost_monety:
    if moneta < reszta_kwota:
        reszta_monety.append(moneta)
        reszta_kwota = reszta_kwota - moneta

print("Twoja reszta to:")
for moneta in reszta_monety:
    print("{}zl, ".format(moneta), end="",)
print ("czyli łącznie", do_wydania, "zł")
