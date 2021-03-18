This project solves the famous Towers of Hanoi puzzle using a rather inefficient 'brute force' algorithm using random numbers. I'm well aware that there are more optimal ways to solve the puzzle such as recursive algorithms, but I thought it would be fun to see how much I could solicit my CPU and learn a bunch of useful libraries like Pandas along the way!! For full disclosure, the node.py and stack.py files are from codecademy.com, and the random, datetime, pandas, numpy, and matplotlib libaries are invoked in the main script.py file that I largely wrote on my own, with the help of some online sources.

Rules of the game (source: Codecademy.com)

    Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.

    The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

    The game follows three rules:

    Only one disk can be moved at a time.
    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    No disk may be placed on top of a smaller disk.
    
Main steps from script.py:
-Create CSV template with header in working directory

-Prompt user to enter number of disks (hardcode in script.py, don't go larger than 3 to start)

-Prompt user to enter number of times to play game (hardcode)

-Play_game function invoked until loop ends and number of moves needed and time elapsed logged to CSV for each function iteration. Please read comments in script.py play_game 
function definition for more details

-CSV trailer record created and file closed.

-Import csv file using Pandas library and create Dataframe object (ignoring header and trailer records)

-Define linear regression using numpy library and insert into dataframe object

-Create and open scatterplot with x as '# of moves', y as 'time elapsed' and linear regression

I hope this exercices was valuable to all. Please comment if you have any feedback!

