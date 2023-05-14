
#An individual, bettable outcome for a game
class outcome:
    oID = 0

    def outcomeID():
        outcome.oID += 1

        return outcome.oID
    
    def equals(outcomeA, outcomeB):

        if(outcomeA.name == outcomeB.name and outcomeA.ImpliedProbability == outcomeB.ImpliedProbability):
            return True
        else:
            return False
    
    def __init__(self, winP, name, gameID):
        self.outcomeID = outcome.outcomeID()
        self.gameID = gameID
        self.name = name
        self.AmericanOdds = "Not Yet Assigned"
        self.ImpliedProbability = winP
        self.decimalOdds = "Not Yet Assigned"

        if(winP < 50):
            self.underdog = True
        else:
            self.underdog = False