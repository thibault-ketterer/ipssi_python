#!/usr/bin/python3
import os
list_files = os.listdir("/tmp")
# list_files = os.listdir(".") # repertoire courant
# print(list_files)
print(type(list_files))
print(list_files[0])
print(list_files[1])
print(list_files[2])
# trouver la taille des fichiers
list_files[2]
# avec os.stat trouver la taille
# os.stat(list_files[2]) #ne fonctionne pas car il manque le chemin
os.stat("/tmp/" + list_files[2]) # fonctionne ok
print("toutes les informations du fichier: ", os.stat("/tmp/" + list_files[2]))
print("id du owner du fichier: ", os.stat("/tmp/" + list_files[2]).st_uid)
print("taille      du fichier: ", os.stat("/tmp/" + list_files[2]).st_size)
from pwd import getpwuid
print("txt  owner  du fichier:", getpwuid(os.stat("/tmp/" + list_files[2]).st_uid).pw_name)
