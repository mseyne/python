# -*- coding:Utf-8 -*-


#Variables
ACCEPTÉS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

          
#Fonctions
def menu():
    print('Bonjour dans le convertisseur km/mile')
    print("(1) Convertir mile par heure en km/h et mètres/s")
    print("(2) Convertir kilomètres par heure en mile/h et m/s")
    print("(3) Convertir mètres par seconde en km/h et mile/h")
    answer = input(">>>")
    while answer not in ACCEPTÉS[1:4]:
        print('Vous avez le choix entre "1", "2" ou "3".')
        answer = input(">>>")
    conversion(answer)

def conversion(choix):
    print(choix)
    if choix == "1":
        kmh = input("Combien de kilomètre heure souhaitez vous convertir ?")    
        if vérification(kmh) == True:
            kmh = int(kmh)
            mh = round(kmh / 1.609, 2)
            ms = round(kmh / 3.6, 2)
            print(kmh, "kilomètres par heures correspond à", mh, "miles par heures et",
                  ms, "mètres par secondes.")
            
    elif choix == "2":
        mh = input("Combien de mile par heure souhaitez vous convertir ?")
        if vérification(mh) == True:
            mh = int(mh)
            kmh = round(mh * 1.609, 2)
            ms = round(kmh / 3.6, 2)
            print(mh, "mile à l'heure correpond à", kmh, "kilomètres par heures soit",
                  ms, "mètres par secondes.")
        
    elif choix == "3":
        ms = input("Combien de mètres par secondes souhaitez vous convertir ?")
        if vérification(ms) == True:
            ms = int(ms)
            kmh = round(ms * 3.6, 2)
            mh = round(kmh / 1.609, 2)
            print(ms, "mètres par secondes correpond à", kmh, "kilomètres par heures et",
                  mh, "miles par heures.")
    else:
        print("bug")

def vérification(data):
    for i in str(data):
        if i not in ACCEPTÉS:
            print("Ce n'est pas un nombre.")
            return False
    return 1

#Démarrage programme
menu()
