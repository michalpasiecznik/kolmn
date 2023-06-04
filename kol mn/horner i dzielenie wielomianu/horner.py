# Wartość wielomianu w punkcie przy pomocy schematu Hornera

print("Podaj stopień wielomianu: ")
stopien = int(input())

wspolczynniki = []

for i in range(stopien + 1):
    print("Podaj współczynnik dla x^" + str(stopien - i) + ": ")
    wspolczynniki.append(float(input()))

print("Podaj wartość x0: ")
x = float(input())
wynik = wspolczynniki[0]

for i in range(1, stopien + 1):
    wynik = wynik * x + wspolczynniki[i]

print("Wartość wielomianu dla x0=" + str(x) + ": " + str(wynik))