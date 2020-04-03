n=int(input("Saisissez une valeur positive : "))
s=0
for x in range (n):
     if(x%2 != 0):
         print("impair", x)
         s=s+x
     else:
         print("faux")
print("La somme des impairs est", s)