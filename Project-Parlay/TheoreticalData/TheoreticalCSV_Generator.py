import csv
import random
from datetime import datetime, timedelta

# Set up the CSV writer
with open('theoretical_game_data1000000.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers
    writer.writerow(['Game_ID','Season','Week','SeasonWeek_ID','gameDate','FavoredTeam_ID','Underdog_ID','Fav_Implied_Win_P','UndD_Implied_Win_P','Winner_ID',])

    # Set up initial values for each attribute
    game_id = 0
    season = 0
    week = 0
    game_date = datetime.strptime('1/1/0001', '%m/%d/%Y')

    num_rows = 1000000

    # Loop through and generate each row of data
    for i in range(num_rows):
        # Increment the season every 272 rows
        if game_id % 272 == 0 and game_id > 0:
            season += 1
            week = 0

        # Increment the week every 17th row
        if game_id % 17 == 0 and game_id > 0:
            week += 1
            game_date += timedelta(days=7)

        # Set up the rest of the row's attributes
        season_week_id = f'{season}.{week}'
        favored_team_id = random.choice([chr(x) for x in range(65, 91)])
        underdog_id = favored_team_id
        while underdog_id == favored_team_id:
            underdog_id = random.choice([chr(x) for x in range(65, 91)])
        fav_implied_win_p = random.randint(51, 100)
        undd_implied_win_p = 100 - fav_implied_win_p

        fav_win = (fav_implied_win_p > random.randint(0,100))

        if (fav_win):
            winner_id = favored_team_id
        else:
            winner_id = underdog_id

        # Write the row
        writer.writerow([game_id, season, week, season_week_id, game_date.strftime('%m/%d/%Y'), favored_team_id, underdog_id, fav_implied_win_p, undd_implied_win_p, winner_id])

        # Increment the game_id
        game_id += 1
