import sys
# import pygame
from music21 import instrument, note, chord, stream

def mangimukoodi(failinimi):
    fail = open(failinimi, "r+", encoding="UTF-8")
    failisisu = []
    stream1 = stream.Stream() #stream on nootide list pmst.
    reanr = 60 #alustan noodist A
    for rida in fail:
        reanr -= 1
        if reanr >= 0:
            failisisu = rida.split()
            for i in range(len(failisisu)):
                noot = note.Note(reanr)
                noot.duration.quarterLength = len(failisisu[i]) / 8
                stream1.append(noot)
    # pygame.init()
    stream1.write('midi', fp=failinimi.split("/")[-1].replace(".py", ".mid")) #see salvestab faili 
    # pygame.mixer.music.load(fail)
    # pygame.mixer.music.play() #see miskiprst ei toimi hetkel

# pygame.init()
# pygame.mixer.music.load()  # failinimi
# pygame.mixer.music.play()
            
failinimi = input("Sisesta faili nimi, mida tahad kuulda: ")    
mangimukoodi(failinimi)