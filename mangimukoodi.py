import sys
import pygame
from music21 import instrument, note, chord, stream

def mangimukoodi(failinimi):
    fail = open(failinimi, "r+", encoding="UTF-8")
    ridadesisu = fail.readlines()
    koodipikkus = len(ridadesisu)
    nootidestream = stream.Stream() #stream on nootide list pmst.
    veerud = [] #meil oleks vaja see fail muuta veergudeks ja need veerud peaksid olema ka tühjadena. Vbl peaks leidma kõige pikema rea ja selle järgi tegema.
    max_pikkus = 0
    alampiir = 21 #MIDIS on 0-127 nooti, aga klaveri nootidest on 21 kuni 108
    # if koodipikkus < (128 + alampiir):                #Ma selle kommentin hetkel välja, homme tegelen sellega.
    #     for mitmesrida in range(koodipikkus):
    #         for rida in ridadesisu:
    #             ajutine_list = []
    #             for el in rida.split():
    #                 ajutine_list.append(el)
    #             veerud.append(list(ajutine_list))

        if koodipikkus > alampiir:
            koodipikkus -= 1
            akordid = chord.Chord()
            for veerusisu in veerud:
                for count, value in enumerate(veerusisu):
                    noot = note.Note(koodipikkus,quarterLength=len(reasisu[count]))
                    akordid.add(noot)
                nootidestream.append(akordid)
    pygame.init()
    uus_fail = failinimi.split("/")[-1].replace(".py", ".mid")
    nootidestream.write('midi', fp=uus_fail) #see salvestab faili
    pygame.mixer.music.load(uus_fail)
    pygame.mixer.music.play()

            
failinimi = input("Sisesta faili nimi, mida tahad kuulda: ")    
mangimukoodi(failinimi)