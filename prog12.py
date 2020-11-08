koszyk_items = ['mleko', 'czekolada', 'sok']
koszyk_ilosc = [2, 1, 3]
koszyk_cena = [30,40, 20]

suma = 0.0
for idx in range(len(koszyk_items)):
    item = koszyk_items[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena[idx]
    
    print("{0} {1} {2}".format(item, ile, cena))
    suma = suma + cena
print("Wartosc koszyka {0} przed znizka".format(suma))

if 'mleko' in koszyk_items and 'czekolada' in koszyk_items:
    print('Hurrra! Znizka!')
    suma = suma - (suma * 10)/100
print("Wartosc koszyka {0} po znizka".format(suma))
