# Applications avec interface graphiques utilisant la bibliothèque Tkinter

## Importer le module

import tkinter

example 

>>>import tkinter as tk

ou

>>>from tkinter import *

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

boucle du programme

fen.mainloop()


## class d'objets

create_line(x1, y1, x2, y2)
create_rectangle(x1, y1, x2, y2)
create_arc(x1, y1, x2, y2)
create_oval(x1, y1, x2, y2)
create_polygon(x0, y0, x1, y1, x2, y2)

## methods .pack() et .pack_forget()

pack(side=, padx, pady)
pack_forget()

## .destroy() et .delete()

## tkinter.Canvas

tkinter.Canvas(master, bg = "couleur", width = largeur, height = hauteur)

## tkinter.Frame

tkinter.Frame(master, bg = "couleur")

## tkinter.Entry

tkinter.Entry(master)

## tkinter.Label et tkinter.Message

tkinter.Label(master)
tkinter.Message(master)

## .configure() .config()

permet de changet les propriétés d'un widget

## .get()

permet de récupérer une donnée dans le widget Entry

## .bind()

permet de lier à une touche un évènement, une fonction

entree.bind("<Return>", fonction)

# tkinter.Checkbutton

# tkinter.Listbox

# tkinter.Menu et tkinter.Menubutton

# tkinter.Radiobutton

# tkinter.Scale

# tkinter.Scrollbar

# tkinter.Text

# tkinter.Toplevel

# .grid()

utilisation d'une grille en ligne/colonne pour placer les objets dans la fenêtre

exemple :

>>> canva1.grid(row=1, column=1)
... canva2.grid(row=1, column=2)
... canva3.grid(row=2, column=1, columnspan=2) # s'étend au deuxième rang sur les deux colonnes

# .place()

# canvas itemconfig

permet de changer les propriété à un objet présent dans un canvas

exemple

>>> canva.intemconfig(text, text="hello")

# .coords()

permet de changer les propriété à d'un widget présent

>>> canva.coords(oval, x, y, x, y)