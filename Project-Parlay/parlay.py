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

    for r in range(r, 0, -1):
        perm = list(itertools.combinations(gameList, r))

        for i in perm:
            x = configurations(i, Id)
            allConfigs.append(x)
            Id += 1
            
    helper.config_print(allConfigs)

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
