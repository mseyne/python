# -*- coding:Utf-8 -*-

import tkinter as tk

fenetre = tk.Tk()

text = tk.Label(fenetre, text="Hello", fg="Red")
text.pack()
bou = tk.Button(fenetre, text="Ok", command=fenetre.destroy)
bou.pack()
fenetre.mainloop()


# def question(annonce, essais = 4, please = 'Oui ou Non, svp'):
# 	while essais > 0:
# 		reponse = input(annonce).lower()
# 		if reponse in ("o", "oui"):
# 			return 1
# 		if reponse in ("n", "non"):
# 			return 0
# 		print(please)
# 		essais +- 1

# question("Est-ce que tu veux des haricots ?")
# question("Est-ce que tu veux aller sur Mars ?")