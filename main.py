import pygame
import keyboard
import time

pygame.mixer.init()

# Charger les sons (bouclés pour pouvoir les arrêter)
sons = {
    "a": pygame.mixer.Sound("1.mp3"),

}

# Pour savoir quelles touches sont actuellement actives
touches_actives = {t: False for t in sons}

print("Clavier musical (ligne de commande)")
print("Maintiens A Z E R pour jouer. Relâche pour arrêter. ESC pour quitter.")

try:
    while True:
        # Vérifier chaque touche
        for touche, son in sons.items():
            if keyboard.is_pressed(touche):
                if not touches_actives[touche]:
                    son.play(loops=-1)  # jouer en boucle
                    touches_actives[touche] = True
            else:
                if touches_actives[touche]:
                    son.stop()
                    touches_actives[touche] = False

        if keyboard.is_pressed("esc"):
            break

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

print("Fermeture…")
