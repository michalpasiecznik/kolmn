# Obliczanie miejsca zerowego równań nieliniowych metodą falsi
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
    # obliczenia
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    iterations = 0

    while abs(f(xn)) > epsilon:
        x1 = (xn * f(a) - a * f(xn)) / (f(a) - f(xn))
        x2 = (xn * f(b) - b * f(xn)) / (f(b) - f(xn))
        if f(a) * f(xn) < 0:
            xn = x1
        else:
            xn = x2
        iterations += 1

    print("Wynik: " + str(xn))
    print("Liczba iteracji: " + str(iterations) + "\n")
