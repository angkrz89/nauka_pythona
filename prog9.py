lotto = [59, 89, 2, 3, 4]

print(lotto[0])
print(lotto[1])
print(lotto[2])
print(lotto[3])
print(lotto[4])


print("=== petla 1 ===")
for s in lotto:
    print(s)

for idx in [0, 1, 2, 3, 4]:
    print(lotto[idx])

print("=== petla 2 po indexie ===")
print("len: {0}".format(len(lotto)))
print("range: {0}".format(range(4)))

for idx in range( len(lotto)):
    print("{0} {1}".format(idx, lotto[idx]))
