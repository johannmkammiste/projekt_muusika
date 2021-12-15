import sys
import pygame
import random
from music21 import note, stream
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from functools import partial
nootidestream = stream.Stream()

def openfile(entryBox): #ava sisestatud fail
    filename = filedialog.askopenfilename()
    entryBox.delete(0, tk.END)
    entryBox.insert(tk.END, filename)

def kirjutafail(failinimi, nootidestream):
    uus_fail = failinimi.split("/")[-1].replace(".py", ".mid")
    nootidestream.write('midi', fp=uus_fail)
    return uus_fail

def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

def playfail(failinimi):
    if tk.messagebox.askyesno("Kuulda?", "Kood konverteeritud! Kas soovid ka seda kuulda?") == True:
        #Music player
        music_player = tk.Tk()
        music_player.title("Music Player")
        music_player.geometry("450x200")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(failinimi)
        pygame.mixer.music.play()
        play_nupp = tk.Button(music_player, width=4, height=2, text="PLAY", command=play, bg="blue", fg="white")
        stop_nupp = tk.Button(music_player, width=4, height=2, text="STOP", command=stop, bg="red", fg="white")
        pause_nupp = tk.Button(music_player, width=4, height=2, text="PAUSE", command=pause, bg="orange", fg="white")
        unpause_nupp = tk.Button(music_player, width=4, height=2, text="UNPAUSE", command=unpause, bg="orange", fg="white")
        play_nupp.pack(fill="x")
        stop_nupp.pack(fill="x")
        pause_nupp.pack(fill="x")
        unpause_nupp.pack(fill="x")
        music_player.mainloop()

#Random versiooni jaoks vajalikud osad
elemendid = "AaBbCcDdeEfFgGhHiIjJkKlLmMnNoOpPqQrRsSšŠzZžŽtTuUvVWwõÕäÄöÖüÜx\"XyY<>*,._#¤%&/?!-;:^'1234567890´=`\{}()[]€+$£@ˇ~ ½"
lst = list(elemendid)
pikkus = len(lst)

def mangimukoodirandom():
    failinimi = kirjuta_failinimi.get()
    with open(failinimi, "r+", encoding="UTF-8") as fail:
        for rida in fail:
            puhas = rida.strip()
            failisisu = puhas.split(" ")
            for el in failisisu:
                for i in el:
                    kus = random.randrange(0, pikkus)
                    noot = note.Note(kus)
                    noot.duration.quarterLength = 1 / 8
                    nootidestream.append(noot)
    uus_faili_nimi = kirjutafail(failinimi, nootidestream)
    playfail(uus_faili_nimi)

#Põhiprogramm
def mangimukoodi():
    failinimi = kirjuta_failinimi.get()
    with open(failinimi, "r+", encoding="UTF-8") as f:
        failisisu = f.readlines()
    rea_noodid = []
    reanr = 108
    alampiir = 21  # MIDIS on 0-127 nooti, aga klaveri nootidest on 21 kuni 108
    for line in failisisu:
        if reanr < alampiir:
            reanr = 108
        puhas = line.strip("\n").split(" ")
        if reanr < alampiir:
            reanr = 108
        for el in puhas:
            pausinoot = note.Rest(quarterLength=1/8)
            noodid = note.Note(reanr, quarterLength=len(el)/4)
            rea_noodid.append(noodid)
            rea_noodid.append(pausinoot)
        reanr -= 1
    nootidestream.append(rea_noodid)
    uus_faili_nimi = kirjutafail(failinimi, nootidestream)
    playfail(uus_faili_nimi)

#GUI
root = tk.Tk()
root.title("Mängi mu koodi!")
root.geometry("500x200")
kirjuta_failinimi = tk.Entry(root, text="Failinimi", font=('Arial', 20))
kirjuta_failinimi.grid(row=1)
vali_fail_nupp = ttk.Button(root, text="Vali fail", command=partial(openfile, kirjuta_failinimi))
vali_fail_nupp.grid(row=0, sticky=tk.W, pady=4)
mangi_koodi = ttk.Button(root, text='Mängi mu koodi!', command=mangimukoodi)
mangi_koodi_random = ttk.Button(root, text='Mängi mu koodi (suvakalt)!', command=mangimukoodirandom)
mangi_koodi.grid(row=2, sticky=tk.W, pady=4)
mangi_koodi_random.grid(row=2, sticky=tk.E, pady=4)

root.mainloop()