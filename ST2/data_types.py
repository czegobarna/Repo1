'''
Tipuri de date:

1. numere  -> int (numere intregi)
           -> float ( numere cu virgula)
2. boolean -> true/fals (valoare logica)
3. siruri de caractere -> string (adica text libe )
'''

age = 30 # int
height = 1.80 # float
is_married = True  # boolean
has_children = False  # boolean
first_name = "Barni" # string
last_name = 'Czego' # string
description = "Putem scrie aici orice ne dorim , este un string poate contine cam orice"

alfa = "1234"  # acesta este un string , chiar daca are o valoare de numar
beta = "True"  # tot string
gamma= "1.21"  # tot string

"""
Functia type ne poate zice ce tip de data avem intr-o anumita variabila
"""

print(type(age))
print(type(height))
print(type(is_married))
print(type(first_name))

"""Ca sa schimbam tipul unei variabile numita casting:
Adica avem niste functii speciale (int str bool float)
care ne ajuta sa schimbam tipul variabile respective
"""

alfa = int(alfa) # as putea sa folosesc si float aici , daca as vrea sa obtin un numar zecimal
print('Dupa type casting: ', type(alfa))
beta = bool(beta)
print('Dupa type casting, beta: ', type(beta))
gamma = float(gamma)
print('Dupa type casting, gamma: ',type(gamma))

var_x = 'Text aiurea aici, care nu poate fi convertit'

print(int(3.14))
print(float(10))
print (int(True))
print(int(False))
print(bool(1999))