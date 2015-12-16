#! /usr/bin/env python
# -*- coding:Utf-8 -*-


def countChr(uistr, uich):
    "return the number of time the character occur in the string"
    nbChr = 0
    for char in uistr:
        if char == uich:
            nbChr += 1
    return nbChr


# Test :
if __name__ == '__main__':
    strUserInput = input("A sting\n>>>")
    chrUserInput = input("A charactere\n>>>")
    countNb = countChr(strUserInput, chrUserInput)
    print("The character", chrUserInput, "occur", countNb, "times in", strUserInput)
