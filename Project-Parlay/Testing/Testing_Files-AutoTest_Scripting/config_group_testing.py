from helper_testing import helper
from configurations_testing import configurations
import copy


class configGroup:
    cgID = 0

    def configGroupID():
        configGroup.cgID += 1

        return configGroup.cgID
    
    def value(cG):
        sumValues = 0

        for x in cG.configList:
            sumValues += x.value

        return sumValues
    
    def aveSize(configGroup):
        size = 0

        for config in configGroup:
            size += config.numOutcomes
        
        aveSize = size / len(configGroup)

        return aveSize
            
    
    #returns number of shared configs in two config groups
    @staticmethod
    def crossover(configGroupA, configGroupB):
        combinedList = []
        combinedList.extend(configGroupA.configList)
        combinedList.extend(configGroupB.configList)
        remainderListA = copy.deepcopy(configGroupA.configList)
        remainderListB = copy.deepcopy(configGroupB.configList)
        combinedSet = []
        duplicates = []

        for item in combinedList:
            present = False

            for config in combinedSet:

                if configurations.equals(item, config):
                    present = True
                    break
                
            if(not present):
                combinedSet.append(item)
            else: 
                duplicates.append(item)

        Crossover = len(combinedList) - len(combinedSet)

        for element in duplicates:

            for i in range(len(remainderListA)-1):
                
                if(configurations.equals(remainderListA[i], element)):
                    del remainderListA[i]
            
            for j in range(len(remainderListB)-1):
                if(configurations.equals(remainderListB[j], element)):
                    del remainderListB[j]
                

        return Crossover, duplicates, remainderListA , remainderListB

    def __init__(self, configList):
        self.numConfigs = len(configList)
        self.cgID = configGroup.configGroupID()
        self.configList = configList
        self.profitChance = "Not Yet Assigned"
        self.theoreticalProfit = "Not Yet Assigned"
        self.AmericanOdds = "Not Yet Assigned"
        self.ImpliedProbability = "Not Yet Assigned"
        self.decimalOdds = "Not Yet Assigned"
        #TODO: Needs to have attribute 'value' that represents parlay quality
        # 'value' will be attribute maximized by simulated annueling
        self.value = configGroup.value(self)
