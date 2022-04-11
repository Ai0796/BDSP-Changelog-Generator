##This generates a changelog for:
##Pokemon Abilities (Tokusei)
##Pokemon Base Stats
##Pokemon Typing

from os import path
from shutil import move
import sys
import UnityPy
from resources import *
import ChangelogGenerators.Movesets
import ChangelogGenerators.TMLearned
import ChangelogGenerators.Egg
import ChangelogGenerators.Pokemon

# originalPath = "Original/personal_masterdatas"
# editedPath = "Edited/personal_masterdatas"
changelogPath = "Changelogs/Summary.txt"

def main():
    moves = ChangelogGenerators.Movesets.getData()
    tms = ChangelogGenerators.TMLearned.getData()
    eggs = ChangelogGenerators.Egg.getData()
    abilities = ChangelogGenerators.Pokemon.getData()
    
    changelogWrite = open(changelogPath, "w+", encoding="utf8")
    
    # print(tms)
    
    # for tm in tms:
    #     print(tm)
    zipped = zip(moves, tms, eggs, abilities)

    monsno = 1
    for move, tm, egg, abilities in zipped:
        pokemon = getNamefromForm(monsno)
        monsno += 1
        move = move.strip()
        tm = tm.strip()
        egg = egg.strip()
        abilities = abilities.strip()
        
        changelogWrite.write(f"{pokemon}\n{abilities}\n\n{move}\n{tm}\n\n")

if __name__ == '__main__':

    main()
