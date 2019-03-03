# 4. oblicz ocenę na podstawie progu procentowego

wynik=input('\nPodaj procentowy wynik Twojego egzaminu\n')

print("Twoj wynik to "+wynik+'%')
wynik = int(wynik)
if wynik < 50:
    print ("Ocena: niedostateczny (1)")
if  51 < wynik < 60 :
    print ("Ocena: mierny (2) ")
if 61 < wynik < 70:
    print("Ocena: dostateczny (3)")
if 71 < wynik < 80:
    print("Ocena: dobry (4)")
if 81 < wynik < 90:
    print("Ocena: bardzo dobry (5)")
if 91 < wynik :
    print("Ocena: celujący (6)")