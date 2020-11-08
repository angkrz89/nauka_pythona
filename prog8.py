samochody = ['syrena', 'polonez']

print(samochody[0])
print(samochody[1])

print("=== petla1 ===")
for s in samochody:
    print(s)

for idx in[0,1]:
    print(samochody[idx])

print("=== petla2 po indexie ===")
for idx in range( len(samochody) ):
    print(samochody[idx])
