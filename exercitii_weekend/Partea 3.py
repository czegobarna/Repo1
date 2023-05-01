'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
# dict1 = {'ANA' :8, 'Gigel' : 10, 'Dorel' :5}
# for keys in dict1.keys():
#     print(keys)

'''
9. Printeazea cei 3 elevi si notele lor
Ex: 'Ana a luat nota {x}
Doar nota o vei lua folosindute de cheie

'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for keys, values in dict1.items():
    print(f'Ana a luat nota:{}