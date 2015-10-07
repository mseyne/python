# -*- coding: utf-8 -*-
# Python Hardway, Exercice 25, Even More Practice
# ex25.py
# This script create somes functions to be imported and used

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    
def return_first_word(words):
    """Return the first word after popping it off."""
    word = words.pop(0)
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def return_last_word(words):
    """Return the last word after popping it off."""
    word = words.pop(-1)
    return word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
#    variable1 = return_first_word(words)
#    variable2 = return_last_word(words)
#    variable = variable1 + variable2
#    print(variable)
    print(return_first_word(words) + ' ' + return_last_word(words))
    
def return_first_and_last(sentence):
    """Return the first and last words of the sentence."""
    words = break_words(sentence)
    return return_first_word(words) + ' ' + return_last_word(words) #test

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
#    words = break_words(sentence)
#    words_sorted = sort_words(words)
    words_sorted = sort_sentence(sentence)
    print(return_first_word(words_sorted) + ' ' + return_last_word(words_sorted))