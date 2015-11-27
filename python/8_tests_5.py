from tkinter import *

fen1 = Tk()

#widgets non référencés dans des variables
Label(fen1, text = "Premier champ :").grid(row = 1, sticky = 'e')
Label(fen1, text = 'Second :').grid(row = 2, sticky = 'e')
Label(fen1, text = 'Troisième :').grid(row = 3, sticky = 'e')


entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)
entr1.grid(row = 1, column = 1)
entr2.grid(row = 2, column = 1)
entr3.grid(row = 3, column = 1)

chek1 = Checkbutton(fen1, text="Case à cocher, pour voir")
chek1.grid(columnspan = 2)

#création du canvas avec l'image
can1 = Canvas(fen1, width = 160, height = 160, bg = "white")
photo = PhotoImage(file = 'bird.gif')
item = can1.create_image(80, 80, image = photo)
can1.grid(row = 1, column = 2, rowspan = 3, padx = 10, pady = 5)

fen1.mainloop()