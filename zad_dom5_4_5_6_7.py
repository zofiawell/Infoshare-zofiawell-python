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
        stringi2.append(string)

odp = len(stringi2)
print("są", odp, "takie stringi")



# 6. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]
lista_b = []

for wartosc in lista_a:
    if wartosc not in lista_b:
        lista_b.append(wartosc)
print(lista_b, "unikalne wartości")



# 7. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_c = [10,20,30,20,10,50,60,40,80,50,40]
dl_listy_c = len(lista_c)
lista_c = sorted(lista_c)
print(lista_c)
if lista_c[0] == lista_c[1]:
    lista_c.remove(lista_c[1])
if lista_c[1] == lista_c[2]:
    lista_c.remove(lista_c[2])
if lista_c[2] == lista_c[3]:
    lista_c.remove(lista_c[3])
if lista_c[3] == lista_c[4]:
    lista_c.remove(lista_c[4])
if lista_c[4] == lista_c[5]:
    lista_c.remove(lista_c[4])
print(lista_c)

