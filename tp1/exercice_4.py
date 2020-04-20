i=1
n=int(input("saisir une valeur de 1 à 100"))
if(n<1 or n>100):
    n = int(input("saisir une valeur de 1 à 100"))

while (i>=1 and i<=n):
    print(i)
    i=i+1

print("fin")