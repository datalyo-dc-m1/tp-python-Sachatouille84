# # Exo 1
# t = [1, 2, 3, 4, 5]
# a = t[0] + t[3] # 1 + 4 ==> 5
# b = t[-1]
# c = t[3:]
# a = a + t[-2]
#
# print("t est de type ", type(t))
# print  (a)
# print("b est de type ", type(b))
# print("c est de type ", type(c))
# print(t[1:]) # 1er element jusqu'à la fin
# print(t[3:]) # 3eme element jusqu'à la fin
# print(t[-4]) # 4 eme en partant de la fin
#
# abc=["A","B","C","D","E"]
# print(abc[3])
# print(abc[-3:])

# Exo 2

liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste) # longueur de la liste
b = liste[0]
liste.append(0) # ajout de i à la liste
c = len(liste)
d = liste[-1]

print(a)
print(b)
print(c)
print(d)

print(liste)

liste.append(2)
liste.append(9)
liste.append(1)

print(liste)

liste_2 = [3,6,8]

print(liste)

liste.extend(liste_2)

print(liste)

while liste.count(1) > 0:
    liste.remove(1)

print(liste)

liste.sort()

print(liste)

print("Min liste ", min(liste), "Max liste : ", max(liste))
print(sum(liste))

# Moyenne de la classe
print("EXERCICE : Moyenne de la classe ")

grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]
ecart = max(grades) - min(grades)
print("Ecart : ", ecart)

nombre_eleve = len(grades)
print("Nombre d'élèves : ",nombre_eleve)

grades.append(14)
print(grades)

grades[4] = 13

print(grades)

moyenne_classe = sum(grades) / len(grades)

print("La moyenne de la classe est : ", moyenne_classe)

grades.sort()


import statistics
print(statistics.median(grades))

cpt = 0
for i in grades:
    if grades[i] > 10:
        cpt = cpt + 1
print(cpt, "élèves ont validé la matière")



