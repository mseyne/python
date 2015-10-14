#Apprendre Python
*notes de cours*
source : (http://python.developpez.com/cours/apprendre-python3/)

##Programme/Sommaire :

###PARTIE 1 : SYNTAXE DU LANGAGE PYTHON

####leçon 0 : introduction à la programmation et le langage python + installation

* qu'est ce que le développement logiciel et un langage de programmation ?
* introduction au langage python, comment l'installer (sous windows, linux et mac)
* comment lancer et utiliser une console shell(powershell, terminal)
* présentation de idle, interpréteur et éditeur de texte

####leçon 1 :  première utilisation de l'interpréteur et des nombres

* des nombres int, float
* des calculs, opérateurs mathématiques + - / * (// % etc)
* la fonction type()
* les commentaires #

####leçon 2 : les variables et les chaines de caractères

* assignement de variable =
* La fonction print() et les chaînes de caractères string
* la fonction input()
* la bibliothèque sys, l'argument argv ?

#### Leçon 3 : les boucles

* boucle while
* boucle for
* incrémentation +1
* l'opérateur modulo %

#### Leçon 4 : les listes et dictionnaires

* len()
* del et .remove()
* append()

#### Leçon 5 : les fonctions

* def
* variable global


######Installation de Python et de l'IDLE, et un éditeur de texte

Première approche de la syntaxe du language.

Utilisation de l'interpréteur, puis création de premier scripts sauvegardé.

Le prompteur Python Shell ">>>" :

Au commencement nous avons l'interpréteur Python Shell qui se présente avec trois signe de comparaison supérieur à : " > "
>>>


Commençons à découvrir les expressions, qui consistes en des combinaisons de valeurs (0, 1, 'a', 'b', etc...) et des opérateurs (+, -, =, etc..)

>>> 2 + 2
4 

Une expression renvoi toujours une valeur. Même une valeur peut devenir une expression en elle-même en renvoyant une valeur.
>>> - 5
-5

######Données (valeurs) et types et la fonction type( )

Les données sont les informations tel que les nombres et les lettres (appelées chaînes de caractère) que le programme utilise pour fonctionner. Pour les nombres il existe dans python principalement deux types, les nombres entiers sont de type integer (int) et les nombres décimaux sont de type float.

Dans l'interpréteur la fonction type( ) permet de connaître le type dans lequel python range la donnée.

'''python
>>> type(42)
<class 'int'>
>>> type(1)
<class 'int'>
>>> type(2.)
<class 'float'>
>>> type(3.14)
<class 'float'>
'''

Il existe aussi le type string (str) pour les chaînes de caractères que nous veront ailleurs.

>>> type("hello")
<class 'str'>

#####Variables

Une variable est une boite dans laquelle se trouve une donnée, une valeur.
Il s'agit d'un nom pour une objet.
Assignation/Affectation d'une valeur à une variable.

'''python
>>> x = 5 * 5
>>> print (x)
25
>>> message = "Bonjour !"
>>> print(message)
Bonjour !
>>> a = 5
>>> b = a
>>> c = a + b
>>> print(a, b, c)
5 5 10
>>> 
'''


######Chaîne de caractères

L'interpréteur Python reconnaît les lettres et les mots comme des fonctions ou des variables, lorsque l'on souhaite utiliser les lettres et les nombres comme une données à utiliser dans le programme en dehors des calculs, il existe les chaînes de caractères de type string (str)

'''python
>>> Bonjour
Traceback (most recent call last):
File "<pyshell#15>", line 1, in <module>
Bonjour
NameError: name 'Bonjour' is not defined
>>> "Bonjour"
'Bonjour'
>>> Bonjour = "Bonjour"
>>> type(Bonjour)
<class 'str'>
>>> type("Bonjour")
<class 'str'>
>>>
''' 

Ce que l'on remarque dans cet exemple, c'est que l'utilisation de lettres dans l'interpréteur renvoie une erreur, car Python cherche une variable appelé Bonjour mais qui n'a jamais été défini. 

On utilise l'apostrophe (single quote) ou le guillemet (double quote) pour signifier au programme l'utilisation d'une chaîne de caractère string.

'''python
>>> "Bonjour"
'Bonjour'
>>> 'Bonjour'
'Bonjour'
>>> 4566
4566
>>> "4566"
'4566'
>>> 
'''

Des nombres entre guillemet sera toujours considéré comme une chaîne de caractère pour python et non pas une donnée integer ou float.

La différence entre une fonction et une variable sera expliqué plus loin.

######Instructions (Statements)

Les intructions sont toutes les commandes légales du programme que Python peut interpréter.

>>> x = 5 * 5 # assignation à une variable x
>>> print(1) # utilisation de la fonction print ( )
1

######Opérations et opérandes : 
Quelques expressions mathématiques dans l'interpréteur :

En utilisant les nombres et les opérateurs mathématiques, il est possible de faire des opérations directement dans l'interpréteur python. Les opérateurs mathématiques +, -, * et / sont reconnus par python. 

'''python
>>> 1 + 2
3
>>> 9 - 6
3
>>> 9 / 3
3.0
>>> 2 / 3
0.6666666666666666
>>> 2 + 3 * 5
17
>>> (2 + 3) 5
SyntaxError: invalid syntax
>>> (2 + 3) * 5
25
>>> 
'''

Il est possible d'utiliser les opérateurs avec des chaînes de caractères.

'''python
>>> "ab" * 3
'ababab'
>>> "a" + "bc" #Concaténation
'abc'
>>> 3 + "a"
Traceback (most recent call last):
File "<pyshell#2>", line 1, in <module>
3 + "a"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(3) + "a" # changement de type avec la fonction str( )
'3a'
>>> 
'''

######Ordre des opérations (P – E – MD - AS)

1)Parenthèses

>>> 2 * (3-1)
4
>>>(1+1) ** (5-2)
8

2)Exposants
>>> 2**1 + 1
3


3)Multiplications et Division

4)Addition et Soustraction


######La fonction print( )

La fonction print( ) permet d'afficher à l'écran une donnée.

>>> print(1)
1
>>> print(2 + 3.)
5.0
>>> print('Bonjour')
Bonjour
>>> 

l'argument sep remplace l'espace entre des données séparé par des virgules par le caractère souhaité

>>> print("bonjour", "monde", "!")
bonjour monde !
>>> print("bonjour", "monde", "!", sep="*")
bonjour*monde*!
>>>

l'argument end remplace le saut à la ligne


print("bonjour", end=" ")
print("monde", end=" ")
print("!", end=" ")
bonjour monde !

######Commentaires # et ''''''

Les commentaires sont des instructions ignorées par Python qui permettent de documenter le programme et en faciliter la lecture.

######La fonction input()

Le fonction input( ) permet d'attendre de l'utilisateur une donnée à entrer dans le programme.

>>>nom = input("Quel est ton nom ?")
Quel est ton nom ?
>>>print ('Bonjour', nom)
Bonjour michael


######Le type boolean : fonction bool( )

Une valeur booléenne est soit True (vrai) soit False (fausse) 

>>> 2 == 2
True
>>> 2 == 1
False
>>> 

######Opérateurs logiques Or, And et Not

l'opérateur Not transforme vrai en faux et faux en vrai.

Or est True si l'une des deux proposition sont vrai.

And est True si les deux proposition sont vrai.

>>> True and False
False
>>> True and True
True
>>> False and False
False
>>> True or False
True
>>> True or True
True
>>> False or False
False
>>> Not True
SyntaxError: invalid syntax
>>> not True
False
>>> not False
True
>>> not False and True
True
>>> 

######L'opérateur modulo % et les opérateurs de division / et //

Tandis que l'opérateur de division travaille sur une donnée integer 

>>> 7 / 2 # la division float
3.5
>>> 7 // 2 #la division integer
3
>>> 7 % 2 #le reste aprés une division de 7 divisé par 2 est 1
1
>>> 

######String ou Chaînes de caractères

Un nombre est converti en chaine de caractère avec la fonction str( ). (de la même façon une chaine de caractères contenant des nombres peut être converti avec la fonction int( ) et float( ) )


>>> 432
432
>>> str('432')
'432'
>>> nombre = 432
>>> str(nombre)
'432'
>>> nombre = str(nombre)
>>> nombre
'432'
>>> nombre + 25
Traceback (most recent call last):
File "<pyshell#31>", line 1, in <module>
nombre + 25
TypeError: Can't convert 'int' object to str implicitly

>>> nombre + '25'
'43225'
>>> nombre = int(nombre)
>>> nombre
432
>>> nombre + 25
457

La chaine de caractères se délimite par des guillemets '' ou des apostrophes '. Un triple guillemet permet d'introduire tous les caractères sans recourir au \.

>>> prt = 'C\'est une catastrophe!'
>>> prt
"C'est une catastrophe!"
>>> prt2 = 'Cest pas vrai'
>>> prt2
'Cest pas vrai'
>>> prt
"C'est une catastrophe!"
>>> prt3 = 'C\'est une \"catastrophe\"'
>>> prt3
'C\'est une "catastrophe"'
>>> prt4 = """C\'est une \"catastrophe\""""
>>> prt4
'C\'est une "catastrophe"'
>>> 

Certaine séquences dans une chaîne de caractères permet d'agir à l'intérieure de celle ci, on utilise pour cela l'antislash \.
\n insère un saut à la ligne
\' permet d'insérer une apostrophe entre deux apostrophe

La casse de caractères est significative une variable haha est différente de HaHa ou encore HAHa.

Les séquences d'une chaîne de caractère se trouve dans un index qui commence par 0.
Par exemple la chaîne 'Bonjour' de la variable bonjour.

>>> bonjour = 'Bonjour'
>>> bonjour[0]
'B'
>>> bonjour[7]
Traceback (most recent call last):
File "<pyshell#14>", line 1, in <module>
bonjour[7]
IndexError: string index out of range
>>> bonjour[6]
'r'
>>> print(bonjour[1], bonjour[3], bonjour[4])
o j o

len() est une fonction qui calcul le nombre de caractères dans une chaîne. (string)

>>> len(bonjour)
7

lower( ) et upper( ) sont des méthodes qui ne s'applique qu'aux chaine de caractères : 

>>> bonjour.lower()
'bonjour'
>>> bonjour.upper()
'BONJOUR'
>>> bonjour
'Bonjour'
>>> 

On remarque que la variable bonjour reste non affecté par les méthodes.

La concaténation est une opération qui fait de deux chaines de caractères, une nouvelle qui est l'addition des deux.

>>> a = "Bonjour "
>>> b = input("Quel est ton nom ?")
Quel est ton nom ?Michael
>>> c = a + b
>>> c
'Bonjour Michael'
>>> 

######Conditions if, elif, else

if est une instruction que nous appelons une condition, elle est suivit d'une expression qui se doit d'être vrai pour que le bloc indenté sous la condition soit executé par le programme.

Le programme est appelé à branche si l'on utilise les instructions if, elif et else pour proposer différentes conditions que le programme doit atteindre afin de trouver son déroulement opératoire.

>>> x = 10
>>> 
if x < 5:
	print(x, "est inférieur à 5")
elif x < 10:
	print(x, "est inférieur à 10")
elif x == 10:
	print(x, "est égal à 10")
else:
	print(x, "est supérieur à 10")
10 est égal à 10
>>> 

Si une condition est fausse, les instructions indenté sont simplement ignorées.

Bloc d'instructions, instructions composées et indentation

Les opérateurs de comparaisons dans les instructions conditionnels

< inférieur à 
> supérieur à
=> égal ou supérieur
=< égal ou inférieur
== égal à 
!= différent de

En utilisant un opérateur de comparaison python retourne une valeur booléenne. (True, False)

######Boucle while

La boucle while est suivie d'une intructions qui répète le bloc d'instruction indenté dans la boucle tant que l'instruction est vrai (True).

>>> x = 0
>>> while x < 4:
	print(x, "bonbon(s)")
	x += 1

0 bonbon(s)
1 bonbon(s)
2 bonbon(s)
3 bonbon(s)

######Boucle For

>>>for i in range(10)
		print(i)

######Incrémentation

L'incrémentation est utile dans boucle car il s'agit d'augmenter ou diminuer une valeur à elle-même progressivement afin de la faire atteindre une valeur qui est necessaire pour remplir une condition.

+= ajouter à

-= diminuer à

>>> x = 1
>>> x = x + 1
>>> print(x)
2
>>> x = x - 1
>>> print(x)
1
>>> x += 1 #identique a x = x + 1
>>> print(x)
2
>>> x -= 1 #identique à x = x - 1
>>> print(x)
1
>>> 


######Liste

Une liste est un ensemble de données assigné au sein d'une même variable. 

>>> x = [1, 2, 3, 4, 5]

pour connaître le nombres de données dans une liste il suffit d'utiliser la fonction len()

>>>len(x)
5

Il est possible d'accéder à ces données individuellement. il s'agit d'utiliser la position de la donnée dans séquence. La séquence ne commence pas par 1, mais par 0.

>>>x[0]
1
>>>x[4]
5

En sortant de la séquence, on reçoit une erreur.

>>> x[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range



Il est possible de supprimer une donnée avec del et la méthode .remove()

del permet de supprimer à partir de sa position dans la liste

>>> del x[0]
>>>x
[2, 3, 4, 5]

tandis que .remove() supprimer la donnée elle même

>>x.remove(5)
>>x
[2, 3, 4]

attention toutefois, si la donnée est multiple, il ne supprime que la première.

>>> x = [1, 1, 1]
>>> x
[1, 1, 1]
>>> x.remove(1)
>>> x
[1, 1]
>>>

ou d'en ajouter une  avec la méthode .append()

>>>x.append(''bonjour'')
>>>x
[1, 1, 'bonjour']



######Dictionnaires

>>>a = {"0" : 0, "1" : 1} 



###### Définir une fonction originale

def nom_fonction(paramètres):
	instructions

Voici un exemple de fonction simple :

>>> def table(n):
...    c = 1
...    while c < 11 :
...       print(c * n, end =' ')
...       c = c + 1
...
Nous pouvons ensuite appeler la fonction "table" autant de fois que l'on souhaite en lui donnant un paramètre "n".

>>>table(7)
7 14 21 28 35 42 49 56 63 70



###### Variable globale


À l'intérieure d'une fonction, on peut informer que nous ne souhaitons pas qu'une variable soit locale, mais modifie une variable globale qui a été défini hors de la fonction. On peut faire cela dans une fonction en déclarant la variable globale avec l'instruction global.

>>>def up():
...	global a
...	a += 1
>>>a = 15
>>>up(a)
>>>print(a)
16
>>>up(a)
>>>print(a)
17



###### Return

Une fonction le plus souvent reçoit des données, les transforment et renvoie de nouvelles données, pour renvoyer, elle utilise l'instruction return

>>>def cube(x):
... 	return x * x * x

>>>b = cube(9)
>>> print(b)
729


###### Commentaire de fonction

utilise " pour créer un commentaire qui est lié à la fonction et est accessible par la suite par print(fonction.__doc__)

>>> def carre(a)
... 	"met au carré a"
...	n = a * a
... 	return n


######Premiers modules

ex : Import Math

Les modules sont des fichiers qui regroupent des ensembles de fonctions
>>> from math import * #import toutes les fonctions du module
>>> sin(pi/6)
0.49999
>>>sqrt(100) #racine carrée
10.0

ex : Import Random

ex : Import Turtle


###### Créer un nouveau module 

Si la fonction est sauvegardé dans un fichier, elle peut être appelé comme un module avec import et est alors utilisé avec son nom de fichier. 

Ex, Si l'on sauvegarde la fonction précédente (carre) dans le fichier cr.py on peut l'appeler dans un autre fichier de programme ainsi :

>>>import cr
>>>cr.carre(4)
16

###### Valeur par défaut définition d'une fonction

Il est possible de définir par défault un argument avec une valeur, si la fonction est appelé sans cet argument, il utilisera la valeur par défault, sinon l'argument prendra la valeur envoyé.

>>>def politesse(nom, titre ='Monsieur')
...		print("Bonjour", titre, nom)
>>>politesse("Michael")
Bonjour Monsieur Michael
>>>politesse("Laura", "Madame")
Bonjour Madame Laura