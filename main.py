from doctest import master
import ChangelogGenerators.Movesets
import ChangelogGenerators.Pokemon
import ChangelogGenerators.TMCompat
import ChangelogGenerators.TMLearned
import ChangelogGenerators.Trainers
import ChangelogGenerators.Summary
import ChangelogGenerators.Egg
from os import path
import traceback

originalPath = "Original/"
editedPath = "Edited/"

def gamesettingExists():
    gamesettings = "gamesettings"
    return path.exists(originalPath + gamesettings) and path.exists(editedPath + gamesettings)

def masterdatasExists():
    masterdatas = "masterdatas"
    return path.exists(originalPath + masterdatas) and path.exists(editedPath + masterdatas)

def pmlExists():
    pml = "personal_masterdatas"
    return path.exists(originalPath + pml) and path.exists(editedPath + pml)

if __name__ == '__main__':
    
    try:
        print("Generating changelogs...")
        
        if masterdatasExists():
            ChangelogGenerators.Trainers.main()
        else:
            print("masterdatas not found")
        if pmlExists():
            ChangelogGenerators.Movesets.main()
            ChangelogGenerators.Pokemon.main()
            ChangelogGenerators.TMCompat.main()
            ChangelogGenerators.TMLearned.main()
            ChangelogGenerators.Egg.main()
            ChangelogGenerators.Summary.main()
        else:
            print("personal_masterdatas not found")
            
        print("Finished generating changelogs")
        input()
            
    except Exception:
        print("An Error has occured: ")
        print(traceback.format_exc())
    