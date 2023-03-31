import sqlite3

class db_operations():

    #constructor with connection path to database
    def __init__(self, conn_path):
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("connection made...")
    
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
    
    #returns the results of a query with first column
    def name_placeholder_query(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    #returns results of a query for all columns
    def name_placeholder_query2(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        results = self.cursor.fetchall()
        return results
    
    #deletes a record based on query parameter and returns confirmation of deletion
    def delete_record(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()
        return "Song deleted.\n"
    
    #updates a single record's attribute based on query parameter and returns confirmation of attribute updated
    def update_query(self, query, dictionary, attribute):
        self.cursor.execute(query, dictionary)
        self.connection.commit()
        return "" + attribute + " updated.\n"

    
    #destructor that closes connection to database
    def destructor(self):
        self.connection.close()
