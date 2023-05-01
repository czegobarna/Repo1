# 1. ---------------------------------------
# if = daca
# else = altfel

# 2. ----------------------------------------
# x = int(input())
# if x <= 0:
#     print("Numarul introdus nu este natural!")
# else:
#     print("Numarul introdus este natural!")
#

# 3. ----------------------------------------
# x = int(input())
# if x < 0:
#     print("Numarul introdus este negativ")
# elif x == 0:
#     print("Numarul introdus este neutru")
# else:
#     print("Numarul introdus este pozitiv")

# 4. ----------------------------------------
# x = int(input())
# if x > -2 and x < 13:
#     print("Numarul este intre -2 si 13")
# else:
#     print("Numarul NU este intre -2 si 13")

# 5. -----------------------------------------
# print("Introdu x :")
# x = int(input())
# print("Introdu y :")
# y = int(input())
#
# if x - y >= 5:
#     print("Diferenta e mai mica")
# else:
#     print("Diferenta e mai mare")






# ---------------------------------------
# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# # introducem X - ul
# print("Introdu un nr.")
# x = int(input())
# # verificam daca X-ul este sau nu intre 5 si 27 folosind operator logic "not"
# if x not in range (5, 27):
#     print("Numarul NU ESTE intre 5 - 27")
# else:
#     print("Numarul ESTE intre 5 - 27")
# # printam rezultatele



# -----------------------------------------

# x și y (int)
# 7. Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

#Introducem x si y
# print("Introdu x:")
# x = int(input())
# print("Introdu y:")
# y = int(input())
# # Verificam daca x si y sunt egale sau nu
# if x == y:
#     print("x si y sunt egale")
# elif x != y:
#     print("x si y nu sunt egale")
#     # Verificam care dintre x si y este mai mare si afisam cel mai mare
#     if x > y:
#         print(f"Numarul mai mare dintre x si y este : x = {x}")
#     else:
#         print(f"Numarul mai mare dintre x si y este : y = {y}")




# 8. ---------------------------------------
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare

# Printam cele 3 puncte ale triunghiului
# print("Puntul x al triunghiului")
# x = int(input())
# print("Puntul y al triunghiului")
# y = int(input())
# print("Puntul z al triunghiului")
# z = int(input())
#
# if x == y == z:
#     print("Triunghiul este echilateral")
# elif x != y == z:
#     print("Triunghiul este isoscel")
# elif y != x == z:
#     print("Triunghiul este isoscel")
# elif z != x == y:
#     print("Triunghiul este isoscel")
# else:
#     print("Triunghiul este oarecare")

# 9. -------------------------------------------
# print("Introdu o litera: ")
# x = str(input())
# if x == "A" or x == "a" or x == "E" or x == "e" or x == "I" or x == "i" or x == "O" or x == "o" or x == "U" or x == "u":
#     print(f"Litera  este o vocala")
# else:
#     print("Litera introdusa este o consoana ")
#
# 10. --------------------------------------------
#
# grade = float(input("Introdu nota:\n"))
# american_grade = ""
#
# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "C"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#     # afisam mesajul doar daca nota introdusa a fost corecta!
#     print(f"Felicitari, ai luat nota {american_grade}")
#
#
# 11. -------------------------------------------------------
# x = int(input())
# if x >= 1000:
#     print(f"{x} are 4 sau mai multe cifre")








# 0. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
# Printează nota după modificare

dict1 = {"Ana" : 8, "Gigel" :10, "Dorel" :5}
dict1["Dorel"] = 6
print(f'Dorel are acum nota {dict1["Dorel"] }')













