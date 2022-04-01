import pandas as pd 
from datetime import datetime, timedelta
import sys
if len(sys.argv) != 2 :
    print("Pas le bon nombre d'arguments")
    exit(1)
episode = sys.argv[1]
saison = 2
#episode = input("Num. Ep : ")
#saison = input("Num. Saison : ") 
debut = input("Timestamp Deb : ")
fin = input("Timestam Fin : ")

utile=input("Utile ? : ")

debut = timedelta(hours=0, minutes=int(debut.split(".")[0]), seconds = int(debut.split(".")[1])) 
fin = timedelta(hours=0, minutes=int(fin.split(".")[0]), seconds = int(fin.split(".")[1])) 

duree = fin - debut

with open("caveman.txt", "a") as fp:
    fp.write(f"{episode}:{saison}:{duree.total_seconds()}:{utile}\n")
        

