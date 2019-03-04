# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku

data_miesiac = input("\nPodaj miesiąc w formacie MM\n")
data_miesiac = int(data_miesiac)

max_miesiac =12

while data_miesiac > max_miesiac:
    print("Podano niepoprawną wartość, spróbuj raz jeszcze")
    data_miesiac = input("\nPodaj miesiąc w formacie MM\n")
    data_miesiac = int(data_miesiac)

data_dzien = input("Podaj dzień w formacie DD\n")
data_dzien = int(data_dzien)

max_dzien=31

while data_dzien > max_dzien:
    print("Podano niepoprawną wartość, spróbuj raz jeszcze")
    data_dzien = input("Podaj dzień w formacie DD\n")
    data_dzien = int(data_dzien)

styczeń=1
luty=2
marzec=3
kwiecień=4
maj=5
czerwiec=6
lipiec=7
sierpień=8
wrzesień=9
październik=10
listopad=11
grudzień=12

pocz_zimy=22
pocz_wiosny=21
pocz_lata=22
pocz_jesieni=23

if data_miesiac == grudzień:
    print("Podana data to:", data_dzien, "grudnia")
if data_miesiac == listopad:
    print("Podana data to:", data_dzien, "listopada")
if data_miesiac == październik:
    print("Podana data to:", data_dzien, "października")
if data_miesiac == wrzesień:
    print("Podana data to:", data_dzien, "września")
if data_miesiac == sierpień:
    print("Podana data to:", data_dzien, "sierpnia")
if data_miesiac == lipiec:
    print("Podana data to:", data_dzien, "lipca")
if data_miesiac == czerwiec:
    print("Podana data to:", data_dzien, "czerwca")
if data_miesiac == maj:
    print("Podana data to:", data_dzien, "maja")
if data_miesiac == kwiecień:
    print("Podana data to:", data_dzien, "kwietnia")
if data_miesiac == marzec:
    print("Podana data to:", data_dzien, "marca")
if data_miesiac == luty:
    print("Podana data to:", data_dzien, "lutego")
if data_miesiac == styczeń:
    print("Podana data to:", data_dzien, "stycznia")

if styczeń <= data_miesiac  <= luty:
    print("Jest zima")

if kwiecień <= data_miesiac  <= maj:
    print("Jest wiosna")

if lipiec <= data_miesiac  <= sierpień:
    print("Jest lato")

if październik <= data_miesiac  <= listopad:
    print("Jest jesień")

if data_miesiac == grudzień and data_dzien >= pocz_zimy:
    print("Jest zima")
elif data_miesiac == grudzień and data_dzien < pocz_zimy:
    print("Jest jesień")

if data_miesiac == marzec and data_dzien >= pocz_wiosny:
    print("Jest wiosna")
elif data_miesiac == marzec and data_dzien < pocz_wiosny:
    print("Jest zima")

if data_miesiac == czerwiec and data_dzien >= pocz_lata:
    print("Jest lato")
elif data_miesiac == czerwiec and data_dzien < pocz_lata:
        print("Jest wiosna")

if data_miesiac == wrzesień and data_dzien >= pocz_jesieni:
    print("Jest jesień")
elif data_miesiac == wrzesień and data_dzien < pocz_jesieni:
    print("Jest lato")