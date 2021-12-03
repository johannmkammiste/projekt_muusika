import sys
import random
from music21 import instrument, note, chord, stream

elemendid = "AaBbCcDdeEfFgGhHiIjJkKlLmMnNoOpPqQrRsSšŠzZžŽtTuUvVWwõÕäÄöÖüÜx\"XyY<>*,._#¤%&/?!-;:^'1234567890´=`\{}()[]€+$£@ˇ~ ½"
lst = list(elemendid)
pikkus = len(lst)

def mangimukoodi(failinimi):
    fail = open(failinimi, "r+", encoding="UTF-8")
    stream1 = stream.Stream() 
    for rida in fail:
        puhas = rida.strip()
        failisisu = puhas.split(" ")
        for el in failisisu:
            for i in el:
                kus = random.randrange(0, pikkus)
                noot = note.Note(kus)
                noot.duration.quarterLength = 1 / 8
                stream1.append(noot)
    stream1.write('midi', fp=failinimi.split("/")[-1].replace(".py", ".mid")) #see salvestab faili 
            
failinimi = input("Sisesta faili nimi, mida tahad kuulda: ")    
mangimukoodi(failinimi)