from time import sleep
import serial
import pygame.mixer

# Chemin du fichier audio (mets le bon chemin)
AUDIO_FILE_KICK = "kick.mp3"
AUDIO_FILE_SNARE = "snare.mp3"
AUDIO_FILE_HAT = "hat.mp3"

# Configuration du port série (remplace COM3 par le bon port)
ser = serial.Serial("COM8", 115200, timeout=.1)

print("Initialisation du module gyro+accel...")
ser.write(bytes('\n', "utf-8"))

print("Calibration... ! Garder le capteur immobile !")
sleep(10)
print("Calibration terminée.")

pygame.mixer.init(channels=3)
print("✅ Attente du signal sur le port série...")

while True:
    line = ser.readline().decode("utf-8").strip()
    if line == "1":  # Si on reçoit "1", on joue le son
        print("🔊 Signal reçu ! Lecture du son kick...")
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(AUDIO_FILE_KICK))
        
    if line == "2":  # Si on reçoit "1", on joue le son
        print("🔊On a reçu un 2!!!")
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(AUDIO_FILE_SNARE))
        
    if line == "3":  # Si on reçoit "1", on joue le son
        print("🔊On a reçu un 3!!!")
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(AUDIO_FILE_HAT))
    
    #print("On a reçu : " + line)