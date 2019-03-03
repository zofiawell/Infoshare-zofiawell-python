# 3. czy liczba jest podzielna przez 3, 5, 7

liczba = input("\nPodaj liczbę\n")

if liczba.isdigit() and int(liczba) != 0:
    print('Podano liczbę '+liczba)
    liczba = int(liczba)
    if liczba % 3 == 0:
        print("liczba jest podzielna przez 3")
    else:
        print("liczba nie jest podzielna przez 3")
    if liczba % 5 == 0:
        print("liczba jest podzielna przez 5")
    else:
        print("liczba nie jest podzielna przez 5")
    if liczba % 7 == 0:
        print("liczba jest podzielna przez 7")
    else:
        print("liczba nie jest podzielna przez 7")
