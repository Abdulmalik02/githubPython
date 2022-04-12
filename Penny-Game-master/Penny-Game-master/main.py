# This is a game that determines if two pennies land on a matching side and
# alerts the user of the victor. If there is no winner, the game continues.

# Author: Logan Gremler 12/12/15

# Import everything we need from the games module:
from games import place_penny, display_menu

# Display the menu and get the user's option:
display_menu()
choice = raw_input("Enter your choice: ")

# Create values for the pennies and store them. Assign blank values to them if
# the user chooses an option other than play in order to avoid an ugly error:
if choice == "p":
    pn1 = place_penny()
    pn2 = place_penny()
else:
    pn1 = ""
    pn2 = ""

# Kick them out or display the coin values based off the menu option:    
if choice == "q":
    print "Bye!!!"
else:
    print "Player 1:" ,pn1
    print "Player 2:" ,pn2
    
# If the pennies do not match, play again. If there is a match, declare the
# appropriate winner:
while pn1 != pn2:
    print "Game Continue..."
    pn1 = place_penny()
    pn2 = place_penny()
    print "Player 1:" ,pn1
    print "Player 2:" ,pn2
if pn1 == "Head" and pn2 == "Head":
    print "Player 1 wins the game"
    print "Bye!!!"
elif pn1 == "Tail" and pn2 == "Tail":
    print "Player 2 wins the game"
    print "Bye!!!"
    
    
