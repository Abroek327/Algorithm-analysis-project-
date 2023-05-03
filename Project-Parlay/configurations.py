from db_operations import db_operations
import random

class configurations:
        
    def americanOddsToString(config):

        if(config.AmericanOdds > 0):
            return "+" + str(round(config.AmericanOdds, 2))
        else:
            return "-" + str(-1 * round(config.AmericanOdds, 2))
        
    #TODO: Make accurate 'value' function from historical/theoretical factors using data science and back testing
    # Profit/risk are different representations of the same stat, so their ratio will always be 10
    #config.value = config.theoreticalProfit * config.profitChance
    def value(config):
        config.value = config.theoreticalProfit
        value = config.value
        return value
        
    #Calculates potential profit for parlay assuming "True Odds"
    #TODO Add web-Scraper support for the fixed odds of popular online casinos, maybe store tables of fixed odds for different size parlays and update as frequently as needed
    @staticmethod
    def profit(config):
        # Win Percentage = Implied Probability
        # Implied probability = negative American odds/(negative American odds + 100) * 100
        # Implied probability = 100 / (positive American odds + 100) * 100
        # positive American odds = ((1 – implied probability) / implied probability)  * 100
        # negative American odds = –1 * ( implied probability / (1 – implied probability)) * 100
        # decimal odds (From +American) = (AmericanOdds + 100) / 100
        # decimal odds (From -American) = (AmericanOdds + 100) / AmericanOdds (Please note that for the purposes of this calculation, the negative sign in the odds is ignored.)

  
        theoreticalCapital = 10
        configDecimalOdds = 1
        outcomeList = config.outcomeList
        
        for outcome in outcomeList:
            iP = outcome.ImpliedProbability/100

            if(outcome.underdog):

                outcome.AmericanOdds = ((1 - iP) / iP) * 100
                outcome.decimalOdds = (outcome.AmericanOdds + 100) / 100
            else:
                outcome.AmericanOdds = -1 * (iP / (1 - iP)) * 100
                outcome.decimalOdds = ((-1 *  outcome.AmericanOdds) + 100) / (-1 * outcome.AmericanOdds)

            configDecimalOdds *= outcome.decimalOdds

        config.decimalOdds = configDecimalOdds

        if(configDecimalOdds > 2):

            config.AmericanOdds = (configDecimalOdds - 1) * 100
            config.ImpliedProbability = 100 / (config.AmericanOdds + 100) * 100
        else:
            config.AmericanOdds = -1 * (100 / (configDecimalOdds - 1))
            config.ImpliedProbability = config.AmericanOdds / (config.AmericanOdds + 100) * 100

        config.theoreticalProfit = (configDecimalOdds * theoreticalCapital)

        configurations.value(config)


    #TODO(SOLVED): Needs work to calculate for underdogs as well, currently assumes every team is a favorite
    #TODO(SOLVED): Needs to be fixed to properly asses risk
    @staticmethod
    def risk(outcomeList):
        risk = 1

        for outcome in outcomeList:
            risk *= (outcome.ImpliedProbability/100)

        return risk


    
    def __init__(self, outcomeList, configID):
        self.numOutcomes = len(outcomeList)
        self.configID = configID
        self.outcomeList = outcomeList
        self.theoreticalProfit = "Not Yet Assigned"
        self.profitChance = configurations.risk(outcomeList)
        self.AmericanOdds = "Not Yet Assigned"
        self.ImpliedProbability = "Not Yet Assigned"
        self.decimalOdds = "Not Yet Assigned"
        #TODO: Needs to have attribute 'value' that represents parlay quality
        # 'value' will be attribute maximized by simulated annueling
        self.value = "Not Yet Assigned"

        configurations.profit(self)


