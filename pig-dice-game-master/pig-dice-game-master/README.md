# Pig

This app is a virtual version of the dice game, Pig, built in Python using object-oriented programming. 

The Player plays against the computer, both of whom are trying to be the first to reach a score of 100 points. Each player alternates turns rolling a die (in this case, a random integer between 1 and 6) until they roll a 1 (or a "pig") or they choose to hold their score. If they hold, the sum total of their rolls is added to their total score. If they roll a pig, they get no points. After a pig is rolled or the player holds, the turn is passed to the other player. 

In this version of the game, the first player is chosen randomly and the computer player will always roll again until they reach a total of 20 points in a turn. Once they reach 20, they will always hold. 

The program can be run with the 'python3 pig.py' command in the terminal after cloning this repository. 

This was an assignment for Momentum Learning Immersive Full Stack Development Course.