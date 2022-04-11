##This generates a changelog for:
##Pokemon Movesets
##Maybe TMs in the future

from os import path
import sys
import UnityPy
from resources import *
from collections import OrderedDict

originalPath = "Original/personal_masterdatas"
editedPath = "Edited/personal_masterdatas"
changelogPath = "Changelogs/Egg Moves.txt"

PersonalTablePathID = 1670399578319621162

pathIDList = [PersonalTablePathID]

compareList = ["Data"]

moveset = "wazaNo"

iterateList = [moveset]

idKey = 'no'  # Used to get pokemon id, as it's named differently in different files
formKey = "formNo"


def exists(src):
    return path.exists(src)


def getUnityTrees(unityfile, pathIDs=pathIDList):

    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())

    return treeList


def splitList(list):
    list1 = []
    list2 = []
    for i in range(len(list)):
        if i % 2 == 0:
            list1.append(list[i])
        else:
            list2.append(list[i])
    return list1, list2


def getGarchompDance(monsno, movenum):
    return monsno == "Garchomp" and movenum == "Quiver Dance"

def main():

    changelogWrite = open(changelogPath, "wt", encoding="utf8")

    original = UnityPy.load(originalPath)
    edited = UnityPy.load(editedPath)

    originalTrees = getUnityTrees(original)[0]
    editedTrees = getUnityTrees(edited)[0]
    
    eggMoves = []
    
    for i in range(16):
        eggMoves.append(i)

    for compareKey in compareList:
        personalTableOriginal = originalTrees[compareKey]
        personalTableEdited = editedTrees[compareKey]

        minLength = min(len(personalTableEdited), len(personalTableOriginal))

        for i in range(1, minLength):
            pokemonOriginal = personalTableOriginal[i]
            pokemonEdited = personalTableEdited[i]

            unchanged = True  # Used to add pokemon name if there are changes
            for j in iterateList:
                if pokemonOriginal[j] != pokemonEdited[j]:
                    changelogWrite.write(
                        f"{getName(pokemonOriginal[idKey], pokemonOriginal[formKey])} ID{pokemonOriginal[idKey]}: \n")
                    unchanged = False
                    break

            if not unchanged:  # If there are changes with any of the functions

                oldMoveset = pokemonOriginal[moveset]
                newMoveset = pokemonEdited[moveset]

                oldMovesetlist = []
                oldMovesetPrint = []

                if len(oldMoveset) > 1:
                    for move in oldMoveset:
                        oldMovesetlist.append(move)
                        oldMovesetPrint.append(move)

                if len(newMoveset) > 1:
                    changelogWrite.write("\n")
                    for move in newMoveset:
                        if move in oldMovesetlist:
                            # If unchanged then doesn't matter
                            delIndex = oldMovesetlist.index(move)
                            oldMovesetlist.pop(delIndex)
                            oldMovesetPrint.pop(delIndex)
                            changelogWrite.write(
                                "Egg: {}\n".format(getMove(move)))
                        else:
                            changelogWrite.write(
                                "Egg: {} [+]\n".format(getMove(move)))

                changelogWrite.write("\n")
                changelogWrite.write("Removed: \n")

                for moves in oldMovesetPrint:
                    level = moves[0]
                    move = moves[1]
                    changelogWrite.write(
                        "Egg: {} [-]\n".format(getMove(move)))

                changelogWrite.write("\n")

            else:

                if devMode:

                    changelogWrite.write(
                        f"{getNamefromForm(pokemonOriginal[idKey])} "f"ID{pokemonOriginal[idKey]}: \n")
                    changelogWrite.write("Unchanged\n")
                    changelogWrite.write("\n")


def getData():

    original = UnityPy.load(originalPath)
    edited = UnityPy.load(editedPath)

    originalTrees = getUnityTrees(original)[0]
    editedTrees = getUnityTrees(edited)[0]
    
    eggMoves = []

    for i in range(16):
        eggMoves.append([])

    for compareKey in compareList:
        personalTableOriginal = originalTrees[compareKey]
        personalTableEdited = editedTrees[compareKey]

        minLength = min(len(personalTableEdited), len(personalTableOriginal))
        
        for i in range(1, minLength):
            pokemonEdited = personalTableEdited[i]
            
            idNum = getIDfromForm(pokemonEdited["no"], pokemonEdited["formNo"])
            pokeEggGroup = getEggGroupfromid(idNum)
            
            for move in pokemonEdited["wazaNo"]:
                for group in pokeEggGroup:
                    eggMoves[group].append(move)
                        
        for group in eggMoves:
            group = list(OrderedDict.fromkeys(group))

        for i in range(1, minLength):
            returnString = ""

            idNum = getIDfromForm(pokemonEdited["no"], pokemonEdited["formNo"])
            pokeEggGroup = getEggGroupfromid(idNum)

            # print(oldMoveset)

            combinedEggMoves = []

            for group in pokeEggGroup:
                combinedEggMoves += eggMoves[group]
                
            combinedEggMoves = list(OrderedDict.fromkeys(combinedEggMoves))
            
            for move in combinedEggMoves:
                returnString += "Egg: {}\n".format(getMove(move))

            returnString += "\n"
            
            yield returnString

if __name__ == '__main__':

    main()
