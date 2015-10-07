# -*- coding: utf-8 -*-
# Python Hardway, Exercice 36, Designing and Debugging my own Adventure Game
# ex36.py
# This script is about designing an adventure game from scratch with what we know from here

from sys import exit
import time


###
# outside the little house
###

def place_wood_start(player, k, t, m):
    '''a little path going near a house'''

    print('''
        ----------------------
               FOREST
        ----------------------
        ''')

    while True: # infinite loop
        print('%s is in a forest, there is a path going near a *house*.' % player)
        print('%s can either to go near the *house* or to continue *deeper* in the forest.' % player)
        print('Everything is fine, except %s is hungry.' % player)

        choice = prompt()        
#        choice = input(GP)
        
        if choice in ['house', 'House', 'h', 'H']: # go front house
            print("%s go near the house." % player)
            time.sleep(1)
            place_front_house(player, k, t, m)
        
        elif choice in ['deeper', 'Deeper', 'd', 'D']: # go front house
            if k == 1 and t == 1 and m == 1:
                print("%s decide to go deeper in the forest with the tomato, the mozzarella and the knife like a true adventurer." % player) # Easter egg
            else:
                print('%s just adventure deeper into the forest, no one never heard of him since then, \n He is probably dead from hunger.' % player)
            end(player)
        
        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            inventory(k, t, m)
        
        else:
            print("I don't understand your command, %s." % player) # ask again

def place_front_house(player, k, t, m):
    '''the door is closed'''

    print('''
        --------------------------------------
               FRONT OF THE LITTLE HOUSE
        --------------------------------------
        ''')
    
    while True:
        print("%s is in the front entrance of the little white house, behind is the *forest*." % player)
        print("The is a litte path surrounding the house and going in the *back*, there is also a *door*.")
        
        choice = prompt()        
#        choice = input(GP)
        
        if choice in ['back', 'Back', 'b', 'B']:
            print("Moving to the back of the house.")
            time.sleep(1)
            place_back_house(player, k, t, m)
        
        elif choice in ['door', 'open door', 'Door', 'd', 'D']:
            print("The door is closed.\n")
        
        elif choice in ['forest', 'Forest', 'F', 'f']:
            print("%s go to the forest." % player)
            time.sleep(1)
            place_wood_start(player, k, t, m)
            
        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            inventory(k, t, m)
            
        else:
            print("This is not a valid command.")
        
def place_back_house(player, k, t, m):
    '''here is a open door to go inside'''

    print('''
        --------------------------------------
               BACK OF THE LITTLE HOUSE
        --------------------------------------
        ''')
    
    while True:
        print("%s is behind the little white house, there is a path going in the *front*." % player)
        print("Here there is a *door* and a *window*.")

        choice = prompt()        
#        choice = input(GP)

        if choice in ["door", 'Door', 'D', 'd']:
            print("The door is closed.\n")

        elif choice in ["window", 'Window', 'w', 'W']:
            print("The window is open, you can either *enter* or *stay* here")
            choice = prompt()
#            choice = input(GP)
            if choice in ['Enter', 'enter', 'e', 'E']:
                print("%s entering in the house." % player)
                time.sleep(1)
                place_living_room(player, k, t, m)

        elif choice in ["front", 'Front', 'f', 'F']:
            print("%s go to the front entrance of the house." % player)
            time.sleep(1)
            place_front_house(player, k, t, m)

        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            inventory(k, t, m)
            
        else:
            print("I don't understand the command.")

###
# in the white house
###


def place_living_room(player, k, t, m):
    '''it is the living room, a door go in kitchen'''

    print('''
        ----------------------
             LIVING ROOM
        ----------------------
        ''')

    while True:
        print("%s is in the living room, there is four doors and one window, the one to go *outside*." % player)
        print("There is one door which is going in the *kitchen* and other one going in the *bedroom*.")
        print("The third and fourth doors are the front and back entrance, closed.")
        if t == 0:
            print("In the living room there is a table with one *tomato*")
        else:
            print('There is a table in the middle of the living room.')

        choice = prompt()            
#        choice = input(GP)
        
        if choice in ['tomato', 'Tomato', 't', 'T']:
            if t == 0:
                print('%s take the tomato and put it in his pocket.' % player)
                time.sleep(1)
                t = 1
            else:
                print('You have already took the tomato, check your *inventory*.')
                
        elif choice in ['out', 'O', 'outside', 'o', 'Outside', 'OUT']: # window, sortir de la maison
            print('%s go outside the house using the window.' % player)
            time.sleep(1)
            place_back_house(player, k, t, m)
            
        elif choice in ['kitchen', 'Kitchen', 'k', 'K']: # door 1, go in the kitchen
            print("%s go in the kitchen." % player)
            time.sleep(1)
            place_kitchen(player, k, t, m)
            
        elif choice in ['bedroom', 'Bedroom', 'b', 'B']: # door 2, go in the bedroom
            print("%s go in the bedroom." % player)
            time.sleep(1)
            place_bedroom(player, k, t, m)
            
        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            print("%s open his inventory" % player)
            time.sleep(1)
            inventory(k, t, m)
        
        else:
            print("I don't understand the command.")
        
def place_kitchen(player, k, t, m):
    '''here is the kitchen'''

    print('''
        ----------------------
               KITCHEN
        ----------------------
        ''')

    while True:
        print("%s is in the kitchen, there is a *door* to go in the living room." % player)
        print("Here you can *cook* with what you have collected so far.")
        if m == 0:
            print("The is a fridge, inside there is only a bit of *mozzarella*.")
        else:
            print("There is an empty fridge.")

        choice = prompt()            
#        choice = input(GP)
        
        if choice in ["cook", 'Cook', 'COOK', "C", 'c']:
            print("%s start cooking" % player)
            cooking_salad(player, k, t, m)
            time.sleep(1)

        if choice in ["mozzarella", "Mozzarella", "m", "M"]:
            if m == 0:
                print("%s catch the mozzarella and put it in his pocket." % player)
                time.sleep(1)
                m = 1
            else:
                print("You already took the mozzarella, check your *inventory*.")
                time.sleep(1)
                
        if choice in ["door", 'D', 'd', 'Door']:
            print("%s enter in the living room." % player)
            time.sleep(1)
            place_living_room(player, k, t, m)

        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            print("%s open his inventory" % player)
            time.sleep(1)
            inventory(k, t, m)

def place_bedroom(player, k, t, m):
    '''here is the bedroom'''

    print('''
        ----------------------
               BEDROOM
        ----------------------
        ''')

    while True:
        print("%s is in the bedroom, there is a *door* to go in the living room." % player)
        
        if k == 0:
            print("There is a bed here, with a *knife* under the pillow.")
        else:
            print("There is a bed here.")

        choice = prompt()            
#        choice = input(GP)
        
        if choice in ["Knife", "knife", "k", "K"]:
            if k == 0:
                print("%s take the knife and hang it to his belt." % player)
                k = 1
            else:
                print("You already have the knife, check your *inventory*.")
                
        if choice in ["door", 'D', 'd', 'Door']:
            print("%s enter in the living room." % player)
            time.sleep(1)
            place_living_room(player, k, t, m)
        
        elif choice in ['inventory', 'Inventory', 'I', 'i']: # checking the inventory
            inventory(k, t, m)

###
# inventaire
###

def inventory(k, t, m):
    '''check the inventory'''

    while True:
        print("You have %r knife, %r tomato and %r mozzarella" % (k, t, m))
        print("you can *look* an object using the command : *look knife*, *look tomato* or *look mozzarella*")
        print("You can leave your inventory with the *quit* command")
        choice = prompt()
#        choice = input(GP)

        if choice == "look knife":
            object_knife(k)
        elif choice == "look tomato":
            object_tomato(t)
        elif choice == "look mozzarella":
            object_mozzarella(m)
            
        elif choice in ['q', 'QUIT', 'Quit', 'Q', 'quit']:
            break

        else:
            print("I don't understand your command sorry.")

###
# les trois objets à trouver dans le jeu
###

def object_knife(k):
    '''object knife'''
    
        # knife
    if k == 1:
        print('The knife is sharp.')
    else:
        print("The don't have knife.")
        
def object_tomato(t):
    '''object tomatoe'''
    
        # tomato
    if t == 1:
        print('The tomato look juicy.')
    else:
        print("You don't have tomato.")
            
def object_mozzarella(m):
    '''object mozzarella'''
    
        # mozzarella
    if m == 1:
        print('The mozzarella is white.')
    else:
        print("You don't have mozzarella.")

###
# l'action que peut entreprendre le joueur une fois qu'il a trouvé les trois objets
###

# victoire
def cooking_salad(player, k, t, m):
    '''game is won by cooking salad with three objects'''
    
    if k == 1 and t == 1 and m == 1:
        print("%s use the knife to cook a salad with tomato, mozzarella." % player)
        print("Prepare yourself for a nice meal.\n")
        print("***********")
        print("You won !!!")
        print("***********")
        time.sleep(1)
        end(player)
    
    else:
        print("You missing something to cook the salad.")

# game over        
def end(player):
    '''everything must finish somewhere'''
       
    print('''
        ----------------------
              GAME OVER
        ----------------------
        ''')
    time.sleep(1)    
    print("Bye %s, don't hesitate to play the game once more, and to buy the full version of the game.\n" % player)
    exit(0)

# demander le nom du joueur pour le garder dans une variable le temps du jeu
def player():
    '''here is where we ask the player his name'''

    print('\n***')
    print("PAX FABRICA GAME 01")
    print("Welcome user, in the python game adventure of Pax Fabrica")
    print('***\n')
    print("What's the name of the player ?")
    name = prompt()
#    name = input(GP)
    return name

# présente au joueur les règles
def rule():
    '''rules of the game'''
    
    print('do you want help before to start ? *yes* or *no*') # juste un peu d'explication concernant le fonctionnement du jeu
    answer = prompt()
#    answer = input(GP)
    if answer in ["yes", "YES", "Yes", "y", "Y"]:
        print("\n     ***     ")
        print("You can use the words surrounded by star * as commands to play with the possible actions.")
        print("You can check your *inventory* at any moment.")
        print("Type your command after the prompt '>'.")
        print("     ***     \n")
    else:
        return

# prompt du jeu
def prompt():
    '''le prompt qui renvoi au jeu les intéractions du joueur'''

    command = input('> ')
    return command

# on prépare les variables du jeu
#GP = '> ' # Game Prompt
knife, tomato, mozzarella = 0, 0, 0 # ici on commence la quête du jeu avec 0 à chaque objet

# puis le jeu démarre ici
def start():
    '''everything must start somewhere'''
    playername = player() # ici on enregistre le nom du joueur qui sera envoyé dans chaque fonction et utilisé toute la durée du jeu   
    rule() # ici on propose la lecture des règles du jeu
    print("Hello %s, it's time to play, loading.." % playername) # ici on lance le joueur dans le jeu
    time.sleep(2)
    
# START PLACE
    place_wood_start(playername, knife, tomato, mozzarella) # the start place of the adventure game

# DEBUG JUMPS
#    inventory(knife, tomato, mozzarella) # inventory debug jump
#    place_back_house(playername, knife, tomato, mozzarella) # debug jump
#    place_living_room(playername, knife, tomato, mozzarella) # debug jump
#    place_kitchen(playername, knife, tomato, mozzarella) # debug jump
#    place_bedroom(playername, knife, tomato, mozzarella) # debug jump
    
start()
print('BYE...')
time.sleep(2)
exit(0)