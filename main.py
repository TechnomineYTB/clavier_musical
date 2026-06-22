import os
import pygame
from evdev import InputDevice, categorize, ecodes

# ---------------------------------------------------------
# CONFIGURATION AUDIO (ALSA)
# ---------------------------------------------------------
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["AUDIODEV"] = "hw:0,0"   # Jack = hw:0,0 / HDMI = hw:1,0

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)

print("Audio OK :", pygame.mixer.get_init())


# ---------------------------------------------------------
# CHARGEMENT DES SONS
# ---------------------------------------------------------
sons = {
    "a": pygame.mixer.Sound("sons/do.wav"),
    "z": pygame.mixer.Sound("sons/re.wav"),
    "e": pygame.mixer.Sound("sons/mi.wav"),
    "r": pygame.mixer.Sound("sons/fa.wav"),
    "t": pygame.mixer.Sound("sons/sol.wav"),
    "y": pygame.mixer.Sound("sons/la.wav"),
    "u": pygame.mixer.Sound("sons/si.wav"),
}

print("Sons chargés :", list(sons.keys()))


# ---------------------------------------------------------
# DÉTECTION DU CLAVIER
# ---------------------------------------------------------
# Trouve automatiquement le clavier
def trouver_clavier():
    from evdev import list_devices
    for path in list_devices():
        dev = InputDevice(path)
        if "Keyboard" in dev.name or "kbd" in dev.name.lower():
            return dev
    raise RuntimeError("Aucun clavier trouvé !")

clavier = trouver_clavier()
print("Clavier détecté :", clavier)


# ---------------------------------------------------------
# BOUCLE PRINCIPALE
# ---------------------------------------------------------
print("Prêt ! Appuie sur les touches A Z E R T Y U…")

for event in clavier.read_loop():
    if event.type == ecodes.EV_KEY:
        data = categorize(event)

        if data.keystate == 1:  # 1 = key down
            touche = data.keycode.lower()

            # Certaines touches ont un nom en liste : ['KEY_A']
            if isinstance(touche, list):
                touche = touche[0]

            touche = touche.replace("key_", "")

            if touche in sons:
                print("→", touche)
                sons[touche].play()
