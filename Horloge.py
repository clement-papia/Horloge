import time

# Initialisation de l'heure
heure = (0, 0, 0)
mode_affichage = "24h"
alarme = None
en_pause = False

def afficher_heure():
    global heure, mode_affichage
    heures, minutes, secondes = heure
    if mode_affichage == "12h":
        suffixe = "AM" if heures < 12 else "PM"
        heures = heures % 12
        if heures == 0:
            heures = 12
    else:
        suffixe = ""
    heures = str(heures).zfill(2)
    minutes = str(minutes).zfill(2)
    secondes = str(secondes).zfill(2)
    print(f"{heures}:{minutes}:{secondes} {suffixe}")

def regler_heure(nouvelle_heure):
    global heure
    heure = nouvelle_heure

def regler_alarme(nouvelle_alarme):
    global alarme
    alarme = nouvelle_alarme

def choisir_mode_affichage(nouveau_mode):
    global mode_affichage
    if nouveau_mode not in ["12h", "24h"]:
        raise ValueError("Mode d'affichage non valide")
    mode_affichage = nouveau_mode

def mettre_en_pause():
    global en_pause
    en_pause = True

def relancer():
    global en_pause
    en_pause = False

while True:
    if not en_pause:
        heure = (heure[0], heure[1], heure[2] + 1)
        if heure[2] == 60:
            heure = (heure[0], heure[1] + 1, 0)
        if heure[1] == 60:
            heure = (heure[0] + 1, 0, 0)
        if heure[0] == 24:
            heure = (0, 0, 0)
    afficher_heure()
    if alarme and heure == alarme:
        print("Alarme!")
    time.sleep(1)
