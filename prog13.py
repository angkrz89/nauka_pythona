 # klucz wartosc
samolot = {'name': 'boeing',
           'przebieg': 1000.50,
           'type': 'pasazerki' }

# lista_dostep_po_kluczy = {'PESEL1': 'Wotjek', 'PESEL2': 'Kat'}

print(samolot['name'])
print(samolot['przebieg'])
print(samolot['type'])

samolot['silnik'] = 'odrzutowy'
# co stanie
# print(samolot['xyz'])
# print(samolot.get('xyz'))

print("==== petla po kluczu - key ===")
for klucz in samolot:
    print("{0}: {1}".format(klucz, samolot[klucz]))

print("=== petla klucz/wartosc - key/value ===")
for key, value in samolot.items():
    print("{0} {1}".format(key, value))
