from posixpath import split
import sys
from os import name, path

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

def splitFile(src):
    if path.isfile(src):
        with open(src, "r", encoding="utf8") as f:
            fileString = f.read()
            return fileString.splitlines()
    else:
        input("Error "f"{src} does not exist")
        sys.exit()

class searchLists():
    abilityList = splitFile(pokemonAbilitiesPath)
    typeList = splitFile(pokemonTypePath)
    nameList = splitFile(pokemonNamePath)
    natureList = splitFile(pokmoneNaturePath)
    moveList = splitFile(pokemonMovePath)
    pokemonIDs = splitFile(pokemonIDPath)
    trainerName = splitFile(trainerNamePath)
    genderList = splitFile(pokemonGenderPath)
    itemList = splitFile(pokemonItemPath)
    japaneseStatList = splitFile(japanesStatPath)
    showdownStatList = splitFile(statPath)
    TMMoveIDList = splitFile(TMMoveIDsPath)


def getAbility(abilityIndex):
    return searchLists.abilityList[abilityIndex]

def getType(typeIndex):
    return searchLists.typeList[typeIndex]

def getName(nameIndex):
    return searchLists.nameList[nameIndex]

def getNature(natureIndex):
    return searchLists.natureList[natureIndex]

def getMove(moveIndex):
    return searchLists.moveList[moveIndex]

def getNamefromForm(formIndex):
    return searchLists.nameList[int(searchLists.pokemonIDs[formIndex])]

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