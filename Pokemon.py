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
changelogPath = "Changelogs/Pokemon Changelog.txt"

PersonalTablePathID = 6925071152922426992

pathIDList = [PersonalTablePathID]

compareList = ["Personal"]

ability1 = "tokusei1"
ability2 = "tokusei2"
hiddenAbility = "tokusei3"
type1 = "type1"
type2 = "type2"

abilityList = [ability1, ability2, hiddenAbility] 
iterateList = [ability1, ability2, hiddenAbility, type1, type2]

idKey = 'monsno' ##Used to get pokemon id, as it's named differently in different files
       
def formatAbility(abilityNum, abilityFlag): ##Change variable name, ability is to see if it's hidden or not
    ability = getAbility(abilityNum)
    abilityType = ""
    if abilityFlag == 3:
        abilityType = "Hidden Ability: "
    else:
        abilityType = "Normal Ability {}: ".format(abilityFlag)
    formattedAbility = abilityType + ability
    return formattedAbility

def formatType(primaryType, secondaryType):
    if primaryType == secondaryType: ##Monotype Pokemon
        type = getType(primaryType)
        return type
    else: ##Dual Type
        type = getType(primaryType) + " / " + getType(secondaryType)
        return type
    
def exists(src):
    return path.exists(src)

def getUnityTrees(unityfile, pathIDs = pathIDList):
    
    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())
    
    return treeList

def compareAbility(oldAbility, newAbility, abilityFlag):
    if oldAbility == newAbility:
        return formatAbility(oldAbility, abilityFlag) + "\n"
    else:
        return formatAbility(oldAbility, abilityFlag) + " -> " + getAbility(newAbility) + "\n"
    
def compareType(oldtype1, oldtype2, newtype1, newtype2):
    type1Diff = oldtype1 != newtype1
    type2Diff = oldtype2 != newtype2
    
    if type1Diff or type2Diff:
        return "Type: " + formatType(oldtype1, oldtype2) + " -> " + formatType(newtype1, newtype2) + "\n"
    else:
        return ""


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
                    changelogWrite.write(f"{getNamefromForm(pokemonOriginal[idKey])}: "f"ID{pokemonOriginal[idKey]}: \n")
                    unchanged = False
                    break
                        
            if not unchanged: ##If there are changes with any of the functions
                
                ##Iterate through the 3 abilities
                for i in abilityList:
                    originalAbility = pokemonOriginal[i]
                    newAbility = pokemonEdited[i]
                    abilityFlag = int(i[-1])
                    changelogWrite.write(compareAbility(originalAbility, newAbility, abilityFlag))
                    
                ##Compare the two types
                oldtype1 = pokemonOriginal[type1]
                oldtype2 = pokemonOriginal[type2]
                newtype1 = pokemonEdited[type1]
                newtype2 = pokemonEdited[type2]
                
                changelogWrite.write(compareType(oldtype1, oldtype2, newtype1, newtype2))
                changelogWrite.write("\n")
                
                
            else:
                
                changelogWrite.write(f"{getNamefromForm(pokemonOriginal[idKey])}: "f"ID{pokemonOriginal[idKey]}: \n")
                changelogWrite.write("Unchanged\n")
                changelogWrite.write("\n")