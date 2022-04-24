##This only generates a changelog for trainer pokemon using my Showdown Converter

from os import path
import sys
import UnityPy
from resources import *
import showdown

originalPath = "Original/masterdatas"
editedPath = "Edited/masterdatas"
changelogPath = "Changelogs/Trainer Changelog.txt"

TrainerTablePathID = 676024375065692598

pathIDList = [TrainerTablePathID]

compareList = ["TrainerPoke"]
trainerDataKey = "TrainerData"

idKey = 'ID' ##Used to get pokemon id, as it's named differently in different files
    
def exists(src):
    return path.exists(src)

def getUnityTrees(unityfile, pathIDs = pathIDList):
    
    treeList = []

    for obj in unityfile.objects:
        if obj.path_id in pathIDs:
            treeList.append(obj.read_typetree())
    
    return treeList
    
def main():
    changelogWrite = open(changelogPath, "wt", encoding="utf8")
    
    original = UnityPy.load(originalPath)
    edited = UnityPy.load(editedPath)
    
    originalTrees = getUnityTrees(original)[0]
    editedTrees = getUnityTrees(edited)[0]
    
    generatedTrainerList = getIfGeneratedTrainers()
    
    typeList = []
    
    if generatedTrainerList:
        for trainerType in editedTrees["TrainerType"]:
            typeList.append(trainerType["LabelTrType"])
    
    for compareKey in compareList:
        trainerTableOriginal = originalTrees[compareKey]
        trainerTableEdited = editedTrees[compareKey]
        trainerDataEdited = editedTrees[trainerDataKey]
        
        minLength = min(len(trainerTableEdited), len(trainerTableOriginal))
        
        # for i in range(minLength):
        #     changelogWrite.write("========================================\n")
            
        #     trainerOriginal = trainerTableOriginal[i]
        #     trainerEdited = trainerTableEdited[i]
        #     trainerData = trainerDataEdited[i]
            
        #     if trainerOriginal != trainerEdited:
        #         if generatedTrainerList:
        #             type = typeList[trainerData["TypeID"]]
        #             name = trainerData["NameLabel"]
        #             fullName = getTrainerNameFromTypes(name, type)
        #             changelogWrite.write(f"{fullName} ID{trainerEdited[idKey]}\n")
                
        #         else:
        #             changelogWrite.write(f"{getTrainerName(trainerOriginal[idKey])} "f"ID{trainerOriginal[idKey]}: \n")
                
        #         unchanged = False
            
        #     else:
        #         unchanged = True ##Used to add pokemon name if there are changes
                        
        #     if not unchanged: ##If there are changes with any of the functions
        #         originalTrainerClass = showdown.Trainer(trainerOriginal)
        #         editedTrainerClass = showdown.Trainer(trainerEdited)
                
        #         # changelogWrite.write("OLD: \n")
        #         # changelogWrite.write(originalTrainerClass.getShowdown())
        #         changelogWrite.write("NEW: \n")
        #         changelogWrite.write(editedTrainerClass.getShowdown())
                
        #     else:
                
        #         if devMode:
                    
        #             if generatedTrainerList:
        #                 type = typeList[trainerData["TypeID"]]
        #                 name = trainerData["NameLabel"]
        #                 fullName = getTrainerNameFromTypes(name, type)
        #                 changelogWrite.write(f"{fullName} ID{trainerEdited[idKey]}\n")
        #             else:
        #                 changelogWrite.write(f"{getTrainerName(trainerOriginal[idKey])} "f"ID{trainerOriginal[idKey]}: \n")
                    
        #             changelogWrite.write("Unchanged\n")
        #             changelogWrite.write("\n")
                    
        if len(trainerTableEdited) > len(trainerTableOriginal):
            for i in range(len(trainerTableEdited)):
                
                trainerEdited = trainerTableEdited[i]
                trainerData = trainerDataEdited[i]
                
                ##Removes Volkner
                if trainerData["TypeID"] == 83 and i > 707:
                    continue
                         
                else:
                    
                    changelogWrite.write("========================================\n")
                    
                    if generatedTrainerList:
                        type = typeList[trainerData["TypeID"]]
                        name = trainerData["NameLabel"]
                        fullName = getTrainerNameFromTypes(name, type)
                        changelogWrite.write(f"{fullName} ID{i}\n")
                    
                    else:
                        changelogWrite.write(f"{getTrainerName(trainerEdited[i])} ID{trainerEdited[i]}: \n")
                    
                    editedTrainerClass = showdown.Trainer(trainerEdited)
                    
                    # changelogWrite.write("ADDED: \n")
                    changelogWrite.write(editedTrainerClass.getShowdown())
                
            else:
                
                if devMode:
                    
                    if generatedTrainerList:
                        type = typeList[trainerData["TypeID"]]
                        name = trainerData["NameLabel"]
                        fullName = getTrainerNameFromTypes(name, type)
                        changelogWrite.write(f"{fullName} ID{trainerEdited[idKey]}\n")
                    else:
                        changelogWrite.write(f"{getTrainerName(trainerEdited[idKey])} "f"ID{trainerEdited[idKey]}: \n")
                    changelogWrite.write("Unchanged\n")
                    changelogWrite.write("\n")
            
                    

if __name__ == '__main__':
    
    main()