import random
import math
import itertools
from prettytable import PrettyTable

def generateAllConfigStructures(binSize):
    pass


# #Generates all unique combination of elements in set up to set size 'r'
#     for numOutcomesPool in range(numOutcomesPool, 0, -1):
#         #TODO: May need to check if this is most efficient way to generate all combinations
#         #TODO: Needs to use Delayed Column Generation Via Knapsack algorithm or other comination set approximation algorithm if total set of combinations is too large to be practical to generate quickly

#         perm = list(itertools.combinations(outcomesList, numOutcomesPool))

#         #TODO: Needs to utilize SQL insert to store configurations instead of list
#         for i in perm:
#             gameIDs = helper.gameIDs(i)

#             #TODO: the if-statement in this for-loop checks the list for multiple outcomes with duplicate gameIDs (Which would make it impossible for both outcomes to occur), we need to research if there is a more efficient way to do this
#             if(len(gameIDs) == len(set(gameIDs))):
                  
#                 x = configurations(i, Id)
#                 allConfigs.append(x)
#                 Id += 1

#     #TODO: Needs to pull from SQL Database instead of list before printing
#     helper.config_print(allConfigs)