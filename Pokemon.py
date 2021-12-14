##This generates a changelog for:
##Pokemon Abilities (Tokusei)
##Pokemon Base Stats
##Pokemon Typing

from os import path
import sys
import UnityPy

originalPath = "Original/personal_masterdatas"
editedPath = "Edited/personal_masterdatas"
changelogPath = "Changelogs/personal_masterdatas.txt"
pokemonAbilitiesPath = "Resources/abilities.txt"
pokemonTypePath = "Resources/types.txt"
pokemonNamePath = "Resources/pokemon.txt"

PersonalTablePathID = "6925071152922426992"

pathIDList = [PersonalTablePathID]

compareList = ["Personal"]

ability1 = "tokusei1"
ability2 = "tokusei2"
hiddenAbility = "tokusei3"
type1 = "type1"
type2 = "type2"

iterateList = [ability1, ability2, hiddenAbility, type1, type2]

def splitFile(src):
    if path.isfile(src):
        with open(src, "w", encoding="utf8") as f:
            fileString = f.read()
            return fileString.splitlines()
    else:
        input("Error "f"{src} does not exist")
        sys.exit()
        
abilityList = splitFile(pokemonAbilitiesPath)
typeList = splitFile(pokemonTypePath)     
       
def formatAbility(abilityNum, abilityFlag): ##Change variable name, ability is to see if it's hidden or not
    ability = abilityList[abilityNum]
    abilityType = ""
    if abilityFlag == 3:
        abilityType = "Hidden: "
    else:
        abilityType = "Normal: "
    formattedAbility = abilityType + ability
    return formattedAbility

def formatType(primaryType, secondaryType):
    if primaryType == secondaryType: ##Monotype Pokemon
        type = typeList[primaryType]
        return type
    else: ##Dual Type
        type = typeList[primaryType] + " / " + typeList[secondaryType]
        return type
    
def exists(src):
    return path.exists(src)

def getUnityTrees(unityfile, pathIDs = pathIDList):
    
    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())
    
    return treeList
    

def formatString(pokemon, type, ability):

if __name__ == '__main__':
    
    changelogWrite = open(changelogPath, "wt", encoding="utf8")
    
    original = UnityPy.load(originalPath)
    edited = UnityPy.load(editedPath)
    
    originalTrees = getUnityTrees(original)
    editedTrees = getUnityTrees(edited)
    
    