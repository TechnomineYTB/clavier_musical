import os
import pygame
from evdev import InputDevice, categorize, ecodes

# AUDIO
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["AUDIODEV"] = "hw:0,0"
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
print("Audio OK :", pygame.mixer.get_init())

# SONS
sons = {
    "a": pygame.mixer.Sound("1.WAV"),
}

print("Sons chargés :", list(sons.keys()))

# DETECTION CLAVIER
def trouver_clavier():
    from evdev import list_devices
    for path in list_devices():
        dev = InputDevice(path)
        name = dev.name.lower()

        if (
            "keyboard" in name or
            "Logitech" in name or
            "usb" in name or
            "hid" in name or
            "key" in name
        ):
            return dev

    raise RuntimeError("Aucun clavier trouvé !")

clavier = trouver_clavier()
print("Clavier détecté :", clavier)

# BOUCLE PRINCIPALE
print("Prêt ! Appuie sur A")

for event in clavier.read_loop():
    if event.type == ecodes.EV_KEY:
        data = categorize(event)

        if data.keystate == 1:
            touche = data.keycode.lower()

            if isinstance(touche, list):
                touche = touche[0]

            touche = touche.replace("key_", "")

            if touche in sons:
                print("=>", touche)
                sons[touche].play()
