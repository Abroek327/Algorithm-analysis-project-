from helper import helper

#An individual, bettable outcome for a game
class outcome:

  def __init__(self, winP, name, gameID):
    self.gameID = gameID
    self.name = name
    self.AmericanOdds = "Not Yet Assigned"
    self.ImpliedProbability = winP
    self.decimalOdds = "Not Yet Assigned"

    if(winP < 50):
       self.underdog = True
    else:
      self.underdog = False