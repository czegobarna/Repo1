#flow control

"""
if conditie:
    acest cod
    va fi executat
....
"""
# age = 19
# print("Inainte de if")
#
# if age > 18:
#     print('Esti major')
#     print('Felicitari')
#
# print("dupa if")

#
# nota_de_trecere = 4.5
# nota_primita = float(input("Introdu nota primita: \n"))
# if nota_primita >= nota_de_trecere:
#     print("Felicitari")
# else:
#     print("Imi pare rau")


# MAXIM 3 INDENTARE!!!
# if age >= 18:
#     print('Esti major')
#     if age >= 65:
#         print("esti pensionar")
#         if age > 100:
#             print("esti centagenar")
#     else:      # daca varsta este mai mica de 65
#         print("esti adulta , dar nu pensionar")
#
"""
elif (else-if)
in conditie1:
    cod execautat cand conditie1 este adevarat
elif conditie2:
    cod executat cond conditie2 este adeverat
elif conditie3:
    codul executat cand coditie 3 este adevarat
.... 
else:
    cod executat cand niciuna dintre coditiile de mai sus nu sunt adevarate
"""

years_of_experience = int(input("Introdu ani de exper: \n"))


if years_of_experience == 0:

    #aici va intra daca yoe este 0
    print("esti junior , poti merge la un intern")
elif years_of_experience < 3:
    #aici va intra daca yoe este 1 sau 2
    print("Esti junior , salariul tau este 4000")
elif years_of_experience < 5:
    #aici va intra daca yoe este 3 sau 4
    print("esti mid salaru este 8000")
elif years_of_experience < 10:
    # aici va intra daca yoe este 5-9 (inclusiv)
    print("esti senior, salaru e 12000")
else:
    #aici intra daca yoe este 10 sau mai mare
    print("felicitari esti pensionat!")