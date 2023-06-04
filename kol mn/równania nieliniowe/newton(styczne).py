# Obliczanie miejsca zerowego równań nieliniowych metodą stycznych (Newton)-
from sympy import *

x = symbols('x')  # deklaracja symboli funkcji

# deklaracja funkcji. '**' oznacza '^'
f = (x + 1) * (x - 1) ** 4

epsilon = 0.0001  # ustalamy dokładność błędu

a = float(input("Podaj lewą granicę przedziału: "))
b = float(input("Podaj prawą granicę przedziału: "))

# sprawdzanie, czy funkcja ma przeciwne znaki w punktach a i b
if f.subs(x, a) * f.subs(x, b) >= 0:
    print("Funkcja nie przyjmuje różnych znaków na końcach przedziału.")
else:
    # znajdowanie punktu startowego
    dx2 = diff(f, x, 2)
    dx = diff(f, x)

    if f.subs(x, a) * dx2.subs(x, a) > 0:
        x0 = a
    else:
        x0 = b

    iterations = 0

    while abs(f.subs(x, x0)) > epsilon:
        xn = x0 - (f.subs(x, x0) / dx.subs(x, x0))
        x0 = xn
        iterations += 1

    print("Wynik: " + str(x0))
    print("Liczba iteracji: " + str(iterations) + "\n")
