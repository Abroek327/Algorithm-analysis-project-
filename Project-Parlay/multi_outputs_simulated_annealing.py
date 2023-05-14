import random
import math
from configurations import configurations
from helper import helper
import copy

#References
#https://www.researchgate.net/publication/227061666_Computing_the_Initial_Temperature_of_Simulated_Annealing#:~:text=The%20classical%20version%20of%20simulated,with%20a%20given%20acceptance%20ratio.
#http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/

class outputs_SA():
    parlaysOutput = 0
    threshold = 0.03
    thresholdMod = 0.8

    def getThresh():
        return outputs_SA.threshold

    #Simulated Annueling Algorithm that finds best configuration from a set of total outputs
    def outputs_simulated_annealing(initial_config, allOutputsList, bestConfigurationsList, temp_threshold=0.03):
        outputs_SA.parlaysOutput += 1
        current_config = initial_config
        best_config = initial_config
        temperature = 100
        temperature_init = temperature
        countIter = 0
        bestConfigurationsList
        
        outputs_SA.threshold = temp_threshold

        for i in range(outputs_SA.parlaysOutput):
            outputs_SA.threshold *= outputs_SA.thresholdMod

        #While the current temperature is above the threshhold, it will keep the simulated annealing running
        while (temperature > (outputs_SA.threshold)):
            neighbor_config = outputs_SA.get_neighbor(current_config, allOutputsList)
            current_value = current_config.value
            neighbor_value = neighbor_config.value

            #Evaluates neighbor against current state
            if (neighbor_value > current_value):
                current_config = neighbor_config
                #Best state found so far if neighbor is best
                if (neighbor_value > best_config.value):
                    potential_best_exists = False
                    
                    #Adds functionality for multi-output parlay
                    #Compared best parlay found to already listed parlays to avoid repeats
                    #Finds best grouping
                    for existingBestConfig in bestConfigurationsList:
                        if(configurations.equals(neighbor_config, existingBestConfig)):
                            potential_best_exists = True
                    #Checks if best exists 
                    if(potential_best_exists):
                        pass
                    else:
                        best_config = neighbor_config

            else:
                #Determines if neighbor state should still be acccpeted if value is lower than current state
                delta_value = (current_value - neighbor_value)
                acceptance_probability = math.exp(-delta_value / temperature)

                if (random.uniform(0, 1) < acceptance_probability):
                    current_config = neighbor_config
            #Cooling Schedule (Linear)
            temperature = temperature_init / (1 + (3 *countIter))
            countIter += 1

        return configurations(best_config.outcomeList)


    # Generate a random 'neighbor' of the current config
    # Configs are 'Neighbors if they only differ by one output
    def get_neighbor(config, allOutputsList):
        

        neighborOutcomeList = []
        cOutputList = copy.deepcopy(config.outcomeList)
        localAllOutputs = copy.deepcopy(allOutputsList)
        breakout = False

        #checks to see if a smaller neighbor exists
        if(len(cOutputList) > 0):

            rand = random.randint(0,10)
        else:
            rand = 5

        #slight bias towards building bigger parlays to avoid initial backtracking
        if (rand > 4):
            #Generate Larger neighbor
            count = 0

            while(True):
                #generates list of the gameID's of the outputs in the current config's outPutList
                #[*cOutputList, 'e']
                if (len(localAllOutputs) > 1):
                    randomIndex = random.randint(0,len(localAllOutputs) - 1)
                else:
                    randomIndex = 0
                    breakout = True

                potentialNeighborOptList = [*cOutputList,localAllOutputs[randomIndex]]
                gameIDs = helper.gameIDs(potentialNeighborOptList)


                if((len(gameIDs) == len(set(gameIDs)))):
                    break
                elif(breakout):
                    potentialNeighborOptList.pop()
                    break
                else:
                    del localAllOutputs[randomIndex]

            neighborOutcomeList = potentialNeighborOptList


        else:
            #generate smaller neighbor
            ri = random.randint(0,len(cOutputList)-1)
            del cOutputList[ri]

            neighborOutcomeList = cOutputList


        return configurations(neighborOutcomeList)


