import random
import copy


class hypoParlay:
    hpID = -1

    def parlayID():
        hypoParlay.hpID += 1

        return hypoParlay.hpID
    

    def __init__(self, outcomeList):
        self.numOutcomes = len(outcomeList)
        self.hpID = hypoParlay.parlayID()
        self.outcomeList = outcomeList
        self.AmericanOdds = "Not Yet Assigned"
        self.ImpliedProbability = "Not Yet Assigned"
        self.H_misses = 0
        self.H_hits = 0
        self.H_hitMissRatio = 0
        self.H_total_profit = 0
        self.H_seasonsProfit = []
        self.H_profitFailRatio = 0
        self.T_misses = 0
        self.T_hits = 0
        self.T_hitMissRatio = 0
        self.T_total_profit = 0
        self.T_seasonsProfit = []
        self.T_profitFailRatio = 0

