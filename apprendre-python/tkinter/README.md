# Applications graphiques avec Tkinter

## Importer le module

import tkinter
from tkinter import *

example 

>>>import tkinter as tk

## Instanciation de la classe fenêtre Tk()

>>> fen = tk.Tk()

## widget Label(maitre, text, fg(foreground))

>>> text = tk.Label(fen, text='Bonjour', fg="blue")


## méthode .pack()

crée un block autou du widget avant de le placer dans la fenêtre "maitre"

>>>text.pack()

## widget Button(maitre, text, command)

>>> bou = Button(fen, text='Quitter', command= fen.destroy)

la méthode destroy s'applique à fen seulement si le bouton est cliqué

penser à utiliser la méthode pack() sur le nouveau widget créé

bou.pack()

## méthode .mainloop()

fen.mainloop()