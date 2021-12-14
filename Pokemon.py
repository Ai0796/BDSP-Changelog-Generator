##This generates a changelog for:
##Pokemon Abilities (Tokusei)
##Pokemon Base Stats
##Pokemon Typing

from os import path
import sys
import UnityPy

inputPath = "Original/personal_masterdatas"
outputPath = "Edited/personal_masterdatas"
pokemonAbilitiesPath = "Resources/Abilities.txt"
pokemonTypePath = "Resources/Types.txt"

def splitFile(src):
    if path.isfile(src):
        with open(src, "w", encoding="utf8") as f:
            fileString = f.read()
            return fileString.splitlines()
    else:
        input("Error "f"{src} does not exist")
        sys.exit()
        
  
