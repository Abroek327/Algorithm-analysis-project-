from helper import helper

class game:
  def __init__(self, favoredTeam, underdog, favWinP):
    self.favoredTeam = favoredTeam
    self.underdog = underdog
    self.favWinP = (favWinP/100)
    self.uWinP = 1 - favWinP