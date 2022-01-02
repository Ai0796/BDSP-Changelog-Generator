##This generates a changelog for:
##Pokemon Movesets
##Maybe TMs in the future

from os import path
import sys
import UnityPy
from resources import *

originalPath = "Original/personal_masterdatas"
editedPath = "Edited/personal_masterdatas"
changelogPath = "Changelogs/Moveset Changelog.txt"

PersonalTablePathID = 1345203096983357567

pathIDList = [PersonalTablePathID]

compareList = ["WazaOboe"]

moveset = "ar"

iterateList = [moveset]

idKey = 'id' ##Used to get pokemon id, as it's named differently in different files
    
def exists(src):
    return path.exists(src)

def getUnityTrees(unityfile, pathIDs = pathIDList):
    
    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())
    
    return treeList

def splitList(list):
    list1 = []
    list2 = []
    for i in range(len(list)):
        if i%2 == 0:
            list1.append(list[i])
        else:
            list2.append(list[i])
    return list1, list2

if __name__ == '__main__':
    
    changelogWrite = open(changelogPath, "wt", encoding="utf8")
    
    original = UnityPy.load(originalPath)
    edited = UnityPy.load(editedPath)
    
    originalTrees = getUnityTrees(original)[0]
    editedTrees = getUnityTrees(edited)[0]
    
    
    for compareKey in compareList:
        personalTableOriginal = originalTrees[compareKey]
        personalTableEdited = editedTrees[compareKey]
        
        minLength = min(len(personalTableEdited), len(personalTableOriginal))
        
        for i in range(minLength):
            pokemonOriginal = personalTableOriginal[i]
            pokemonEdited = personalTableEdited[i]
            
            unchanged = True ##Used to add pokemon name if there are changes
            for j in iterateList:
                if pokemonOriginal[j] != pokemonEdited[j]:
                    changelogWrite.write(f"{getNamefromForm(pokemonOriginal[idKey])} "f"ID{pokemonOriginal[idKey]}: \n")
                    unchanged = False
                    break
                        
            if not unchanged: ##If there are changes with any of the functions
                
                oldMoveset = pokemonOriginal[moveset]
                newMoveset = pokemonEdited[moveset]
                
                oldLevels, oldMoves = splitList(oldMoveset)
                newLevels, newMoves = splitList(newMoveset)
                
                oldMovesetlist = []
                oldMovesetPrint = []

                if len(oldMoveset) > 1:
                    for level, move in zip(oldLevels, oldMoves):
                        oldMovesetlist.append(move)
                        oldMovesetPrint.append([level, move])
                    
                if len(newMoveset) > 1:
                    changelogWrite.write("New: \n")
                    for level, move in zip(newLevels, newMoves):
                        if move in oldMovesetlist:
                            delIndex = oldMovesetlist.index(move) ##If unchanged then doesn't matter
                            oldMovesetlist.pop(delIndex)
                            oldMovesetPrint.pop(delIndex)
                            changelogWrite.write("{}: {}\n".format(level, getMove(move)))
                        else:
                            changelogWrite.write("{}: {} [+]\n".format(level, getMove(move)))
                        
                changelogWrite.write("\n")
                changelogWrite.write("Removed: \n")

                for moves in oldMovesetPrint:
                    level = moves[0]
                    move = moves[1]
                    changelogWrite.write("{}: {} [-]\n".format(level, getMove(move)))
                
                changelogWrite.write("\n")
                
            else:
                
                changelogWrite.write(f"{getNamefromForm(pokemonOriginal[idKey])} "f"ID{pokemonOriginal[idKey]}: \n")
                changelogWrite.write("Unchanged\n")
                changelogWrite.write("\n")