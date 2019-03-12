# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok=input('podaj rok\n')
rok = int(rok)
print(rok)
if rok % 400 == 0:
    print("jest przestępny")
elif rok % 4 == 0 and rok % 100 != 0:
    print ('rok jest przestępny')
else:
    print ('rok nie jest przestępny')