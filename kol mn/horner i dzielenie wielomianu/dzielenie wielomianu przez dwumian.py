# Dzielenie wielomianu przez dwumian

n = int(input("Podaj stopień wielomianu: "))
wielomian = [0] * (n + 1)
i = n
for x in range(n + 1):
        wielomian[x] = float(input("Podaj współczynnik " + str(i) + " stopnia: "))
        i -= 1

dwumian = float(input("\nPodaj współczynnik dwumianu: "))

wynik = [0] * (n + 1)
wynik[0] = wielomian[0]

for x in range(n):
    wynik[x + 1] = dwumian * wynik[x] + wielomian[x + 1]

reszta = wynik.pop(n)

wielomian_string = ''
for x in range(n + 1):
    if x == n:
        wielomian_string += str(abs(wielomian[x]))
        break
    elif x == n - 1:
        wielomian_string += str(abs(wielomian[x])) + 'x'
    else:
        wielomian_string += str(abs(wielomian[x])) + 'x^' + str(n - x)
    wielomian_string += ' - ' if wielomian[x] < 0 else ' + '

dwumian_string = 'x  ' + str(abs(dwumian)) if dwumian < 0 else 'x - ' + str(dwumian)

print(wielomian_string + ' : ' + dwumian_string + " = " + wielomian_string)
print("Reszta z dzielenia: " + str(reszta))
