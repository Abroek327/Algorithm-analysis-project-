from helper import helper
from db_operations import db_operations

class configurations:
    def __init__(self, games, configID):
        self.numGames = len(games)
        self.configID = configID
        self.games = games
        self.potentialProfit100dCapital = helper.profit(games)
        self.profitChance = helper.risk(games)
        #TODO: Needs to have attribute 'value' that represents (potential profit) * Chance of profit occuring
        # 'value' will be attribute maximized by simulated annueling
        self.value = self.potentialProfit100dCapital * self.profitChance
        

