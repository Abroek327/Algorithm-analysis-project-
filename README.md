# Algorithim Analysis Final Project: Project Parlay

## How to Run
* Open a terminal inside the Project_parlay Folder
* Run **make run**
* Once the program is finsihed running, you can open index.html in a browser to see the data in a more convenient way
* There is also a generated resultes file called results.txt that is also accessable, but is redundant with the index.html file

## Key Files
* Main Program: parlay.py
* Testing Script: testing_script_generator.py
* Tkinter Window: results.py
* HTML: index.html

## Introduction
Our group consists of James Tran, Jason Bohlinger, Andrew Broek, and Max Hartel. 

Project Parlay is a program made for the purposes of sports betting. It takes the data available in a given sports league and the input of the user's desired amount of capital and bets to return the most optimal way to use that capital for parlays.

The program uses a sqlite database of NFL games with data such as teams, odds, outcomes, and dates as a sample to test simulated annealing as an algorithm for finding the most optimal bets. The bulk of our backend code is done in python. There are two options for our front-end:
* When running the code in a command line, **results.py** will show a Tkinter window that prints the results of the parlays.
* The user can also open index.html in a browser after running the code to see the results in a more accessible environment. 

## Literature Review
We reviewed many sources and conducted a wide variety of research throughout the course of the project, but none was more impactful than "The Algorithm Design Manual" by Steven S. Skiena; it's an indispensable resource for computer scientists, programmers, and algorithm enthusiasts alike. The book provides a comprehensive introduction to the art of algorithm design and analysis, presenting a broad range of algorithmic techniques and strategies that are applicable to a wide variety of computational problems.

The book is divided into two main parts. The first part provides an overview of the fundamental principles of algorithm design, covering topics such as data structures, sorting and searching algorithms, graph algorithms, dynamic programming, and greedy algorithms. The second part delves deeper into advanced topics, including randomized algorithms, linear programming, network flows, and approximation algorithms, which led us to valuable information on simulated annealing.

One of the key takeaways from this book regarding simulated annealing (SA) is its usefulness in optimization problems, particularly in situations where a problem's landscape contains many local optima. SA is a probabilistic algorithm that can escape local optima by occasionally accepting "bad" moves during the search process. Skiena emphasizes the importance of properly tuning the SA parameters, such as the initial temperature and the cooling schedule, in order to ensure a good balance between exploration and exploitation.

Another important takeaway from the book is the use of SA in clustering and partitioning problems. By treating each cluster or partition as a state, SA can be used to search for an optimal configuration that minimizes a given objective function. Skiena presents several examples of using SA for clustering problems, including image segmentation and data clustering.

In addition to its comprehensive coverage of algorithm design and analysis, "The Algorithm Design Manual" is also highly readable and engaging. The author's writing style is clear and concise, and the book is filled with interesting anecdotes and historical background that make the material come alive.

Overall, "The Algorithm Design Manual" is an excellent resource for anyone interested in algorithm design and analysis. Whether you are a student, a researcher, or a practitioner in the field of computer science, this book is sure to be an invaluable reference for years to come.

## Testing
Our project was a very amitious one from the start, and it was regretful that we did not achieve full functionality with a practical betting aid that could directly impact user profits. But that being said, we tested our product extreamely throughly, with great maticularity, and some of our most valuable takeaways from the entire project came from our testing, and analysis of our testing data. For specifics on testing data and to look at visualizations of the data itself, please refer to the markdown document in the testing folder of this project. In general, we tool a big data approach to testing our algorithm, there were lots of adjustable factors that were were trying to optimize within our project, such as runtime, percent correctness, cooling rate, initial temperature, number of out puts, and so on. This led us to think that building an automated testing suite that could generate thousands of tests, which could then be compared on a macro scale and analyzed for overarching trends, would be the best way of testing our program. This was challenging at times, as the project was originally designed for user imput and to display data as a human would like to read it, which was not viable for a testing suite to utilize. This led to us reconfiguring every file of the project to have a testing version as well, which output raw data into a csv for ease of access by our data analytics methods. This was extreamely benefitial to the project, as it led to us discovering many key optimal values for our program, such as threshold and runtime, and which values to use as a benchmark for future improvementsuch as the correct amount of groupings to output at one time. It also led to us establishing that a potentially benifitial future plan would be to have the program switch between brute force and SA depending on the number of user games entered, since the BF algorithm could still run quickly with less than 10 games, but would need to be subbed out for SA after that point. We checked our SA algorithm for correctness by comparing it to the brute-force algorithm, which was guarenteed to be correct, but was tedius to test effectively with a large automated suite, as each running of the brute force program was liable to take significant time, and at times thousands of tests would be sceduled to be run in the testing suite. 

## Complications/Challenges
One of the most significant challenges we faced during the project was developing an efficient communication channel between our back-end and front-end. While we had initially planned on implementing a more sophisticated front-end, we ultimately had to make some compromises due to time and resource constraints. We shifted to a tkinter window and an HTML webpage printing the ASCII version of our output. The important and essential information is there, albeit in a less elegant way. Ultimately, the entire project can be done with one command in the command line and/or opening an HTML file in a browser, which is the ease of use we wanted. We also did not have the time to implement web scraping for live results. However, this did not affect the quality of our algorithm, and we were still able to achieve our goal of delivering accurate and optimal parlays to users.

Most of our computational and algorithmic challenges came from working with large amounds of data at once. With the large historical database being utilized, and the nature of the number of combinations to expand at at great rate as thesize of a user game list increases, great emphasis had to be placed on making sure everything eas being done as efficiently as possible, and we would lose large amounts of time due to waiting for n test results if we did not mind the efficiency. 

## Contributions
* Max: Project Organizer, Implemented the single output and multi output simulated annealing algorithms, implemented and designed the automated testing suite, performed data analysis on testing results, project founder
* James: Initial Simulated Annealing Research, Database cleaning and formatting, Front-End Design and Implementation (Tkinter, HTML)
* Jason: Setup, maintenance, formatting of the SQLite database for the group's needs, and creation + cleaning of testing data sources.
* Andrew: SQL Testing, Knapsack research, and Simulated Annealing implementation research.  

## Future Directions
* Web scraping from an online database, yielding live results, would allow for easy automation. This means you could run this program for an entire season, hands-off, as it places bets for you and you can simply cash your checks!
* Having a more sophisticated UI would help with the average user's understanding of what is going on. Hopefully, a nice and effective web app would showcase the potential of this program.
* the function to determine the "value" of a parlay still needs significant work. It currently is set to maximize a arbitrary value to create parlays from user input, to showcase the effectiveness and efficiency of our well implemented simulated annealing algorithm. But this attribute does not directly contribute to the parlays being beret or worse in any practical measurable way. We have a plan for how to obtain this value by utilizing big data trends in the historical data we have collected, and then settig SA to maximize the attributes identified from the data as being most benifitial. But due to the large size of the historical database, the time it would take to adequately analyze it, and that our primary focus was on developing the algorithm instead of the data science, establishing a true "value" function was forced to be pushed outside of the scope of this phase of the project. However it is worth mentioning that effort was made to achieve this, but most of what was gained was a greater understanding of the time and effort it would take to achieve such a goal. 
* As the core of the project views outcomes through the lense of "Implied Win Percentages" the project should be able to be scaled such that any sports game from any leuage across the world could be incorperated into the project without much effort. The culmination of this would result in the user being able to utilize this algorithm with anything that has odds attached to it, no matter what the actual betting event is itself. 
* Our goal for this phase of the project was to be able to test and have the algorithm perform with a pool of up to 16 games, but through our testing we saw no reason why 16 should be a hard cap on the number of games considered, as it did not have any direct negative effects that were picked up by our testing. 

## References
* Skiena, Steven S. The Algorithm Design Manual. 3rd ed., Springer, 2021.
* References for algorithms:  https://algorithmsbook.com/optimization/#
* Tkinter implementation: https://www.geeksforgeeks.org/python-tkinter-text-widget/
* HTML: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
