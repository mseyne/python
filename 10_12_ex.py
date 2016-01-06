# -*- coding:Utf-8 -*-
'Extract from text all words that start with Uppercase letter.'

upperWordList = [] # will get the uppercase words inside

def extractWords(text):
    "get the uppercase words from sentence"
    # global upperWordList
    flag = 0
    word = "" #fill the word with letter from an uppercase letter
    c = 1

    for letter in text:
        if letter == letter.upper() and letter != " ": #if caract is uppercase, flag = 1
            # print("debug1")
            flag = 1

        if flag == 1 and letter != " ":
            # print("debug2")
            word += letter

        if flag == 1 and letter == " " or flag == 1 and c == len(text): 
            #the word is added to list when there is an empty space or the end of string + reset all to default
            upperWordList.append(word)
            # print("debug3", upperWordList)
            # print("debug3", flag, word)
            word = ""
            flag = 0
        c += 1 #used to compage index and lenght from sentence


userText = input("Write a text with uppercase word.\n>>>")
extractWords(userText)

if len(upperWordList) > 0:
    print("The words with uppercase in this sentence are :")
    for word in upperWordList:
    	print(word)
else:
    print("No word with uppercase in this sentence.")