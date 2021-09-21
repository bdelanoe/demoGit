'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

# Votre code ici
print("Taper 0 pour réaliser la somme des nombres saisis et quitter le programme")
userNumber = int(input("Veuillez saisir un nombre entier : "))
savedNumbers = []
sumNumbers = 0

while userNumber != 0:
    savedNumbers.append(userNumber)
    sumNumbers += userNumber
    userNumber = int(input("Veuillez saisir un nombre entier : "))

print("Somme des valeurs saisies : %s (%s)" % (sumNumbers,savedNumbers))




