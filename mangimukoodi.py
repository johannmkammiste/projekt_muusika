import sys
import pygame
from music21 import instrument, note, chord, stream
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from functools import partial
nootidestream = stream.Stream()

def openfile(entryBox):
    filename = filedialog.askopenfilename()
    entryBox.delete(0, tk.END)
    entryBox.insert(tk.END, filename)

def kirjutafail(failinimi, nootidestream):
    uus_fail = failinimi.split("/")[-1].replace(".py", ".mid")
    nootidestream.write('midi', fp=uus_fail)
    return uus_fail

def mangimukoodi():
    failinimi = kirjuta_failinimi.get()
    with open(failinimi, "r+", encoding="UTF-8") as f:
        failisisu = f.readlines()
    rea_noodid = []
    akord = []
    reanr = 108
    alampiir = 21  # MIDIS on 0-127 nooti, aga klaveri nootidest on 21 kuni 108
    akordid = chord.Chord()
    for line in failisisu:
        puhas = line.strip("\n").split()
        akordinoodid = []
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
    if tk.messagebox.askyesno("Kuulda?", "Kood konverteeritud! Kas soovid ka seda kuulda?") == True:
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode ((600,375),0,32)
        pygame.mixer.music.load(uus_faili_nimi)
        pygame.mixer.music.play()
    
#GUI
root= tk.Tk()
root.title("Mängi mu koodi!")
root.geometry("500x200")
kirjuta_failinimi = tk.Entry(root, text="Failinimi", font=('Arial', 20))
kirjuta_failinimi.grid(row=1)
vali_fail_nupp = ttk.Button(root, text="Vali fail", command=partial(openfile, kirjuta_failinimi))
vali_fail_nupp.grid(row=0, sticky=tk.W, pady=4)
mangi_koodi = ttk.Button(root, text='Mängi mu koodi!', command=mangimukoodi)
mangi_koodi.grid(row=2, sticky=tk.W, pady=4)

root.mainloop()