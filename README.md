# Algorithim-analysis-project

## MVP
[Link to the MVP Google Doc](https://docs.google.com/document/d/13wJoVv6TtfDdh3ldmpE6DFQjKy5D8gcNz_RNbGRM4Nw/edit?usp=sharing)

Our group consists of James Tran, Jason Bohlinger, Andrew Broek, and Max Hartel. For our MVP of Project Parlay, we will be taking a static finite database from a sports league (ex: NFL, NHL, MLB, etc.) that contains the most important attributes needed to test our algorithm(s). These important attributes are: Games, Outcomes, Dates. The finite database will allow us to test our algorithms on a small sample size to be scaled later on with live data using a web scraper. SQL will be used to help with parsing queries and implementing the algorithms. From here, we will be trying 4 different types of algorithms that we were suggested. These algorithms will determine the most optimal bet to maximize the probability of winning and capital gain. Testing these algorithms would include research and implementation to determine which gives the most optimal results. If multiple algorithms give very good yet slightly different results, we could give the user a choice of which result to use. We will be using Python as our primary language for algorithm implementation and logic.

Once the algorithm works with one finite database, we can easily implement our algorithm to another database given it has the same necessary attributes.It should update often with present developments in the sport. Since data for each different sport would include the attributes: Games, Outcomes, and Dates, the algorithm would be able to be applied over multiple sports.

The UI will be implemented in HTML, CSS, and JavaScript and be accessed through a browser for ease of use. The UI will be able to send user input data to our backend to run the algorithm using our database. User data will include a game with its date and matchup as well as budget to bet. The user will also be able to input an ‘aggressiveness’ factor to adjust how aggressive the algorithm will be when deciding possible results. The data will be fed into the algorithm and returned as an optimal bet on the screen. If the user does not like this bet, they would be able to re-run the program with different parameters to find their preference. 

References for algorithms: 
https://algorithmsbook.com/optimization/#

