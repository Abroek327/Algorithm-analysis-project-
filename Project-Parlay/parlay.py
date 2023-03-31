from helper import helper
from db_operations import db_operations

db_ops = db_operations("allGameHistory.db")

def startScreen():
    print("Welcome to your Project Parlay!")

#returns 0 if there are no entries in table
def is_empty():
    query = '''
    SELECT COUNT(*)
    FROM NFLHistory;
    '''
    result = db_ops.single_record(query)
    return result == 0
    
def search_by_artist():
    #get a list of all artists
    query = '''
    SELECT DISTINCT game_id, team_home, team_away, winning_team
    FROM NFLHistory;
    '''

    print("Games in playlist: ")
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


    
#Main Program
startScreen()
search_by_artist()


#deconstruct at end
db_ops.destructor()