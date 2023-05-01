# print("Incepe programul...")
# input()
# print('Gata')

# cu \n fortam sa treaca pe linia urmatoare
name = input("Care este numele tau?\n")
print(f"Salut, {name}!")

age = input("Ce varsta ai? \n")
age = int(age) # by default , input imi da mereu un string , convertez in INT!!!
print(f"acuma ai {age} ani , la anul vei avea {age + 1}")