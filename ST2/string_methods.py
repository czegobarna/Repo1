"""
len(s) => ne da lungimea unui string, adica nr de caractere
"""

s = "Hello, World"

print(len(s)) # 12 caractere , se numara tot , inclusiv space , taburi , newline

ss = " \n"
print(len(ss)) # 2 adica un spatiu , si un newline

'''
Metode pe stringuri:
Metodele sunt niste sfunctii care se apeleaza pe o anumita variabile:

numa_var.numa_metoda()
'''

print(s.count('l'))  # numara cate caractere l avem in string
print(s.lower())  # converteste stringul la lowercase
print(s.upper()) # va face upper case



