from evdev import InputDevice, categorize, ecodes
import pygame

pygame.mixer.init()

sons = {
    ecodes.KEY_A: pygame.mixer.Sound("1.mp3"),

}

touches_actives = {k: False for k in sons}

# Trouver le clavier automatiquement
import glob
claviers = glob.glob("/dev/input/event*")
device = None

for path in claviers:
    dev = InputDevice(path)
    if "keyboard" in dev.name.lower() or "kbd" in dev.name.lower():
        device = dev
        break

if device is None:
    print("Aucun clavier trouvé dans /dev/input/")
    exit()

print(f"Utilisation du clavier : {device.path}")
print("Maintiens A Z E R pour jouer. Relâche pour arrêter. Ctrl+C pour quitter.")

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        code = key_event.scancode

        if code in sons:
            if key_event.keystate == key_event.key_down:
                if not touches_actives[code]:
                    sons[code].play(loops=-1)
                    touches_actives[code] = True

            elif key_event.keystate == key_event.key_up:
                if touches_actives[code]:
                    sons[code].stop()
                    touches_actives[code] = False
