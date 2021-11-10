import sys
import pygame
from music21 import instrument, note, chord, stream

failinimi = input("Sisesta faili nimi, mida tahad kuulda: ")
nootidestream = stream.Stream()

def mangimukoodi(failinimi):
    fail = open(failinimi, "r+", encoding="UTF-8")
    failisisu = fail.readlines()
    rea_noodid = []
    akord = []
    rida = 1
    reanr = 80
    akordid = chord.Chord()
    for line in failisisu:
        puhas = line.strip("\n")
        rida += 1
        for el in puhas:
            if el == " ":
                el_noot = note.Rest()
                rea_noodid.append(el_noot)
            else:
                el_noot = note.Note(reanr - rida)
                rea_noodid.append(el_noot)
    nootidestream.append(rea_noodid)
    #for line in failisisu:
     #   puhas = line.strip()
      #  sõnad_reas = puhas.split(" ")
       # noodid_reas = len(sõnad_reas)
        #def indentation(puhas):
         #   taanded = puhas.count("  ")
          #  return taanded
        #print(indentation(puhas))
        #for el in sõnad_reas:
         #   noodi_pikkus = len(el)
          #  elemendi_noot = note.Note(reanr, quarterLength=noodi_pikkus/4)
           # rea_noodid.append(elemendi_noot)
            #akordid = chord.Chord()
            #akordid.add(elemendi_noot)
        #nootidestream.append(akordid)
        #reanr -= 1
    max_pikkus = 0
    alampiir = 21  # MIDIS on 0-127 nooti, aga klaveri nootidest on 21 kuni 108
    # if koodipikkus < (128 + alampiir):

mangimukoodi(failinimi)
pygame.init()
uus_fail = failinimi.split("/")[-1].replace(".py", ".mid")
nootidestream.write('midi', fp=uus_fail)  # see salvestab faili
pygame.mixer.music.load(uus_fail)
pygame.mixer.music.play()

