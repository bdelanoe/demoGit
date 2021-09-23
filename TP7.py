'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

# Votre code ici
import csv # module csv built-in (natif)

filmYearIndex = 0  # n° colonne de l'année des films
filmRateIndex = 1  # n° colonne des notes des films
filmNameIndex = 2  # n° colonne des noms de films
bestFilmRate  = 0  # note du meilleur film
bestFilmName  = "" # nom du meileur film
bestFilmYear  = 0  # année du meilleur film
numMatching   = 0  # compteur du nombre de films correspondant aux critères de recherche

with open("deniro.csv", "r") as csvFile:
    rows = csv.reader(csvFile, delimiter = ",")
    for r in rows:
        if r[filmYearIndex] != 'Year': # On ignore la première ligne (l'entête des colonnes)
            filmYear = int(r[filmYearIndex])
            filmRate = int(r[filmRateIndex].strip().strip())
            filmName = r[filmNameIndex].strip().strip('"')

            if filmRate >= bestFilmRate:
                bestFilmRate = filmRate
                bestFilmName = filmName
                bestFilmYear = filmYear

            if filmYear >= 2000 and filmYear <= 2010:
                numMatching += 1

# Preview de ce qui va être enregistré dans le fichier de sortie
print("Nombre de films entre 2000 et 2010 : %d" % numMatching)
print("Le meilleur film est '%s' de %d avec une note de %d" % (bestFilmName,bestFilmYear,bestFilmRate))

fileSortie = open("deniro-report.txt", "w")
fileSortie.writelines(
    [
        "Nombre de films entre 2000 et 2010 : ",
        str(numMatching),
        "\nLe meilleur film est '",
        bestFilmName,
        "' de ",
        str(bestFilmYear),
        " avec une note de ",
        str(bestFilmRate)
    ]
)
fileSortie.close()


