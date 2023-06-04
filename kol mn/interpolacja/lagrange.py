# Obliczanie wielomianu interpolacyjnego metoda Lagrange
from sympy import *

x = symbols('x')
wenz = []

n = int(input("Podaj stopień wielomianu interpolacyjnego: "))

for i in range(n + 1):
    a = float(input("Podaj współrzędną x" + str(i) + ": "))
    b = float(input("Podaj współrzędną y" + str(i) + ": "))
    wenz.append([a, b])

lambd_up = []
lambd_down = []

for i in range(len(wenz)):
    fup = 1
    fdown = 1
    for k in range(len(wenz)):
        if i != k:
            fup *= x - wenz[k][0]
            fdown = (wenz[i][0] - wenz[k][0]) * fdown

    lambd_up.append(fup)
    lambd_down.append(fdown)

funk = 0
for iter in range(len(wenz)):
    funk += wenz[iter][1] * (lambd_up[iter] / lambd_down[iter])

wyn = simplify(funk)
print(wyn)
