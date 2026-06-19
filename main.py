from pynput import keyboard
import pygame

pygame.mixer.init()

sons = {
    "a": pygame.mixer.Sound("sons/do.wav"),
    "z": pygame.mixer.Sound("sons/re.wav"),
    "e": pygame.mixer.Sound("sons/mi.wav"),
    "r": pygame.mixer.Sound("sons/fa.wav")
}

touches_actives = {t: False for t in sons}

def on_press(key):
    try:
        k = key.char
        if k in sons and not touches_actives[k]:
            sons[k].play(loops=-1)
            touches_actives[k] = True
    except:
        pass

def on_release(key):
    try:
        k = key.char
        if k in sons and touches_actives[k]:
            sons[k].stop()
            touches_actives[k] = False
    except:
        pass

    if key == keyboard.Key.esc:
        return False

print("Maintiens A Z E R pour jouer. Relâche pour arrêter. ESC pour quitter.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
