from random import randint
number_to_guess=randint(0, 10)
print(number_to_guess)

user_propal=int(input("Saisissez une Valeur entre 0 et 10 : "))

if (user_propal >= 0, user_propal <=10):
    print("ok")
else:
    print("Le nombre n'est pas compris entre 0 et 10")
    exit()

if (user_propal == number_to_guess):
    print("Le nombre est égal à number_to_guess")
elif (user_propal < number_to_guess):
    print("Le nombre est plus petit que number_to_guess")
elif (user_propal > number_to_guess):
    print("Le nombre est plus grand que number_to_guess")