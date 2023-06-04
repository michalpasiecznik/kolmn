# Obliczanie miejsca zerowego równań nieliniowych metodą siecznych
from sympy import *

x = symbols('x')  # deklaracja symboli funkcji

# deklaracja funkcji. '**' oznacza '^'
f = lambda x: (x + 1) * (x - 1) ** 4

epsilon = 0.0001  # ustalamy dokładność błędu

a = float(input("Podaj lewą granicę przedziału: "))
b = float(input("Podaj prawą granicę przedziału: "))

# sprawdzanie, czy funkcja ma przeciwne znaki w punktach a i b
if f(a) * f(b) >= 0:
    print("Funkcja nie przyjmuje różnych znaków na końcach przedziału.")
else:
    # znajdowanie punktu startowego
    x0 = a
    x1 = b
    x2 = 0
    iterations = 0

    while abs(f(x1)) > epsilon:
        x2 = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x2
        iterations += 1

    print("Wynik: " + str(x2))
    print("Liczba iteracji: " + str(iterations) + "\n")
