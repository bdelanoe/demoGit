'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

# Votre code ici
import os,shutil

targetDir  = "flags" # On peut très bien avoir envie de faire la même chose avec un autre dossier d'origine
targetDirBis = targetDir + "Bis/" # NomDossierBis (dossier de destination)
files = os.listdir("flags") # Listing de tous les fichiers présent dans le dossier d'origine

# Avant de créer les fichiers, vérification de l'existance du dossier de destination 
if not os.path.isdir(targetDirBis):
    print("Le dossier cible '%s' n'existe pas" % targetDirBis)
    try:
        os.mkdir(targetDirBis)
        print("Le dossier cible '%s' a été créé" % targetDirBis)
    except:
        print("Impossible de créer le dossier cible '%s'" % targetDirBis)
        exit()
else:
    print("Le dossier '%s' existe déjà" % targetDirBis)

# to copy the file from source to destination.
# use shutil.copyfile(src, dst)
# Along with the path, the name of the file with its extension should be written

for f in files:
    extension = f[-3:]
    findExtension = "png"  # extension sur laquelle les prochaines opérations seront réalisées
    dotIndex = f.find(".") # stocke l'index où se trouve le caractère "."
    if f[:dotIndex] != "missing" and extension == findExtension: # on ignore uniquement le fichier "missing.png"
        print("Le fichier", f, "est une image à copier")
        nf = f[:2].upper()                                # formattage du nouveau nom de fichier
        src = targetDir + "/" + f                         # dossierOrigine/fichier à copier
        dst = targetDirBis + nf + "." + findExtension     # dossierDestitation/nouveauFichier
        shutil.copyfile(src,dst)                          # copie de la source vers la destination
        print("Copie et renommage réussis")               # la copie avec renommage a bien été réalisée
        print("Source :", src, "=> Destination :", dst)   # indication de la copie et du renommage effectués


