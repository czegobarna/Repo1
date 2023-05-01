'''
Functia print ne ajuta sa afisam informatii in terminal.
print(ceva , altceva , etc.) <= putem afisa oricate chestii cu , intre ele

'''

print('Adela', 'Neacsu', 'Hello', 123, True)

nume = 'Adela Neacsu'
print ('Numele meu este ' + nume)

print('Numele meu este')
print(nume)

varsta = 30
# print('Varsta mea este: ' + varsta) # nu e bine
# f-strings => un mod mai pythonic de a afisa variabile in mesaje
# punem un f'' si numele de variabile le punem intre{}

print(f"Numele meu este {nume} si am {varsta} de ani.")


