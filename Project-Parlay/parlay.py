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
    



    
#Main Program
startScreen()



#deconstruct at end
db_ops.destructor()