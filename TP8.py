'''
*** EXO 8: Health Check ***
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listés répond
à raison d'une requête toutes les n secondes => module natif "time"

la périodicité sera fournie en entrée par l'utilisateur

On produira en sortie un fichier de log "health.log" qui contiendra:
- la date de la requête
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse
'''
print("*** EXO 8: Health Check ***")

# votre code ici
import time, datetime
import requests

checkPeriod = 0
while checkPeriod == 0:
    try:
        checkPeriod = int(input("Veuillez saisir l'intervalle de temps (en secondes) entre chaque 'Health Check' : "))
    except:
        print("Un entier vous est demandé")

print("Le 'Health Check' est effectué toutes les %d secondes" % checkPeriod)
print("Pour quitter le programme : Ctrl+C")

f = open("websites.txt", "r") # Ouverture fichier en lecture seule
siteCheckList = f.read()      # lecture du fichier et stockage de son contenu
f.close()                     # libération du fichier

siteUrl = siteCheckList.splitlines()

# Décommenter les 3 lignes si vous désirez effacer le contenu du fichier "health.log"
# flog = open("health.log", "w") # Ouverture fichier en écriture
# flog.write("")                 # fichier avec un contenu vide
# flog.close()                   # libération du fichier

# Ouverture du fichier pour enregistrement continue jusqu'à interruption utilisateur
flog = open("health.log", "a") # Ouverture fichier en écriture (chaque écriture est ajoutée en fin de fichier)

while True:
    try:
        for r in siteUrl:
            # print(r)
            today = datetime.datetime.today()
            try:
                responseCheck = requests.get(r)
                # print(responseCheck.status_code)
                if responseCheck.status_code == 200:
                    # print("%s : le site '%s' est parfaitement disponible" % (today,r))
                    flog.write(f"{today} : le site '{r}' est parfaitement disponible\n")
                else:
                    # print("%s : le site '%s' rencontre une erreur %d" % (today, r, responseCheck.status_code))
                    flog.write(f"{today} : le site '{r}' rencontre une erreur {responseCheck.status_code}\n")
            except:
                # print("%s : le site '%s' est inconnu/indisponible" % (today,r))
                flog.write(f"{today} : le site '{r}' est inconnu/indisponible\n")
        flog.write("\n") # ajout d'une ligne vide entre chaque 'health check' pour la lisibilité du fichier
        time.sleep(checkPeriod)
    except:
        KeyboardInterrupt # Vérifie si demande d'interruption de l'utilisateur (Ctrl+C)
        print(" Demande utilisateur : Sortie immédiate de la boucle infinie (arrêt du 'health check')")
        break

flog.close() # fermeture du fichier de log
print("Rappel : Le 'Health Check' est enregistré dans le fichier 'health.log'")





