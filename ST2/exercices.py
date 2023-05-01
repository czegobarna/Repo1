# """
# Note din romana in americana
# """
#
# grade = float(input("Introdu nota:\n"))
# american_grade = ""
#
# """
# In general, input checks sunt PRIMELE chestii pe care le facem:
# fail-fast, adica ai introdus date gresite vrem sa scapam de el cat mai repede
# """
#
# if grade > 10 or grade <= 0:
#     print("ai introdus valoare gresita")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade <8:
#         american_grade = "C"
#     elif grade <9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#     #afisam mesajul doar daca nota introdusa a fost corecta!
#     print(f"Felicitari ai luat nota {american_grade}")

"""
14.         xyz (int)
Afiseaza care este cel mai mare dintre ele
"""

# x = int(input("Introdu x:\n"))
# y = int(input("Introdu y:\n"))
# z = int(input("Introdu z:\n"))
#
# maxi = x     # presupunem ca valoare maxima este x
# if maxi < y:
#     maxi = y
# if maxi < z:
#     maxi = z
# print(f"Valoarea este {maxi}")
# print(f"verificare: {max(x, y, z)}")

# solutia 2
