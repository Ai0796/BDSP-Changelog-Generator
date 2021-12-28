##This generates a changelog for:
##Pokemon Abilities (Tokusei)
##Pokemon Base Stats
##Pokemon Typing

from os import path
import sys
import UnityPy
from resources import *

originalPath = "Original/personal_masterdatas"
editedPath = "Edited/personal_masterdatas"
changelogPath = "Changelogs/TMs Learned.txt"

PersonalTablePathID = 6925071152922426992

pathIDList = [PersonalTablePathID]

compareList = ["Personal"]
     
machine1 = "machine1"
machine2 = "machine2"
machine3 = "machine3"
machine4 = "machine4"

TMList = [machine1, machine2, machine3, machine4] 
iterateList = [machine1, machine2, machine3, machine4] 
byteLengths = [32, 32, 32, 4] ##TMs are three 32 bit ints and one 4 bit int

idKey = 'monsno' ##Used to get pokemon id, as it's named differently in different files
       
def formatTM(TMNum, learns):
    name = getTMName(TMNum)
    TM = ""
    if learns:
        TM = "TM{}: ".format(TMNum)
    else:
        TM = "TM{}: ".format(TMNum)
    formattedTM = TM + name
    return formattedTM
    
def exists(src):
    return path.exists(src)

def getUnityTrees(unityfile, pathIDs = pathIDList):
    
    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())
    
    return treeList

def compareTM(oldTM, newTM):
    return oldTM != newTM
    
def getBitString(num, length):
    binaryNum = format(num, "b")
    return binaryNum.zfill(length)[::-1]


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
                    changelogWrite.write(f"{getName(pokemonOriginal[idKey])}: "f"ID{pokemonOriginal[idKey]}: \n")
                    unchanged = False
                    break
                        
            if not unchanged: ##If there are changes with any of the functions
                
                oldTMStr = ""
                newTMStr = ""

                ##Iterate through the 4 machines
                for i in range(4):
                    key = TMList[i]
                    byteSize = byteLengths[i]
                    oldTM = pokemonOriginal[key]
                    newTM = pokemonEdited[key]
                    oldTMStr += getBitString(oldTM, byteSize)
                    newTMStr += getBitString(newTM, byteSize)
                    
                newLearns = []
                newRemoves = []
                    
                for i in range(len(oldTMStr)):
                    
                    oldTM = oldTMStr[i]
                    newTM = newTMStr[i]                    
                    
                    if oldTM == "1":
                        newLearns.append(i + 1)
                            
                for num in newLearns:
                    changelogWrite.write(formatTM(num, True))
                    changelogWrite.write("\n")
                  
                changelogWrite.write("\n")  
                
            else:
                
                changelogWrite.write(f"{getName(pokemonOriginal[idKey])}: "f"ID{pokemonOriginal[idKey]}: \n")
                changelogWrite.write("Unchanged\n")
                changelogWrite.write("\n")