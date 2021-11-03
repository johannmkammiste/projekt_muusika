import sys
import pygame
import numpy as np
from music21 import instrument, note, chord, stream

def pikimrida(failinimi):
    pikkus = 0
    failisisu = open(failinimi, "r+", encoding="UTF-8")
    for rida in failisisu:
        if len(rida) > pikkus:
            pikkus = len(rida)
    return pikkus

def mangimukoodi(failinimi):
    fail = open(failinimi, "r+", encoding="UTF-8")
    failisisu= fail.readlines()
    pikimpikkus = pikimrida(failinimi)
    failipikkus = len(failisisu)
    noodistikupikkus = 0
    if pikimpikkus > failipikkus:
        noodistikupikkus = pikimpikkus
    elif pikimpikkus <= failipikkus:
        noodistikupikkus = failipikkus
    nootidestream = stream.Stream() #stream on nootide list pmst.
    akordid = chord.Chord()
    akordidemaatriks = np.array([], ndmin=noodistikupikkus)
    alampiir = 21 #MIDIS on 0-127 nooti, aga klaveri nootidest on 21 kuni 108
    for rida in failisisu:
        realemendid = []
        reaelemendid = rida.split()
        if len(reaelemendid) < pikimpikkus:
            pikkusevahe = pikimpikkus - len(reaelemendid)
            for i in range(pikkusevahe):
                reaelemendid.append("^0^")
            np.r_[akordidemaatriks,[reaelemendid]]

    print(akordidemaatriks)
 
failinimi = input("Sisesta faili nimi, mida tahad kuulda: ")    
mangimukoodi(failinimi)