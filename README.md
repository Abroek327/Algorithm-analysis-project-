# Algorithim-analysis-project


## How to Run
* Open a terminal inside the Project_parlay Folder
* Run **make run**
* Open index.html


Our group consists of James Tran, Jason Bohlinger, Andrew Broek, and Max Hartel. For our MVP of Project Parlay, we will be taking a static finite database from a sports league (ex: NFL, NHL, MLB, etc.) that contains the most important attributes needed to test our algorithm(s). These important attributes are: Games,Odds, Outcomes, Dates. The finite database will allow us to test our algorithms on a small sample size to be scaled later on with live data using a web scraper. MySQL and SQLite will be used to help with parsing queries and implementing the algorithms. From here, we will be trying 4 different types of algorithms that we were suggested. These algorithms will determine the most optimal bet to maximize the probability of winning and capital gain. Testing these algorithms would include research and implementation to determine which gives the most optimal results. If multiple algorithms give very good yet slightly different results, we could give the user a choice of which result to use. We will be using Python as our primary language for algorithm implementation and logic, and TypeScript for building the webscraper. 

Once the algorithm works with one finite database, we can easily implement our algorithm to another database given it has the same necessary attributes.It should update often with present developments in the sport. Since data for each different sport would include the attributes: Games, Odds, Outcomes, and Dates, the algorithm would be able to be applied over multiple sports.

The UI will be implemented in HTML, CSS, and JavaScript and be accessed through a browser for ease of use. The UI will be able to send user input data to our backend to run the algorithm using our database. User data will include a game with its date and matchup as well as budget to bet. The user will also be able to input an ‘aggressiveness’ factor to adjust how aggressive the algorithm will be when deciding possible results. The data will be fed into the algorithm and returned as an optimal bet on the screen. If the user does not like this bet, they would be able to re-run the program with different parameters to find their preference. 

References for algorithms: 
https://algorithmsbook.com/optimization/#

# Progress Check

## End Goal
Our final project will take user input on how many parlays they would like to bet, how much capital you would like to risk, how many games you would like to consider making parlays out of, and the respective win percentages for each game. Our program will then find all possible unique combinations of games (potential parlays), or an approximate set of potential parlays if the complete set would be too large to be practical to compute. It will then evaluate these parlays based off of risk reward ratio and assign them a score. The number of parlays to be evaluated may be too large to work with, in that case sinulated annueling will be used to create and score potential parlays. We will then use an algorithm to find the grouping of parlays with the highest possible combined score, that fits within the user specified bounds on parlay number and size. Then another algorithm will be used to split the user's total capital onto each individual parlay in the optimal manner. The resulting set of parlays and how much to bet on each one will then be returned to the user. This will use a colorful, interactive, and dynamic UI to display parlays and provide live tracking on parlay progress.

## Where we are now
Our current project will take user input on how many parlays they would like to bet, how much capital you would like to risk, how many games you would like to consider making parlays out of, and the respective win percentages for each game. Our program will then find all possible unique combinations of games (potential parlays) by brute force, limiting us to smaller sets of total games. It will then evaluate these parlays based off of lowest risk. We will then iterate over the set until we find the desired number of low risk parlays as specified by the user, that fits within the user specified bounds on parlay number and size.  The resulting set of parlays will then be returned to the user. This uses an ASCII based display to convey information to the user.

We have come a long way on our project since planning origionally started, and our plan for the rest of the semester is to take our project from where it is now to ourend project goal as described above. 


## MVP
[Link to the MVP Google Doc](https://docs.google.com/document/d/13wJoVv6TtfDdh3ldmpE6DFQjKy5D8gcNz_RNbGRM4Nw/edit?usp=sharing)
