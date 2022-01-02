from resources import *

##Keynames

class Trainer:
    
    def __init__(self, trainer):
        
        self.pokemon = []
        
        for pokeNum in range(1, 7):
            
            pokemonKeys = []
            pokemonIndexes = []
            
            for key in trainer.keys():
                if "P"f"{pokeNum}" in key:
                    pokemonKeys.append(key.replace("P"f"{pokeNum}", ""))
                    pokemonIndexes.append(trainer[key])
                    
            pokemon = dict(zip(pokemonKeys, pokemonIndexes))
            self.pokemon.append(Pokemon(pokemon, pokeNum))
        
    def getPokemonList(self):
        return self.pokemon
    
    def getShowdown(self):
        
        pokeString = ""
        
        for pokemon in self.pokemon:
            pokeString += pokemon.getShowdownFormat()
            
        return pokeString
        
        
        
        
class Pokemon:
    
    monsnoKey = "MonsNo"
    formnoKey = "FormNo"
    shinyKey = "IsRare"
    levelKey = "Level"
    genderKey = "Sex"
    natureKey = "Seikaku"
    abilityKey = "Tokusei"
    moveKey = "Waza"
    moveNums = ["1", "2", "3", "4"]
    itemKey = "Item"
    ballKey = "Ball"
    sealKey = "Seal"
    IVbaseKey = "Talent"
    EVbaseKey = "Effort"
    hp = "HP"
    attack = "Atk"
    specialAttack = "SpA"
    defense = "Def"
    specialDefense = "SpD"
    speed = "Spe"
    
    japaneseStatList = searchLists.japaneseStatList
    showdownStatList = searchLists.showdownStatList
    
    none = "Null"
    
    def __init__(self, pokemon, pokeNum):
        
        self.pokeNum = pokeNum
        
        self.monsno = pokemon[self.monsnoKey]
        self.formno = pokemon[self.formnoKey]
        self.shiny = pokemon[self.shinyKey]
        self.level = pokemon[self.levelKey]
        self.gender = pokemon[self.genderKey]
        self.nature = pokemon[self.natureKey]
        self.ability = pokemon[self.abilityKey]
        self.item = pokemon[self.itemKey]
        self.ball = pokemon[self.ballKey]
        self.seal = pokemon[self.sealKey]
        
        ##Moves, IVs, EVs are acquired through iteration
        
        self.moveList = []
        for moveNum in self.moveNums:
            self.moveList.append(pokemon[f"{self.moveKey}{moveNum}"])
            
            
        self.IVDic = {}
        self.EVDic = {}
        for i in range(len(self.japaneseStatList)):
            japaneseStat = self.japaneseStatList[i]
            showdownStat = self.showdownStatList[i]
            
            self.IVDic[showdownStat] = pokemon[f"{self.IVbaseKey}{japaneseStat}"]
            self.EVDic[showdownStat] = pokemon[f"{self.EVbaseKey}{japaneseStat}"]
        
    def getPokeName(self):
        return getName(self.monsno, self.formno)
    
    def getShiny(self):
        return self.shiny == 1
    
    def getLevel(self):
        return self.level
    
    def getGender(self):
        return getGender(self.gender)
    
    def getNature(self):
        return getNature(self.nature)
    
    def getAbility(self):
        return getAbility(self.ability)
    
    def getItem(self):
        return getItem(self.item)
    
    def getBall(self):
        return self.ball
    
    def getSeal(self):
        return self.seal
    
    def getFormNo(self):
        return self.formno
    
    def getMove1(self):
        return getMove(self.moveList[0])
    
    def getMove2(self):
        return getMove(self.moveList[1])
    
    def getMove3(self):
        return getMove(self.moveList[2])
    
    def getMove4(self):
        return getMove(self.moveList[3])
    
    def getMoveList(self):
        
        moveList = []
        
        for move in self.moveList:
            if move > 0:
                moveList.append(getMove(move))
            
        return moveList

    
    def getShowdownFormat(self, omitZero=True):
        pokeString = ""
        # print(dic["P"f"{pokeNum}Level"])
        level = self.level
        if level > 0:
            # Pokemon Showdown Format
            # PokemonName (Gender) @ HeldItem
            # Ability: AbilityName
            # Level: Level
            # Shiny: Y/N
            # EVs: x Hp / x Atk / etc.
            # NatureName Nature
            # IVs: x Hp / x Atk / etc.
            # - Move1
            # - Move2
            # - Move3
            # - Move4
            monsno = self.getPokeName()
            gender = self.getGender()
            if self.item > 0:
                item = "@ " + self.getItem()
                
            else:
                item = ""
            
            ability = self.getAbility()
            level = str(level)
            
            nature = self.getNature()
            
            pokeString += monsno
            pokeString += gender
            pokeString += item + "\n" #\n is newline
            
            pokeString += "Ability: " + ability + "\n"
            
            pokeString += "Level: " + level + "\n"
            
            if list(self.EVDic.values()).count(0) != len(self.EVDic.values()): ##If all values are not
                pokeString += "EVs: "
                for ev in self.EVDic.keys():
                    val = self.EVDic[ev]
                    if val == 0 and omitZero:
                        pass
                    else:
                        pokeString += "{} {} / ".format(ev, val)
                pokeString = pokeString[:-2] #Removes the extra backslash
                pokeString += "\n"
            
            pokeString += nature + " Nature\n"
            
            if list(self.IVDic.values()).count(0) != len(self.IVDic.values()): ##If all values are not
                pokeString += "IVs: "
                for iv in self.IVDic.keys():
                    val = self.IVDic[iv]
                    if val == 0 and omitZero:
                        pass
                    else:
                        pokeString += "{} {} / ".format(iv, val)
                pokeString = pokeString[:-2] #Removes the extra backslash
                pokeString += "\n"
            
            for move in self.getMoveList():
                pokeString += "- " + move + "\n"
                
            pokeString += "\n"

        return pokeString
    
    def __str__(self):
        return(self.getShowdownFormat())



    