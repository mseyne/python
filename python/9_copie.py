def createFile(name, text1, text2):
	"crée un nouveau fichier nommé name contenant text1 et text2"
	f = open(name, "w")
	f.write(text1)
	f.write(text2)
	f.close()

def copieFichier(source, destination):
	"copie intégrale d'un fichier"
	fs = open(source, 'r')
	fd = open(destination, 'w')
	while 1:
		txt = fs.read(20)
		if txt == "":
			break
		fd.write(txt)
	fs.close()
	fd.close()
	return

def readFiles(file):
	"read and print a file"
	fr = open(file, 'r')
	print(fr.read())


createFile("MonFichier", "Je suis présent et tu es mort.\n","La vérité, je la cherches,\nJe ne trouves rien.")
copieFichier("MonFichier", "TonFichier")
readFiles("TonFichier")