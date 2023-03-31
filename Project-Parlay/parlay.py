from helper import helper
from db_operations import db_operations
import itertools

db_ops = db_operations("allGameHistory.db")

def startScreen():
    print("Welcome to your Project Parlay!")
    
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
    
    #show all artists an create a dictionary of choices
    choices = {}
    for i in range(len(games)):
        print(i, games[i])
        choices[i] = games[i]
    index = helper.get_choice(choices.keys())

    print("How many songs do you want returned for "+choices[index]+"?")
    print("Enter 1, 5 or 0 for all songs")
    num = helper.get_choice([1,5,0])

    #print results
    query = '''
    SELECT DISTINCT name
    FROM songs
    WHERE Artist =:artist
    ORDER BY RANDOM()
    '''

    #run query for songs and print results
    dictionary = {"artist":choices[index]}
    if num != 0:
        query += "LIMIT:lim"
        dictionary["lim"] = num
    results = db_ops.name_placeholder_query(query, dictionary)
    helper.pretty_print(results)

def calculateWinP(spread):
    percent = (-.0303*spread) + .50
    if(percent > .99):
          return .99
    else:
          return percent
    
def permutations():
    query = '''
    SELECT DISTINCT team_home
    FROM NFLHistory
    '''

    dictionary = {}
    games = db_ops.name_placeholder_query2(query, dictionary)
    list1 = ["a", "b", "c", "x", "y", "z"]
    r = 2
    perm = list(itertools.permutations(games, r))
    helper.pretty_print(perm)

    
#Main Program
startScreen()
permutations()

print(calculateWinP(-11))


numGames = input("How many games would you like to bet on?")
while numGames.isdigit() == False:
            print("Number of games must be a number. Try again")
            numCapital = input("How many games would you like to bet on?")
numCapital = input("How much capital would you like to bet($)?")
while numCapital.isdigit() == False:
            print("Captial must be a number. Try again")
            numCapital = input("How much capital would you like to bet($)?")



search_by_games()


#deconstruct at end
db_ops.destructor()