# 4. program ktory zmieni zdanie w liste wyrazow

zdanie = "Ala ma kota, kot ma Ale."
lista = []
slowo = ""

for znak in zdanie:
   if znak != " " and znak != "," and znak != ".":
       slowo = slowo + znak
   elif znak == " " or znak ==".":
       lista.append(slowo)
       slowo = ""


print(lista)
policz = len(lista)
print(policz)



# 5. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

stringi = ['abc', 'xyz', 'aba', '1221']
stringi2 = []
for string in stringi:
    if string[0] == string[-1]:
        if len(string) > 2:
            stringi2.append(string)

odp = len(stringi2)
print("są", odp, "takie stringi")



# 6. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]
lista_b = []

for wartosc in lista_a:
    if wartosc not in lista_b  and lista_a.count(wartosc) ==1:
        lista_b.append(wartosc)
print(lista_b, "pojedyńcze wartości")



# 7. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)

lista_d = [10,20,30,20,10,50,60,40,80,50,40]
print(lista_d)
wynik = list(set(lista_d))
print(sorted(wynik))
dlug = len(wynik)
dlug = int(dlug)
print(dlug)

for liczba in wynik:
    if 2 >= wynik.count(liczba):
        wynik.remove(liczba)

print(wynik)



