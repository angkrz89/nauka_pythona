# produkty = {'SS12': 'sukienka_trojka',
#             'P12': 'spodnia'}
#
# igla = 'P12'
#
# if igla in produkty:
#     print('istnieje!')
#     print(produkty['P12'])

produkty = {
            'SS12': {'nazwa': 'sukienka_trojka', 'rozmiary': ['s','l','xl']},
            'P12': {'nazwa': 'spodnia', 'rozmiary': ['s', 'xl']}
            }

for id in produkty:
    p = produkty[id]
    rozmiary = p['rozmiary']
    # print(p)
    # print(rozmiary)
    print(p['nazwa'])
    for r in rozmiary:
        print (r)
