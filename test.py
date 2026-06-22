import os

# --- CONFIGURATION ALSA / SDL ---
# Force SDL à utiliser ALSA
os.environ["SDL_AUDIODRIVER"] = "alsa"

# Force ALSA à utiliser la carte 0, device 0 (jack du Raspberry Pi)
# Si tu utilises HDMI, remplace par "hw:1,0"
os.environ["AUDIODEV"] = "hw:0,0"

# --- INITIALISATION PYGAME ---
import pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)

# --- DEBUG ---
print("SDL_AUDIODRIVER =", os.getenv("SDL_AUDIODRIVER"))
print("AUDIODEV =", os.getenv("AUDIODEV"))
print("pygame mixer init =", pygame.mixer.get_init())

# --- TEST AUDIO ---
son = pygame.mixer.Sound("1.WAV")   # mets ton fichier ici
son.play()

input("Appuie sur Entrée pour quitter")
