t=input('Saisir votre taille (en mètre) = ')

if(t.isdigit()):
    taille=int(t)
else :
    print("ce n'est pas un entier, redémarrez le programme")
    exit()

m=input('Saisir votre poid (en kg)  = ')

if(m.isdigit()):
    poid=int(m)
else :
    print("ce n'est pas un entier, redémarrez le programme")
    exit()

imc = poid/(taille*taille)*10000

imcDescription = 'Vous êtes en état de maigreur'

if imc > 18.5:
    imcDescription = 'Vous êtes normal'
if imc > 24.9:
    imcDescription = 'Vous êtes en état de surpoid'
if imc > 29.9:
    imcDescription = 'Vous êtes en état d\'obésité'
if imc > 40:
    imcDescription = 'Vous êtes en état d\'obésité massive'

print(imcDescription, "imc :", imc)