from helper import helper
from db_operations import db_operations

db_ops = db_operations("allGameHistory.db")

def startScreen():
    print("Welcome to your playlist!")

#returns 0 if there are no entries in table
def is_empty():
    query = '''
    SELECT COUNT(*)
    FROM songs;
    '''
    result = db_ops.single_record(query)
    return result == 0

#fills songs table if it is empty
def pre_process():
    if is_empty():
        attribute_count = len(data[0])
        placeholders = ("?,"*attribute_count)[:-1]
        query = "INSERT INTO songs VALUES("+placeholders+")"
        db_ops.bulk_insert(query, data)
    
    #Ask User if they want to load new data into the database
    print('''Would you like to load new songs into the database?
    1. YES
    2. NO
    ''')
    user_choice = helper.get_choice([1,2])
    if user_choice == 1:
        filePath = input("Please enter the path to the file:")
        #cleans path and inserts into the database
        data1 = helper.data_cleaner(filePath)
        attribute_count = len(data1[0])
        placeholders = ("?,"*attribute_count)[:-1]
        query = "INSERT INTO songs VALUES("+placeholders+")"
        db_ops.bulk_insert(query, data1)
        print("Database Updated")
    if user_choice == 2:
        print("NO")

def options():
    print('''Select from the following menu options
    1. Find songs by artists
    2. Find songs by genre
    3. Find songs by feature
    4. Update Song
    5. Delete Song
    6. Exit
    ''')
    return helper.get_choice([1,2,3,4,5,6])

#function to search songs table by artist
def search_by_artist():
    #get a list of all artists
    query = '''
    SELECT DISTINCT Artist
    FROM songs;
    '''

    print("Artists in playlist: ")
    artists = db_ops.single_attribute(query)
    
    #show all artists an create a dictionary of choices
    choices = {}
    for i in range(len(artists)):
        print(i, artists[i])
        choices[i] = artists[i]
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


def search_by_genre():
    #get a list of all genres
    query = '''
    SELECT DISTINCT Genre
    FROM songs;
    '''

    print("Genres in playlist: ")
    genres = db_ops.single_attribute(query)
    
    #show all genres and create a dictionary of choices
    choices = {}
    for i in range(len(genres)):
        print(i, genres[i])
        choices[i] = genres[i]
    index = helper.get_choice(choices.keys())

    print("How many songs do you want returned for "+choices[index]+"?")
    print("Enter 1, 5 or 0 for all songs")
    num = helper.get_choice([1,5,0])

    #print results
    query = '''
    SELECT DISTINCT name
    FROM songs
    WHERE Genre =:genre
    ORDER BY RANDOM()
    '''

    #run query for songs and print results
    dictionary = {"genre":choices[index]}
    if num != 0:
        query += "LIMIT:lim"
        dictionary["lim"] = num
    results = db_ops.name_placeholder_query(query, dictionary)
    helper.pretty_print(results)

def search_by_feature():
    #features we want to search for
    features = ['Danceability', 'Liveness', 'Loudness']
    choices = {}

    #show features in table and create dictionary
    for i in range(len(features)):
        print(i, features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())


    print("How many songs do you want returned for "+choices[index]+"?")
    print("Enter 1, 5 or 0 for all songs")
    num = helper.get_choice([1,5,0])

    #get what order we want results shown in
    print("Do you want results sorted in ASC or DESC order?")
    order = input("ASC or DESC: ")

    #print our results
    query = '''
    SELECT DISTINCT name
    FROM songs
    ORDER BY
    ''' + choices[index]+" "+order

    dictionary = {}
    if num != 0:
        query += " LIMIT:lim"
        dictionary["lim"] = num
    results = db_ops.name_placeholder_query(query, dictionary)
    helper.pretty_print(results)

def update_song():
    updateSong = input("Please enter the name of the song you would like to update: ")

    query1 = '''
    SELECT songID
    FROM songs
    WHERE Name =:updateSong
    '''

    dictionary = {"updateSong":updateSong}
    songID = db_ops.name_placeholder_query(query1, dictionary)


    while (not songID): #check if song exists
        updateSong = input("Song does not exist. Try again:")
        query2 = '''
        SELECT songID
        FROM songs
        WHERE Name =:songName
        '''
        dictionary = {"songName":updateSong}
        songID = db_ops.name_placeholder_query(query2, dictionary)
    songID = songID[0][0]

    #get new feature values
    print("Here are the current attributes for "+updateSong+ ":")
    query3 = '''
    SELECT Name, Album, Artist, releaseDate, Explicit
    FROM songs
    WHERE songID =:songID
    '''
    dictionary["songID"] = songID
    results = db_ops.name_placeholder_query(query3, dictionary)
    helper.pretty_print(results)
    print('''Select which attribute to update: 
    1. Name
    2. Album
    3. Artist
    4. releaseDate
    5. Explicit''')
    attributeToChange = helper.get_choice([1,2,3,4,5])
    new_value = input("Enter the new value for the attribute: ")
    query4 = '''
    UPDATE songs
    '''


    if attributeToChange == 1:  #update name
        while (new_value.isnumeric() == True or new_value == " "):
            new_value = input("Previous input was not a word, enter the new value for the attribute: ")
        setQuery = '''
        SET Name =:newSongName
        '''
        dictionary["newSongName"] = new_value
    if attributeToChange == 2: #update album
        while (new_value.isnumeric() == True or new_value == " "):
            new_value = input("Previous input was not a word, enter the new value for the attribute: ")
        setQuery = '''
        SET Album =:newAlbumName
        '''
        dictionary["newAlbumName"] = new_value
    if attributeToChange == 3: #update artist
        while (new_value.isnumeric() == True or new_value == " "):
            new_value = input("Previous input was not a word, enter the new value for the attribute: ")
        setQuery = '''
        SET Artist =:newArtistName
        '''
        dictionary["newArtistName"] = new_value
    if attributeToChange == 4: #update release date
        while (new_value.isalpha() == True or new_value == " "):
            new_value = input("Previous input was not a date, enter the new value for the attribute: ")
        setQuery = '''
        SET releaseDate =:newDate
        '''
        dictionary["newDate"] = new_value 
    if attributeToChange == 5:  #update explicit boolean
        while (not (new_value == "False" or new_value == "True" or new_value == None)):
            new_value = input("Previous input was not True or False, enter the new value for the attribute: ")
        setQuery = '''
        SET Explicit =:newExplicit
        '''
        dictionary["newExplicit"] = new_value
    query4 = query4 + setQuery + '''
        WHERE songID =:songID
    '''

    results = db_ops.execute_query(query4, dictionary)


def delete_song():
    deleteSong = input("Please enter the name of the song you would like to delete: ")
    query = '''
    SELECT songID
    FROM songs
    WHERE Name :=deleteSong
    '''
    
    num = 1
    dictionary = {"deleteSong":deleteSong}
    if num != 0:
        query += " LIMIT:lim"
        dictionary["lim"] = num
    results = db_ops.name_placeholder_query(query, dictionary)
    helper.pretty_print(results)

    


#Main Program
startScreen()
pre_process()

while True:
    user_choice = options()
    if user_choice == 1:
        search_by_artist()
    if user_choice == 2:
        search_by_genre()
    if user_choice == 3:
        search_by_feature()
    if user_choice == 4:
        update_song()
    if user_choice == 5:
        delete_song()
    if user_choice == 6:
        print("Goodbye!")
        break


#don't need to run more than once
#db_ops.create_songs_table()

#deconstruct at end
db_ops.destructor()