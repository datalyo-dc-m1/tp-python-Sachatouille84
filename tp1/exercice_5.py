a = int(input("Donnez le premier nombre : "))
print(a)
b = int(input("Donnez le premier nombre : "))
print(b)
op = input("Donnez le symbole de l'opération: ")
print(op)
print()
if(op=='+'):
    print('Le résultat est', a+b)
if(op=='-'):
    print('Le résultat est', a-b)
if(op=='*'):
    print('Le résultat est', a*b)
if (op == '/'):
    if(b==0):
        print("Opération impossible")
    else:
        print('Le résultat est', a/b)
if (op!='+' and op!='-' and op!='*' and op!='/'):
    print("Opération inexistante. Veuillez choisir un opérateur ( + , - , * , /)")
