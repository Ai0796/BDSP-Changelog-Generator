from posixpath import split
import sys
from os import name, path

pokemonAbilitiesPath = "Resources/abilities.txt"
pokemonTypePath = "Resources/types.txt"
pokemonNamePath = "Resources/pokemon.txt"
pokmoneNaturePath = "Resources/natures.txt"
pokemonMovePath = "Resources/moves.txt"
pokemonIDPath = "Resources/pokemonid.txt"

def splitFile(src):
    if path.isfile(src):
        with open(src, "r", encoding="utf8") as f:
            fileString = f.read()
            return fileString.splitlines()
    else:
        input("Error "f"{src} does not exist")
        sys.exit()
        
abilityList = splitFile(pokemonAbilitiesPath)
typeList = splitFile(pokemonTypePath)
nameList = splitFile(pokemonNamePath)
natureList = splitFile(pokmoneNaturePath)
moveList = splitFile(pokemonMovePath)
pokemonIDs = splitFile(pokemonIDPath)


def getAbility(abilityIndex):
    return abilityList[abilityIndex]

def getType(typeIndex):
    return typeList[typeIndex]

def getName(nameIndex):
    return nameList[nameIndex]

def getNature(natureIndex):
    return natureList[natureIndex]

def getMove(moveIndex):
    return moveList[moveIndex]

def getNamefromForm(formIndex):
    return nameList[int(pokemonIDs[formIndex])]