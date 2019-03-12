# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

gra=(input('\nGra Kółko i krzyżyk\n podaj dziewięć znaków tylko x lub o\n'))



# gra = "oxooxxxox"
print(gra[0:3])
print(gra[3:6])
print(gra[6:])
if gra [0] == 'x':
    if gra[0] == gra[1] == gra [2] or \
    gra[0] == gra[3] == gra [6] or \
    gra[0] == gra[4] == gra [8]:
            print ("wygrało x")

elif gra [0] == 'o':
    if gra[0] == gra[1] == gra[2] or \
    gra[0] == gra[3] == gra[6] or \
    gra[0] == gra[4] == gra[8]:
            print("wygrało o")

if gra[2] == 'x':
    if gra[2] == gra[4] == gra [6] or \
    gra[2] == gra[5] == gra [8]:
            print ("wygrało x")
elif gra[2] == 'o':
    if gra[2] == gra[4] == gra [6] or \
    gra[2] == gra[5] == gra [8]:
            print ("wygrało o")

if gra[4] == 'x':
    if gra[1] == gra[4] == gra [7] or \
    gra[3] == gra[4] == gra [5]:
            print ("wygrało x")
elif gra[4] == 'o':
    if gra[1] == gra[4] == gra [7] or \
    gra[3] == gra[4] == gra [5]:
            print ("wygrało o")

if gra[6] == 'x':
    if gra[6] == gra[7] == gra [8]:
            print ("wygrało x")
elif gra[6] == 'o':
    if gra[6] == gra[7] == gra [8]:
            print ("wygrało o")


