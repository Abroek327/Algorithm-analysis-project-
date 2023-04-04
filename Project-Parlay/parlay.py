from helper import helper
from db_operations import db_operations
from configurations import configurations
from game import game
import itertools
from prettytable import PrettyTable

db_ops = db_operations("allGameHistory.db")
allConfigs = []
bestConfigs = []

def startScreen():
    print("Welcome to your Project Parlay!")


def search_by_year():
       year=input("Enter the last two digits of the year you'd like to see data for: ")
       #query="SELECT * FROM NFLHistory WHERE schedule_date LIKE '%/"+year+"'"
       query="SELECT * FROM NFLHistory WHERE schedule_date LIKE '%" +1/15/67+"'"

       print(db_ops.simple_query(query))
      # helper.pretty_print(results)
    
def search_by_games():
    #get a list of all artists
    query = '''
    SELECT game_id, team_home, team_away, winning_team
    FROM NFLHistory
    GROUP BY game_id;
    '''

    print("Games in database: ")
    dictionary = {}
    games = db_ops.name_placeholder_query2(query, dictionary)
    
    #commenting out for lack of relevence to project; delete later
    '''
    #show all artists an create a dictionary of choices
    choices = {}
    for i in range(len(games)):
        print(i, games[i])
        choices[i] = games[i]
    index = helper.get_choice(choices.keys())

    print("How many songs do you want returned for "+choices[index]+"?")
    print("Enter 1, 5 or 0 for all songs")
    num = helper.get_choice([1,5,0])

    '''
 
    #print results
    
  #  query = '''
   # SELECT DISTINCT name
   # FROM songs
   # WHERE Artist =:artist
   # ORDER BY RANDOM()
   # '''
    
   
    #run query for songs and print results
    '''
    dictionary = {"artist":choices[index]}
    if num != 0:
        query += "LIMIT:lim"
        dictionary["lim"] = num
    results = db_ops.name_placeholder_query(query, dictionary)
    helper.pretty_print(results)
    '''
def calculateWinP(spread):
    percent = (-.0303*spread) + .50
    if(percent > .99):
          return .99
    else:
          return percent
    
def permutations(numGamesPool, gameList):
    query = '''
    SELECT DISTINCT team_home
    FROM NFLHistory
    '''

    dictionary = {}
    games = db_ops.name_placeholder_query2(query, dictionary)
    #list1 = ["a", "b", "c", "x", "y", "z"]

    r = numGamesPool
    
    print("\nYour Options..\n")
    Id = 0

    #Generates all unique combination of elements in set up to set size 'r'
    for r in range(r, 0, -1):
        #TODO: May need to check if this is most efficient way to generate all combinations
        #TODO: Needs to use Delayed Column Generation Via Knapsack algorithm or other comination set approximation algorithm if total set of combinations is too large to be practical to generate quickly

        perm = list(itertools.combinations(gameList, r))

        #TODO: Needs to utilize SQL insert to store configurations instead of list
        for i in perm:
            x = configurations(i, Id)
            allConfigs.append(x)
            Id += 1

    #TODO: Needs to pull from SQL Database instead of list before printing
    helper.config_print(allConfigs)


#TODO: Needs to pull from SQL Database instead of list of configs
#TODO: Needs to evaluate based on (potential profit)/(risk) ratio, currently calculates on lowest risk only
#TODO: Needs to use simulated annueling to approximate best configs when total set of configs is too large to be practical
#TODO: Needs to find a generalized way to find relative potential profit from a configuration before we assign a share of capital to it (Maybe Average?)
#TODO: Needs to use stock cutting algorithm to find final most optimal grouping from set of "best parlays" to fit user specifications
def bestConfig(configList):
      

    while len(bestConfigs) < numParlays:
        maxProfitChance = 0
        best = 0

        for x in configList:

            if x.profitChance > maxProfitChance:
                
                maxProfitChance = x.profitChance
                best = x

        if best not in bestConfigs:
    
            bestConfigs.append(best)
            configList.remove(best)
    
    print("\n Best Parlays to Bet:\n")
    helper.config_print(bestConfigs)
    

    
#Main Program
startScreen()
#permutations()
#print statement unnessary
#print(calculateWinP(-11))

#search_by_year() WIP

#TODO: Program should calculate how many parlays would be optimal to use, instead of asking for user input
# An Idea for that is to use simulated annueling again on possible sets of best parlays looking to maximize "Total Value" (refrencing 'value' attribute of configuration obj)
#TODO: Each configuration group needs to keep track of its 'string factor'
#String factor refers to when one instance of a team winning is included in multiple configurations
#By the nature of parlays, including the same pick in multiple configurations in the same grouping would make it liable for the entire grouping to fail with a single unexpected loss
#Therefore a high "String Factor" would increase the total risk for the grouping, but shouldn't neccicarily be a dealbreaker if stringing a pick adequately improves total profit possibility
numParlays = input("How many parlays would you like to bet on?")
while numParlays.isdigit() == False:
            print("Number of games must be a number. Try again")
            numParlays = input("How many games would you like to bet on?")
numGamesPool = input("From How many games would you like us to consider before we calculate best?")
while numGamesPool.isdigit() == False:
            print("Number of games to consider must be a number. Try again")
            numGamesPool = input("From How many games would you like us to consider before we calculate best?")
numCapital = input("How much capital would you like to bet($)?")
while numCapital.isdigit() == False:
            print("Captial must be a number. Try again")
            numCapital = input("How much capital would you like to bet($)?")

numParlays = int(numParlays)
numCapital = int(numCapital)
numGamesPool = int(numGamesPool)
gameList =[]

for x in range(numGamesPool):
    gameX = game("f","u", 0.5)
    gameX.favoredTeam = input("Please Enter The Favored Team for game " + str(x) + ": ")
    gameX.underdog = input("Please Enter The Underdog for game " + str(x) + ": ")
    gameX.favWinP = int(input("Please enter the win percentage chance for the favored team: "))
    gameList.append(gameX)
    


permutations(numGamesPool, gameList)
bestConfig(allConfigs)
# search_by_games()


#deconstruct at end
db_ops.destructor()


#TODO: Need to design and Implement simple, clean, dynamic, colorful, interactive, web-based, easilly accessable with an internet connection, UI
#TODO: UI should have live parlay tracker feature with good visual design that tracks the state of each leg of a parlay (W,L, Yet To Start, Ongoing)
#If leg is a 'Win' that leg should light up green
#If leg is a 'Loss" whole parlay should light up red
#If All legs in parlay are a 'Win' then whole parlay should turn gold
#While Parlay has legs in either the 'Yet to start' or 'Ongoing' states, it should give a live percentage chance of that parlay hitting
#While Parlay grouping has parlays with legs in either the 'Yet to start' or 'Ongoing' states, it should give a live 'Max potential Win' and a percentage chance of it happening, it should also give a 'Most likely potential win' and a percentage chance of that happening as well
#TODO: UI should have a 'test and learn' tab where a user can enter a user made custom parlay and the algorithm will give it a score out of 10 on how good it is, as well as othr addition stats used for evaluating our own parlays
#TODO: UI should have option to generate 'Best Bet of the day' where it generates the most optimal parlay of games that are being played that day
#TODO: Computer Generate Additional SQL Database that contains 'Theoretical Games' where win percentages and odds are randomly generated, and outcomes are randomly generated based on those win percentages, for aditional testing
#TODO: Complete SQL database of NFL games up until current (Past games are subject to different rule changes and a different style of play, but still useful)
#TODO: Create SQL Database of stats for 'average parlay bettors' as well as 'Pro parlay bettors' to compare against algorithm for effectiveness
#TODO: UI should present user with three different options for parlay groupings to choose from: (High Profit/High Risk), (Optimal), (Lowest Risk)
#High and low risk options should still be relatively optimal
#TODO: Create a linear regression model to test if most profitable parlay groupings will always be profitable in a wide variety of contexts
#Stats for bettors could include (Profitable bet percentage), (Average amount of profit), as well as all stats we use to evaluate our own parlays and parlay groupings
#UI should have click and scrollable 'Input' from a list of web-scraped, upcoming games and bets to save user from wasting time entering data manually
#TODO: Need to implement web scraper to feed live/soon games to UI for easy user selection by click
#TODO:Need to be able to work with 'correlated parlays' as well, and their boosted odds (Ex: Patriots Win + Tom Brady Scores 2 Touchdowns + Patriots Defence allows less than 10 points)
#A decent amount of online betting services do not allow correlated parlays, so there needs to be an option to have the program aviod corredlated parlays as well
#User would have to indicate which bets are directly correlated and give a guess at how correlated they are
#It would be better to avoid additional user input for correlation strength, we could use web scraping to find bets then calculate correlation ourselves using mathematical means
#TODO: Need to create object to hold possible groupings of best parlays, should have the following attributes for later analysis: (Average number of legs in each parlay), (String Factor), (Number of parlays), (Total Value), (Max Profit Possible), (Average Profit Possible), (Percent Chance of profit occuring at all), 
#TODO: Program should calculate how many parlays would be optimal to use in final grouping, instead of asking for user input
# An Idea for that is to use simulated annueling again on possible sets of best parlays looking to maximize "Total Value" (refrencing 'value' attribute of configuration obj), we should also consider a historical factor when calculating "Total Value" so that backtesting with SQL database can be
#TODO: Each configuration group needs to keep track of its 'string factor'
#String factor refers to when one instance of a team winning is included in multiple configurations
#By the nature of parlays, including the same pick in multiple configurations in the same grouping would make it liable for the entire grouping to fail with a single unexpected loss
#Therefore a high "String Factor" would increase the total risk for the grouping, but shouldn't neccicarily be a dealbreaker if stringing a pick adequately improves total profit possibility
    