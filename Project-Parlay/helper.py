from prettytable import PrettyTable
# module contains miscellaneous functions

class helper():
    # function parses a string and converts to appropriate type
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    # function reads file path to clean up data file
    @staticmethod
    def data_cleaner(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()

        data = [i.strip().split(",") for i in data]
        data_cleaned = []
        for row in data[:]:
            row = [helper.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned

    # function checks for user input given a list of choices
    @staticmethod
    def get_choice(lst):
        choice = input("Enter choice number: ")
        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")
        return int(choice)

    # function prints a list of strings nicely
    @staticmethod
    def pretty_print(lst):
        
        for i in lst:
            print(i)
        print("")

     # function prints a list of configurations nicely
    @staticmethod
    def config_print(configList):
        
        for y in configList:
            config = y.games
            # creating an empty PrettyTable
            x = PrettyTable()
            # adding data into the table row by row
            x.field_names = ["Team", "Win Percentage"]

            for i in config:    
                x.add_row([i.favoredTeam, i.favWinP])
            
            #print config
            print(x)

        print("\n")


    #TODO: Needs work to calculate for underdogs as well, currently assumes every team is a favorite
    #TODO: Needs to be fixed to properly asses risk, is not suggesting optimal parlays currently (check sample output)
    @staticmethod
    def risk(gameList):
        risk = 1
        for game in gameList:
            risk *= game.favWinP

        return risk
    
    @staticmethod
    def profit(gameList):
        # Win Percentage = Implied Probability
        # Implied probability = negative American odds/(negative American odds + 100) * 100
        # Implied probability = 100 / (positive American odds + 100) * 100
        # positive American odds = (100/Implied probability) - 100
        # negative American odds = ??
        profit = 0

        #for game in gameList:
            #TODO

        return profit
