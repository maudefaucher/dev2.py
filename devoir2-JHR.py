# coding: utf-8 

import json
import csv
import requests

fichier = "lobbyistes.csv"
fichier = "lobbyistes-JHR.csv"

url = "http://jhroy.ca/uqam/lobby.json"
# print(url)

req = requests.get(url)
print(req)

if req.status_code !=200:
    print("Ça ne fonctionne pas.")

else: 
    lobb = req.json()
    # print(lobb)

    # n = 0 

    # print(len(lobb["registre"]))
    total = list(range(0,71998))
    # print(total)

    # print(lobb["registre"][0][0]["comlog_id"])
    # print(lobb["registre"][0][0]["fr_client_org_corp_nm"])
    # print(lobb["registre"][0][0]["en_client_org_corp_nm"])        
    # print(lobb["registre"][0][0]["client_org_corp_num"])
    # print(lobb["registre"][0][0]["date_comm"])
    # print(lobb["registre"][0][1][1]["objet"])
    # print(lobb["registre"][0][1][1]["objet_autre"])
    # print(lobb["registre"][0][2][0]["institution"])

    for un in lobb["registre"]:
        info=[]
        comlog=un[0]["comlog_id"]
        nomfr=un[0]["fr_client_org_corp_nm"]
        nomang=un[0]["en_client_org_corp_nm"]
        date=un[0]["date_comm"]
        objet=un[1][0]["objet"] ### SUPER SCRIPT! SEULEMENT, ICI, TU NE VAS CHERCHER QUE LES PREMIERS OBJETS. PARFOIS, IL Y EN A 2, 3, VOIRE 15! ET LE MOT "CLIMAT" PEUT S'Y RETROUVER...
        objetautre=un[1][0]["objet_autre"]
        institution=un[2][0]["institution"]

        info.append(comlog)
        info.append(nomfr)
        info.append(nomang)
        info.append(date)
        info.append(objet)
        info.append(objetautre)
        info.append(institution)

        # print(info)
        
        # if "objet" or "objetautre" != "limat":
        #     print("NON")

        # else: 
        #     print("OUI")
        
        # n=0
        # for bon in "registre":
        #     n+=1
        #     if "objet" or "objetautre" == "limat":
        #         print(n,[5],[6])

        # n=0
        # for limat in range(0,71998):
        #     n+=1
        #     if objet or objetautre == "limat":
        #         print(n,info)
         

        if "limat" in objet or "limat" in objetautre:
            print(comlog, nomfr, nomang, date, objet, objetautre, institution)
            lobby = open(fichier,"a")
            canada = csv.writer(lobby)
            canada.writerow(info)

# Ce devoir était vraiment très très dur ! Je suis bien heureuse de l'avoir fini ! :-) 

### TON SCRIPT FONCTIONNE... OU PRESQUE...
### MAIS COMMENT SE FAIT-IL QUE TON CSV NE CONTIENNE QUE 6 LIGNES?