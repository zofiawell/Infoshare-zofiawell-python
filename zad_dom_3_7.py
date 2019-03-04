# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

miesiac = input("\nPodaj nazwę miesiąca (z małej litery), a powiem ile jest w nim dni:\n")

styczeń_ilość = 31
luty_ilość_n = 28
luty_ilość_p = 29
marzec_ilość = 31
kwiecień_ilość = 30
maj_ilość = 31
czerwiec_ilość = 30
lipiec_ilość = 31
sierpień_ilość = 31
wrzesień_ilość = 30
październik_ilość = 31
listopad_ilość = 30
grudzień_ilość = 31

miesiace = set(["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"])
while miesiac not in miesiace:
    print('Nie podano miesiąca poprawnie, spróbuj raz jeszcze')
    miesiac = input("\nPodaj nazwę miesiąca, a powiem ile jest w nim dni:\n")

if miesiac == "styczeń":
    print("Jest", styczeń_ilość, "dni w tym miesiącu.")

if miesiac == "luty":
    rok = input("\nPodano luty, dlatego dodaj którego roku:\n")
    rok = int(rok)
    if rok % 400 == 0:
        print("Jest",luty_ilość_p,"w tym miesiącu w roku przestępnym.")
    elif rok % 4 == 0 and rok % 100 != 0:
        print("Jest",luty_ilość_p,"w tym miesiacu w roku przestępnym.")
    else:
        print("Jest",luty_ilość_n,"w tym miesiącu w roku nieprzestępnym.")

if miesiac == "marzec":
    print("Jest", marzec_ilość, "dni w tym miesiącu.")

if miesiac == "kwiecień":
    print("Jest", kwiecień_ilość, "dni w tym miesiącu.")

if miesiac == "maj":
    print("Jest", maj_ilość, "dni w tym miesiącu.")

if miesiac == "czerwiec":
    print("Jest", czerwiec_ilość, "dni w tym miesiącu.")

if miesiac == "lipiec":
    print("Jest", lipiec_ilość, "dni w tym miesiącu.")

if miesiac == "sierpień":
    print("Jest", sierpień_ilość, "dni w tym miesiącu.")

if miesiac == "wrzesień":
    print("Jest", wrzesień_ilość, "dni w tym miesiącu.")

if miesiac == "październik":
    print("Jest", październik_ilość, "dni w tym miesiącu.")

if miesiac == "listopad":
    print("Jest", listopad_ilość, "dni w tym miesiącu.")

if miesiac == "grudzień":
    print("Jest", grudzień_ilość, "dni w tym miesiącu.")

