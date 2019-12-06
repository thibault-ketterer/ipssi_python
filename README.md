# 2019-12-06
## joyeuses greves
procédure de rendu:
faites un répertoires exam3 dans le git que vous aviez utilisez pour l'exam2
mettez vos fichiers dans le répertoire exam3, soit
```
exam3/tree.py
exam3/clean_downloads.py
exam3/noel.py
exam3/sla.py
exam3/test_tree.py
exam3/test_noel.py
exam3/test_sla.py
exam3/nginx.yml
exam3/sapin_noel.py
exam3/valide_clean.py ou exam3/valide_clean.sh
```
si vous souhaitez changer de git pour faire votre rendu. indiquez le moi par slack en message privé avant vendredi soir.

## sapin
faites un script `tree.py`
qui prend en argument un nombre et affiche un sapin comme celui-ci
* l'argument est la largeur du sapin mais doit etre impaire et arrondi au-dessus
* le tronc fait une largeur de 1 si la largeur est <= 3
* le tronc fait une largeur de 3 si la largeur du sapin est > 3
* la hauteur du tain le tronc fait la largeur du sapin divisé par 5 arrondi en dessous mais de minimum 1

attention ce script devra contenir ce code pour gérer l'argument
```
if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
```
le code de "dessin" sera donc dans un fonciton nommé "show_tree"

```
#tketterer@MLA019902 ~ _$ python tree.py 1
 x
 x
#tketterer@MLA019902 ~ _$ python tree.py 2
  x
 xxx
  x
#tketterer@MLA019902 ~ _$ python tree.py 3
  x
 xxx
  x
#tketterer@MLA019902 ~ _$ python tree.py 4
   x
  xxx
 xxxxx
  xxx
#tketterer@MLA019902 ~ _$ python tree.py 5
   x
  xxx
 xxxxx
  xxx
  xxx
#tketterer@MLA019902 ~ _$ python tree.py 10
      x
     xxx
    xxxxx
   xxxxxxx
  xxxxxxxxx
 xxxxxxxxxxx
     xxx
     xxx
     xxx
#tketterer@MLA019902 ~ _$ python tree.py 30
                x
               xxx
              xxxxx
             xxxxxxx
            xxxxxxxxx
           xxxxxxxxxxx
          xxxxxxxxxxxxx
         xxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxx
       xxxxxxxxxxxxxxxxxxx
      xxxxxxxxxxxxxxxxxxxxx
     xxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxx
  xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx
```

## organise mes donwloads
faites un script python `clean_downloads.py` qui va vous proposer de supprimer vos fichiers téléchargés:
le script devra vous proposer de supprimer les fichiers dans le répertoire Downloads de votre machine ( ~/Downloads sous mac et Linux, /mnt/c/Users/votreuser/Downloads sous WSL )
* le nom du répertoire de download sera pris en argument du script

pour cela il va

vous proposer de supprimer les fichiers
* plus vieux que 10 jours
* qui font plus de 50 MB

vous proposer de ranger les autres fichiers dans un répergtoire portant le nom du mois de telechargement comme suit
2019-11
2019-10

* le script ne doit pas planter si le répertoire est vide
* le script ne doit pas planter si le répertoire ne contient pas de vieux fichiers
* le script ne doit pas planter si le répertoire ne contient pas de fichiers plus grand que 50MB

exemple d'utilisation, ou l'on appuie sur "y" pour valider la suppression
```
sous mac
$ clean_downloads.py ~/Downloads

sous windows
$ clean_downloads.py /mnt/c/Users/Robert/Downloads

cleanup old files: (more than 10 days + 50MB)
toto.zip
truc.zip
[yes/No]? y
deleting toto.zip
deleting truc.zip
organizing other files:
moving into 2019-10: old_download.txt
moving into 2019-10: other_download.txt
moving into 2019-11: fichier.txt
end
```

note pour générer de vieux fichiers vous pouvez utilisez touch `man touch` ou la doc ici
http://www.octetmalin.net/linux/tutoriels/touch-modifier-changer-heure-date-horodatage-fichier-files-dossier-folders-repertoire.php

## noel
`noel.py`
utilisez le module calendar et datetime en python pour afficher
* le nombre de jour avant noel
* un calendrier de tous les mois entre la date courante et le prochain noel
* le calendrier devra entourer la date du jour avec () et la date de noel avec []
* le script affichera un sapin de taille 10 si on est le jour de noel
* pour faciliter son test le script prendra en argument OPTIONNEL une date
* si aucun argument n'est passé sur la ligne de commande le script prendra la date du jour
* attention a mettre le bon nombre d'espace dans l'affichage comme l'exemple

attention ce script devra contenir ce code pour gérer l'argument
```
if __name__ == "__main__":
    print(show_noel(sys.argv))
```
exemple
```
$ ./noel.py 2019-11-15
40 days before christmas

          November 2019
Mon  Tue  Wed  Thu  Fri  Sat  Sun
                      1    2    3
  4    5    6    7    8    9   10
 11   12   13   14  (15)  16   17
 18   19   20   21   22   23   24
 25   26   27   28   29   30

          December 2019
Mon  Tue  Wed  Thu  Fri  Sat  Sun
                                1
  2    3    4    5    6    7    8
  9   10   11   12   13   14   15
 16   17   18   19   20   21   22
 23   24  [25]  26   27   28   29
 30   31

$ ./noel.py 2019-12-25
        x
       xxx
      xxxxx
     xxxxxxx
    xxxxxxxxx
   xxxxxxxxxxx
  xxxxxxxxxxxxx
 xxxxxxxxxxxxxxx
       xxx
       xxx
       xxx
       xxx

```

## sla
faites un script `sla.py` qui calcule le temps en heure et minute d'indisponibilité pour un certain pourcentage de sla sur une année.

Vous pouvez vous baser sur ce site pour valider votre script
https://uptime.is/

Exemple
```
$ sla.py 99.9
8h 45m 57.0s
```

le script devra contenir ce code
```
if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))
```

## tests python
faites des scripts de tests python, utilisant la nomenclature unittest

qui permettent
* de tester votre code de sapin
vous le nommerez `test_tree.py` via la fonction show_tree

il devra valider que le sapin fonctionne avec une taille de 1, 2, 5 et 30

* de tester votre code de noel
vous le nommerez `test_noel.py` via la fonction show_noel

il devra valider que noel fonctionne avec les dates 2018-8-18 et 2020-11-1

* de tester votre code de sla
vous le nommerez `test_sla.py` via la fonction show_sla

il devra tester la sla 99.5, 99.8 et 99.99

une fois que vous lancer `pytest -v` dans votre répertoire exam3 il doit vous indiquer que tout est bon comme vu en cours


## ansible nginx
faites un role ansible
* que vous appelerez `nginx.yml`
* qui installe le package nginx
* qui copie un fichier de config nginx valide de votre choix dans /etc/nginx.conf
* le fichier nginx devra contenir la ligne "add_header X-myname le-nom-de-la-machine" dans le bloc `http {`
* qui verifie que la config nginx est correcte
* qui reload le demon nginx (cf nginx -h)

* ansible remplacera bien sur le-nom-de-la-machine par la valeur de ansible_hostname

## sapin de noel
faites une copie de votre sapin et modifiez le pour qu'il affiche aussi des boules de noel au hasard (fonction random)
* il affiche un nombre de boules au hasard
* les boules sont réparties au hasard sur les branches
* si on lance 2 fois le script de suite les boules vont donc changer de place

comme ceci par exemple `sapin_noel.py`:

```
#tketterer@MLA019902 ~ _$ python sapin_noel.py 30
                x
               xxx
              xxxxx
             xxxOxxx
            xxxxxOxxx
           xxxxxxxxxxx
          xxxxxxOxxxxxx
         xxOxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxx
       xxxxxxxxOxxxxxxxOxx
      xxxOxxxxxxxxOxxxxxxxx
     xxxxxxxxxxxxxxxxxxxOxxx
    xxxxxxxxxxOxxxxxxxxxxxxxx
   xxxxOxxxxxxxxxxxxxxxxxxxxxx
  xxxxxxxxxxxxxOxxxxxxxxxxxxxxx
 xxxxOxxxxxxxOxxxxxxxxOxxxxxOxxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx


#tketterer@MLA019902 ~ _$ python sapin_noel.py 30
                O
               xxx
              xOxxx
             xxxxxxx
            xxxxxxxxx
           xxxxOxxxxxx
          xxxxxxxxxxOxx
         xxxxxOxxxxxxxxx
        xxxxxxxxxxxxxxxxx
       xxxxxxxxOxxxxxxxxxx
      xxxxxxOxxxxxxxxOxxxxx
     xxxxOxxxxxxxxxxxxxxxxxx
    xxxOxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxx
  xxOxxxxxxxxxxOxxxxxxxxxxOxxxx
 xxOxxxxxxxxxxxxxxxxxxxxxxxxxxxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx
               xxx
```

## bonus
Faites un script de test pour le script clean_downloads.py dans le language de votre choix.

Vous le nommerez `valide_clean.py` ou `valide_clean.sh` selon votre choix de language.

S'il fonctionne vous aurez 18 directement (meme si le reste n'est pas fait ou invalide, cependant c'est l'exercice le plus difficile)

il doit gérer tous les cas
- créer de vieux fichiers
- des fichiers > 50MB
- des fichiers < 50MB
- lancer le script clean_downloads.py et entrer "y" au clavier pour la suppression
- vérifier que les fichiers ont été supprimés ou déplacés
