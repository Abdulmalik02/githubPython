CRC 

GAME:

Responsibilities:
Start - Begin the game
End - End the game when a player's score reaches 100
Computer - Create the COMPUTER player
Player - Create the human PLAYER
Die - Create the DIE that will be rolled
Score - Create a scoreboard starting at 0
Turn - Determine which player goes first and change player turns when they "hold" or roll "pig"

Collaborators:
COMPUTER
PLAYER
DIE



DIE:

Responsibilities:
Value - Determine the values of the DIE faces, i.e., 1-6.
Roll - Give the DIE the ability to be rolled by the PLAYER and COMPUTER

Collaborators:
GAME
PLAYER
COMPUTER



COMPUTER:

Responsibilities:
Roll - Give the COMPUTER the ability to roll the DIE (Always roll if turn score is below 20)
Hold - Give the COMPUTER the ability to hold their score (Always hold if turn score is 20 or above)
Score - Keep track of turn score

Collaborators:
DIE
GAME



PLAYER:

Responsibilities:
Roll - Give the PLAYER the option to roll the DIE
Hold - Give the PLAYER the option to hold their score and pass their turn to the COMPUTER
Score - Keep track of turn score

Collaborators:
DIE
GAME