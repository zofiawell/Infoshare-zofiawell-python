# 8. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
from random import choice

lista_a = ["kasia", "marek", "marian", "basia", "marek", "marian", "gosia"]
lista_b = ["Kasia", "Marian", "marek", "basia", "Kasia", "Marian", "marek"]

lista_A = set(lista_a)
lista_B = set(lista_b)

lista_mix = lista_A.intersection(lista_B)
print(lista_mix)
if int(len(lista_mix)) > 0:
    print(True)

# 9. stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *

tablica = "****"
for i in range(5):
    wiersz = tablica[0:4]
    print(wiersz, "-------------")

napis = "*"* 4
napis = napis + "\n"
napis = napis * 5
print(napis)

for i in range(5):
    print("*"* 4)

# 10. wybierz losowo element z listy

print(choice(lista_a))

# 11. oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???

my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]
#najpierw rozwiązanie na piechotę, ale tak by działało dla każdej listy:

dlug_list = int(len(my_list)) #liczę elementy listy
my_list_zbior = set(my_list)
my_list_zbior = list(my_list_zbior)
dlug_zbior = int(len(my_list_zbior)) #liczę elementy unikalne listy

a=0 #tym będę liczyć ile unikalnych elementów jest w liście my_list
n=0 #to mi będzie "przewijać" kolejne wartości z unikanej listy my_list_zbior

for j in range(dlug_zbior):
    for i in range(dlug_list):
        if i != range(dlug_list)[-1]:
            if my_list[i] == my_list_zbior[n]:
                a = a+1
        else:
            print("Jest", a, my_list_zbior[n], "w liście")
            a=0
            n=n+1