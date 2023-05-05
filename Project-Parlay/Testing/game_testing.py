from outcome_testing import outcome

#a contest between two sides with odds
class game:

  def __init__(self, favoredTeam, underdog, favWinP, gameID):
    outcomeF = outcome(favWinP, favoredTeam, gameID)
    outcomeU = outcome((100 - favWinP), underdog, gameID)
    outcomeList = [outcomeF, outcomeU]
    
    self.gameID = gameID
    self.outcomes = outcomeList
    self.favoredTeam = outcomeF
    self.underdog = outcomeU