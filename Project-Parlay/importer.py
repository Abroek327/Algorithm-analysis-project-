from db_operations import db_operations

def calculateWinP(spread):
    percent = (-0.0303 * spread) + 0.5
    if (percent > 0.99):
        percent = 0.99
    return round(percent, 2)

# negative American odds = –1 * ( implied probability / (1 – implied probability)) * 100
def calcNegAmericanOdds(winP):
    return -1.0 * (winP / (1.0 - winP)) * 100.0

# positive American odds = 
# ((1 – implied probability) / implied probability)  * 100
def calcPosAmericanOdds(winP):
    return ((1 - winP) / winP) * 100


# decimal odds (From +American) = (AmericanOdds + 100) / 100
def calcPosDecOdds(american):
    return (american + 100) / 100
# decimal odds (From -American) = (AmericanOdds + 100) / AmericanOdds (Please note that for the purposes of this calculation, the negative sign in the odds is ignored.)
def calcNegDecOdds(american):
    return ((-1 * american) + 100) / (-1 * american)

dictionary = {"Las Vegas Raiders": "LVR",
              "Denver Broncos": "DEN",
              "Buffalo Bills": "BUF",
              "New York Jets": "NYJ",
              "Indianapolis Colts": "IND",
              "New England Patriots": "NE",
              "Los Angeles Rams": "LAR",
              "Kansas City Chiefs": "KC",
              "Chicago Bears": "CHI",
              "New York Giants": "NYG",
              "Minnesota Vikings": "MIN",
              "Philadelphia Eagles": "PHI",
              "Cleveland Browns": "CLE",
              "Miami Dolphins": "MIA",
              "Green Bay Packers": "GB",
              "Tennessee Titans": "TEN",
              "Atlanta Falcons": "ATL",
              "Detroit Lions": "DET",
              "Washington Commanders": "WAS",
              "San Francisco 49ers": "SF",
              "Arizona Cardinals": "AZ",
              "Los Angeles Chargers": "LAC",
              "Dallas Cowboys": "DAL",
              "Pittsburgh Steelers": "PIT",
              "New Orleans Saints": "NO",
              "Cincinnati Bengals": "CIN",
              "Tampa Bay Buccaneers": "TB",
              "Seattle Seahawks": "SEA",
              "Carolina Panthers": "CAR",
              "Jacksonville Jaguars": "JAX",
              "Baltimore Ravens": "BAL",
              "Houston Texans": "HOU"
}

db_ops = db_operations('allGameHistory.db')

# query = '''
# SELECT Winner_ID
# FROM NflHistoricalOffical
# '''
# results = db_ops.single_attribute(query)

# for i in range(len(results)):
#     currWinnerName = results[i]
#     print(currWinnerName, i + 1)
#     if (currWinnerName == None):
#         continue
#     query = '''
#      UPDATE NflHistoricalOffical
#      SET Winner_ID = ?
#      WHERE Game_ID = ?
#      '''
     
#     placeholders = [dictionary[currWinnerName], i + 2]
#     db_ops.name_placeholder_query(query, placeholders)
#     #print('inserted:', i + 1)
# db_ops.commit()
# #print('committed')

query = '''
SELECT Winner_ID FROM NflHistoricalOffical
'''
results = db_ops.single_attribute(query)
del results[0]
print(results)
for i in range(len(results)):
    print(i)

    query = '''
    UPDATE NflHistoricalOffical
    SET Winner_ID = ?
    WHERE Game_ID = ?
    '''
    placeholders = [results[i], i + 1]
    db_ops.name_placeholder_query(query, placeholders)
db_ops.commit()
