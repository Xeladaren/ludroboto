#!/bin/python3

import difflib

print("hello word");

def findStringInList(inString, stringList):

    outData = (0, "")

    for string in stringList:
        stringDiff = difflib.SequenceMatcher(None, string, inString).ratio()
        print("{:.2f} : {}".format(stringDiff, string))
        if stringDiff > outData[0]:
            outData = (stringDiff, string)
    
    return outData


stringList = []
stringList += ["bonjour"]
stringList += ["au revoir"]
stringList += ["quels jeux connais tu"]
stringList += ["qui joue a"]
stringList += ["que sais tu faire"]
stringList += ["connais tu"]
stringList += ["je veux ajouter un jeu"]
stringList += ["je joue a"]

jeuxList = []
jeuxList += ["minecraft"]
jeuxList += ["minetest"]
jeuxList += ["scrib.io"]
jeuxList += ["garlic phone"]

inputString = input("entre un string : ").lower()

(diffVal, string) = findStringInList(inputString, stringList)

if diffVal > 0.30:
    
    print("")
    (diffVal2, jeu) = findStringInList(inputString, jeuxList)

    print("")
    print("String : {}".format(string))
    print("Diff   : {:.2f}".format(diffVal))
    if diffVal2 > 0.30:
        print("Jeu    : {}".format(jeu))
        print("DiffJeu: {:.2f}".format(diffVal2))
else:
    print("")
    print("String not found.")
