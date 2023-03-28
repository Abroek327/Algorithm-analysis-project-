import sqlite3

class db_operations():

    #constructor with connection path to database
    def __init__(self, conn_path):
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("connection made...")
    
    #creates the songs table
    def create_songs_table(self):
        query = '''
        CREATE TABLE songs(
            songID VARCHAR(22) NOT NULL PRIMARY KEY,
            Name VARCHAR(20),
            Artist VARCHAR(20),
            Album VARCHAR(20),
            releaseDate DATETIME,
            Genre VARCHAR(20),
            Explicit BOOLEAN,
            Duration DOUBLE,
            Energy DOUBLE,
            Danceability DOUBLE,
            Acousticness DOUBLE,
            Liveness DOUBLE,
            Loudness DOUBLE
        );
        '''
        self.cursor.execute(query)
        print("Table Created")

    #retrieves a single value from a table
    def single_record(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    #bulk inserts query data into table
    def bulk_insert(self, query, records):
        self.cursor.executemany(query, records)
        self.connection.commit()
        print("query executed...")

    #returns the values of a single attribute
    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results
    
    def name_placeholder_query(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    def single_tuple(self, query):
        self.cursor.execute(query)
        return self.cursor.description()[0]
    
    def delete_record(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return "Song deleted"
    
    def update_query(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    
    #destructor that closes connection to database
    def destructor(self):
        self.connection.close()
