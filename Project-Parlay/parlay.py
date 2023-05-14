from helper import helper
from db_operations import db_operations
from configurations import configurations
from outcome import outcome
from game import game
import itertools

from prettytable import PrettyTable

from multi_outputs_simulated_annealing import outputs_SA




db_ops = db_operations("allGameHistory.db")
allConfigs = []
bestConfigsBF = []
bestConfigsSA = []




def startScreen():
    message = "Welcome to your Project Parlay!"


#Calculates Win Percentage based on Research Algorithm
def calculateWinP(spread):
    percent = (-.0303*spread) + .50
    if(percent > .99):
          return .99
    else:
          return percent

    
#Finds all the possible combination based on pool of games
def permutations(numGamesPool, outcomesList):
    query = '''
    SELECT DISTINCT team_home
    FROM NFLHistory
    '''
    dictionary = {}
    games = db_ops.name_placeholder_query2(query, dictionary)
    numOutcomesPool = 2 * numGamesPool
    print("\nYour Options..\n")
    #Generates all unique combination of elements in set up to set size numOutcomesPool
    for numOutcomesPool in range(numOutcomesPool, 0, -1):
        perm = list(itertools.combinations(outcomesList, numOutcomesPool))
        for i in perm:
            gameIDs = helper.gameIDs(i)

            if(len(gameIDs) == len(set(gameIDs))):
                  
                x = configurations(i)
                allConfigs.append(x)
    helper.config_print(allConfigs)



#Finds a generalized way to find relative potential profit from a configuration before we assign a share of capital to it
def bestConfig(configList,outcomeList):
    #Brute force evaluate all configs and then select best ones:
    while len(bestConfigsBF) < numParlays:
        maxValue = 0
        best = 0
        for x in configList:
            if x.value > maxValue: 
                maxValue = x.value
                best = x
        if best not in bestConfigsBF:
            bestConfigsBF.append(best)
            configList.remove(best)

    #Dynamic best config finder using simulated annueling
    configX = configurations([])
    bestConfigsSA = []

    while len(bestConfigsSA) < numParlays:
        bestConfigsSA.append(outputs_SA.outputs_simulated_annealing(configX, outcomeList, bestConfigsSA))

    bestConfigs_BF = configurations.sort(bestConfigsBF)
    bestConfigs_SA = configurations.sort(bestConfigsSA)

    print("\n Best Parlays to Bet (BF):\n")
    helper.config_print(bestConfigs_BF)

    print("\n Best Parlays to Bet (SA):\n")
    helper.config_print(bestConfigs_SA)

    numSameConfigs = 0
    for config in bestConfigsBF:
          for parlay in bestConfigsSA:
                if (configurations.equals(config,parlay)):
                      numSameConfigs += 1
        
    print("\n Num Parlays: " + str(numParlays) + "\n Num Shared: " + str(numSameConfigs))
          
    

    
#Main Program
startScreen()


numParlays = input("How many parlays would you like to bet on?")
while numParlays.isdigit() == False:
            print("Number of games must be a number. Try again")
            numParlays = input("How many games would you like to bet on?")
numGamesPool = input("From How many games would you like us to consider before we calculate best?")
while numGamesPool.isdigit() == False:
            print("Number of games to consider must be a number. Try again")
            numGamesPool = input("From How many games would you like us to consider before we calculate best?")
totalUserCapital = input("How much capital would you like to bet($)?")
while totalUserCapital.isdigit() == False:
            print("Captial must be a number. Try again")
            totalUserCapital = input("How much capital would you like to bet($)?")

numParlays = int(numParlays)
totalUserCapital = int(totalUserCapital)
numGamesPool = int(numGamesPool)
gameList = []
outcomeList = []

#initializes all game objects from user input, and thus al outcome objecs are internally initialized inside the game initialization function
for x in range(numGamesPool):
    favoredTeam = input("Please Enter The Favored Team for game " + str(x) + ": ")
    underdog = input("Please Enter The Underdog for game " + str(x) + ": ")

    favoredWinP = int(input("Please enter the win percentage chance for the favored team: "))
    while favoredWinP < 50:
            print("Favored Win Percentage must be 50 or higher. Try again")
            favoredWinP = int(input("Please enter the win percentage chance for the favored team: "))

    gameX = game(favoredTeam, underdog, favoredWinP, x)
    gameList.append(gameX)

for gameInstance in gameList:
    outcomeList.extend(gameInstance.outcomes)
    


permutations(numGamesPool, outcomeList)
bestConfig(allConfigs, outcomeList)

#deconstruct at end
db_ops.destructor()

