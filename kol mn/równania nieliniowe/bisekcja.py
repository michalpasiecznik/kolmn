# Obliczanie miejsca zerowego równań nieliniowych metodą Bisekcji
#pip install sympy
from sympy import *

x = symbols('x')  # deklaracja symboli funkcji

# deklaracja funkcji. '**' oznacza '^'
f = lambda x: (x + 1) * (x - 1) ** 4

epsilon = 0.001  # ustalamy dokładność błędu

a = float(input("Podaj lewą granicę przedziału: "))
b = float(input("Podaj prawą granicę przedziału: "))
iterations = 0

if f(a) * f(b) >= 0:
    print("Funkcja nie przyjmuje różnych znaków na końcach przedziału.")
else:
    c = (a + b) / 2
    while abs(f(c)) > epsilon:
        if abs(f(c)) <= epsilon:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        iterations += 1

    print("Wynik: " + str(c))
    print("Liczba iteracji: " + str(iterations) + "\n")
