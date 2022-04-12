from random import randint

class Game:
    def __init__(self):
        self.computer = Computer("Computer")
        self.player = Player("Player")

    def choose_starting_player(self):
        rng = randint(1, 10)
        if rng < 6:
            print("Computer goes first.")
            while self.computer.computer_score < 100 and self.player.player_score < 100:
                self.computer.round()
                self.player.round()
            if self.computer.computer_score >= 100:
                print("Computer wins!")
                return 
            else: 
                print("Player wins!")
                return
        else:
            print("Player goes first.")
            while self.computer.computer_score < 100 and self.player.player_score < 100:
                self.player.round()
                self.computer.round()
            if self.computer.computer_score >= 100:
                print("Computer wins!")
                return
            else:
                print("Player wins!")
                return

class Die:
    def __init__(self):
        self.value = randint(1, 6)

    def __str__(self):
        return f"{self.value}"

class Computer:
    def __init__(self, name):
        self.name = name 
        self.round_score = 0
        self.computer_score = 0


    def __str__(self):
        return f"{self.name}"

    def round(self):
        if self.round_score < 20:
            roll = Die().value
            print(f"Computer rolls {roll}")
            if roll != 1:
                self.round_score += roll
                print(f"Round score is {self.round_score}")
                self.round()
                self.round_score = 0
            else:
                print("You pigged it!") 
                self.round_score = 0
                self.computer_score += self.round_score
                print(f"Computer's total score is {self.computer_score}")
        else: 
            print("Computer holds")
            self.computer_score += self.round_score
            print(f"Computer's total score is {self.computer_score}")
            self.round_score = 0

class Player:
    def __init__(self, name):
        self.name = name 
        self.round_score = 0
        self.player_score = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        choice = "r"
        while choice != 'h':
            choice = input("Do you want to (r)oll or (h)old? ")
            if choice == 'h':
                break
            roll = Die().value
            print(f"You rolled {roll}")
            if roll != 1:
                self.round_score += roll
                print(f"Your score for this round is {self.round_score}")
            else:
                print("You pigged it!")
                self.round_score = 0
                break
        self.player_score += self.round_score
        print(f"Your total score is {self.player_score}")
        self.round_score = 0


game = Game()
game.choose_starting_player()