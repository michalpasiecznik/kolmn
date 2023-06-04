# kwadratury metodą trapezów prostych
from sympy import *

x = symbols('x')  # deklaracja symboli funkcji

# deklaracja funkcji. '**' oznacza '^'
f = x ** 2

a = float(input("Podaj dolną granicę przedziału: "))
b = float(input("Podaj górną granicę przedziału: "))

# obliczenia
wyn = ((b - a) / 2) * (f.subs(x, a) + f.subs(x, b))
print("Wynik to: " + str(wyn))

psi = max(f.subs(x, a), f.subs(x, b))
err = (1.0 / 12.0) * (b - a) ** 3 * diff(f, x, 2).subs(x, psi)
print("Błąd to: " + str(err))
