#!/usr/bin/env python3

# Notes

## I've not used any AI/LLMs (incl. AI auto-complete)
## There are a few in-line comments re: design decisions

# New functionality / improvements

## Control game settings through a yaml file or similar
## Create a GUI
## Implement a computer player
## Allow remote playing through Github or similar?
## Implement logging
## A more succinct way of determining win state
## Could work out when a game is drawn (ahead of board being full)

class TicTacToe: # I've created a class so that I don't need to shuttle around lots of variables 

    def __init__(
            self,
            player_names
    ):
        
        self.player_one_name, self.player_two_name = player_names
        self.board = [[None,None,None],[None,None,None],[None,None,None]]
        self.current_input_indices = None
        self.current_player = self.player_two_name # note that these get switched before first move is played
        self.next_player = self.player_one_name

    def play(self):

        self.welcome_message()

        while self.winner_exists() is False:

            if self.full_board() is True:
                self.draw_message()
                return

            self.current_player, self.next_player = self.next_player, self.current_player # this needs to come at the start rather than the end or the winner is stated wrongly
            current_input = player_input(self.current_player)  # I've went back on forth on this being an attribute or not but decided no as it could be garbage and I'm not heading down the setter path 

            while self.validate_input(current_input) is False:   # The ordering of these while loops are important as I don't want to pass an invalid string to the check_square_empty method.
                current_input = player_input(self.current_player)

            while self.check_square_empty(current_input) is False:
                current_input = player_input(self.current_player)

            self.current_input_indices = self.str_to_index(current_input) # I'm creating this attribute as it could be used to determine the win state
            self.update_board()
            self.display_board()

        self.win_message()

    def welcome_message(self):

        print("""Welcome to Lucy's TicTacToe. To specify a position use e.g. "top-left", "middle-left", "bottom-middle", "middle-middle". You know the rest of the rules...""" )
        print("{}, you will play first with the X counters".format(self.player_one_name))
        print("{}, you will play second with the O counters".format(self.player_two_name))

    def display_board(self):

        print(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}")

    def full_board(self):

        if None in [square for row in self.board for square in row]:  # this is a bit dense to read but I'm trying to avoid using external libraries which implement their own flatten functions
            return False
        else:
            return True

    def winner_exists(self):   # It would be nice to find a more succinct way of doing this, perhaps using knowledge of the winning move?

        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] is not None:
            return True

        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] is not None: 
            return True

        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] is not None:
            return True

        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] is not None:
            return True

        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] is not None:
            return True

        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] is not None:
            return True

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True

        else:
            return False

    def update_board(self):

        if self.current_player == self.player_one_name:
            self.board[self.current_input_indices[0]][self.current_input_indices[1]] = "X"
        else:
            self.board[self.current_input_indices[0]][self.current_input_indices[1]] = "O"

    def check_square_empty(self, current_input):   

        current_input_indices = self.str_to_index(current_input)
        if self.board[current_input_indices[0]][current_input_indices[1]] is not None:
            print("This space is occupied. Try Again.")
            return False
        else:
            return True 

    def validate_input(self, current_input):

        valid_player_inputs = ["top-left","top-middle","top-right","middle-left","middle-middle","middle-right","bottom-left","bottom-middle","bottom-right"]
        if current_input not in valid_player_inputs:
            print("This is not a valid input position. Try Again.")
            return False
        else:
            return True

    def str_to_index(self, current_input):   

        str_to_index_dict = {
            "top-left": (0,0),
            "top-middle": (0,1),
            "top-right": (0,2),
            "middle-left": (1,0),
            "middle-middle": (1,1),
            "middle-right": (1,2),
            "bottom-left": (2,0),
            "bottom-middle": (2,1),
            "bottom-right": (2,2)
        }

        return str_to_index_dict[current_input]
        
    def win_message(self):

        print("Congratulations {}, you are the winner!".format(self.current_player))   

    def draw_message(self):

        print("It's a Draw!")     

def player_names():  # I'm keeping the user input functions outside the class to de-couple player input and game mechanics

    player_one_name = input("Enter player one name: ")
    player_two_name = input("Enter player two name: ")

    return player_one_name, player_two_name

def player_input(current_player):

    player_input = input("{}, where would you like to place your counter? ".format(current_player))
    return player_input.strip() # remove any whitespace 

if __name__ == "__main__":

    game = TicTacToe(player_names())
    game.play()

