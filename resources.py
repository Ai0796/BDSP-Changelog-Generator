from posixpath import split
import sys
from os import name, path
import rapidjson

pokemonAbilitiesPath = "Resources/abilities.txt"
pokemonTypePath = "Resources/types.txt"
pokemonNamePath = "Resources/pokemon.txt"
pokmoneNaturePath = "Resources/natures.txt"
pokemonMovePath = "Resources/moves.txt"
pokemonIDPath = "Resources/pokemonid.txt"
trainerNamePath = "Resources/trainername.txt"
pokemonGenderPath = "Resources/gender.txt"
pokemonItemPath = "Resources/items.txt"
japanesStatPath = "Resources/japanesestatnames.txt"
statPath = "Resources/showdownstatnames.txt"
TMMoveIDsPath = "Resources/TMMoveIDs.txt"
pokemonFormPath = "Resources//pokemonForms.txt"


def splitFile(src):
    if path.isfile(src):
        with open(src, "r", encoding="utf8") as f:
            fileString = f.read()
            return fileString.splitlines()
    else:
        input("Error "f"{src} does not exist")
        sys.exit()

def getFormList(src):
    if path.isfile(src):
        with open(src, "r", encoding="utf8") as f:
            fileList = []
            fileString = f.read()
            for line in fileString.splitlines():
                fileList.append(line.split(","))

            return fileList
    else:
        input("Error "f"{src} does not exist")
        sys.exit()
        
def getFormDic(formPath):
    formDic = {}
    with open(formPath, "r", encoding = "utf8") as f:
        for line in f.read().splitlines():
            lineSplit = line.split(",")
            monsno = int(lineSplit[0])
            formno = int(lineSplit[1])
            pokeName = lineSplit[2]
            formDic[(monsno, formno)] = pokeName
    return formDic

class searchLists():
    abilityList = splitFile(pokemonAbilitiesPath)
    typeList = splitFile(pokemonTypePath)
    nameList = splitFile(pokemonNamePath)
    natureList = splitFile(pokmoneNaturePath)
    moveList = splitFile(pokemonMovePath)
    pokemonIDs = getFormList(pokemonIDPath)
    trainerName = splitFile(trainerNamePath)
    genderList = splitFile(pokemonGenderPath)
    itemList = splitFile(pokemonItemPath)
    japaneseStatList = splitFile(japanesStatPath)
    showdownStatList = splitFile(statPath)
    TMMoveIDList = splitFile(TMMoveIDsPath)
    formDic = getFormDic(pokemonFormPath)


settingsPath = "devMode.txt"

try:
    with open(settingsPath) as f:
        data = rapidjson.load(f)
        devMode = data["showUnchanged"]
        
except:
    devMode = 0

def getAbility(abilityIndex):
    return searchLists.abilityList[abilityIndex]

def getType(typeIndex):
    return searchLists.typeList[typeIndex]

def getName(nameIndex, formIndex = 0):
    
    if formIndex > 0:
        try:
            name = searchLists.formDic[(nameIndex, formIndex)]
        except:
            return searchLists.nameList[nameIndex] + " Form Error"
    else:
        name = searchLists.nameList[nameIndex]
        
    return name

def getNature(natureIndex):
    return searchLists.natureList[natureIndex]

def getMove(moveIndex):
    return searchLists.moveList[moveIndex]

def getNamefromForm(formIndex):
    monsno = int(searchLists.pokemonIDs[formIndex][0])
    formno = int(searchLists.pokemonIDs[formIndex][1])
    return getName(monsno, formIndex = formno)

def getTrainerName(nameIndex):
    return searchLists.trainerName[nameIndex]

def getGender(genderIndex):
    return searchLists.genderList[genderIndex]

def getItem(itemIndex):
    return searchLists.itemList[itemIndex]

def getTMMoveID(TMIndex):
    return searchLists.TMMoveIDList[TMIndex]

def getTMName(TMIndex):
    return getMove(int(searchLists.TMMoveIDList[TMIndex]))