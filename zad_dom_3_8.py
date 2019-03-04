 # 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

# a=34
# b=34
# c=45

print("\nRysujemy trójkąt:")
a=input("\nPodaj długość pierwszego boku trójkąta:\n")
b=input("Podaj długość drugiego boku trójkąta:\n")
c=input("Podaj długość trzeciego boku trójkąta:\n")

a = int(a)
b = int(b)
c = int(c)

if a < (b+c) and b < (a+c) and c < (a+b):
    # print("Można narysować trójkąt")
    if a == b or b == c or a == c:
        if a == b == c:
            print("Można narysować trójkąt i będzie to trójkąt równoboczny")
        else:
            print("Można narysować trójkąt i będzie to trójkąt równoramienny")
    else:
        print("Można narysować trójkąt i będzie to trójkąt różnoboczny.")
else:
    print("Nie można narysować trójkąta")





