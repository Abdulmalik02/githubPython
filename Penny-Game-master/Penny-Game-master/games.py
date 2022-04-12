# This functions generates a number between 1 and 10 and will return "Head"
# if the number is even and will return "Tail" if the number is odd. It also
# creates a menu for the user to decide what to do

# Author: Logan Gremler 12/12/15

from random import randint

def place_penny():
    r = randint(1, 10)

    if r % 2 == 0:
        return "Head"
    else:
        return "Tail"

def display_menu():
    print "###MENU###"
    print "p) Play the matching penny game"
    print "q) Quit"
