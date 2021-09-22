'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins au caractères spécial (/;|%, etc.)
La longeur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 6: Générateur de mot de passe ***")

# Votre code ici
import random,string

passwordSize = 0
allCharacters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
# print("Tous les caractères autorisés sont :", allCharacters)

while passwordSize < 4:
    try:
        passwordSize = int(input("Fixer la taille du mot de passe par un entier (minimum 4) : "))
    except:
        print("La saisie d'un nombre entier vous est demandée")

# Pour le mot de passe il faut au moins :
# -1 Majuscule
# -1 Minuscule
# -1 chiffre
# -1 caractère spécial
# rand1 contient 1 caractère de chaque type
rand1 = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.digits), random.choice(string.punctuation)]

if passwordSize > 4:
    for r in range(passwordSize-4):
        rand1.append(random.choice(allCharacters))

# Réarrangement dans un ordre aléatoire des caractères
random.shuffle(rand1)      # réarrangement aléatoire des éléments de la liste (ne fonctionne pas sur un 'str')
password = "".join(rand1)  # concaténation en str de chacun des éléments de la liste sans séparateur

# Affichage final
print("Nombre de caractères du mot de passe :", passwordSize)
print("Mot de passe :", password)

