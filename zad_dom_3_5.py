# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

wynik = input('\nPodaj wynik ruletki (cyfra/liczba od 1 do 36)\n')
wynik = int(wynik)
while wynik > 36:
    print ('Podałeś nieprawdidłową wartość, spróbuj raz jeszcze')
    wynik = input('\nPodaj wynik ruletki (cyfra/liczba od 1 do 36)\n')
    wynik = int(wynik)

# if wynik < 10:
#     print("Wynik to cyfra "+ wynik)
# else:
#     print ("Wynik to liczba " +wynik)

czarne = set ([2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35])
# parzyste

if wynik in czarne:
    print ('Jest czarna')
else:
    print ('Jest czerwona')

if wynik <18:
    print ('Jest niska')
else:
    print ('Jest wysoka')

if wynik % 2 == 0:
    print ('Jest parzysta')
else:
    print ('Jest nieparzysta')