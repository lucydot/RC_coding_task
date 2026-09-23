#!/usr/bin/env python3

# Design Notes

## No AI usage of any form
## Built-in Python only for simplicity
## I've created a class so that I don't need to shuttle around lots of variables 
## I'm keeping the user input functions outside the class to de-couple player input and game mechanics
## Small re-factoring improvements listed in-line as "TODOs"

# New functionality

## Control game settings through a yaml file or similar
## Create a GUI
## Implement a computer player
## Allow remote playing through Github or similar?

class TicTacToe:

    def __init__(
            self,
            player_names
    ):
        
        self.player_one_name, self.player_two_name = player_names
        self.welcome_message()
        self.board = [[None,None,None],[None,None,None],[None,None,None]]
        self.current_player = self.player_two_name # note that these get switched before first move is played
        self.next_player = self.player_one_name
        
    def welcome_message(self):

        print("""Welcome to Lucy's TicTacToe. To specify a position use e.g. "top-left", "middle-left", "bottom-middle", "middle-middle". You know the rest of the rules...""" )
        print("{}, you will play first with the X counters".format(self.player_one_name))
        print("{}, you will play first with the O counters".format(self.player_two_name))

    def play(self):

        while self.check_winner() is False:
            self.current_player, self.next_player = self.next_player, self.current_player # this needs to come at the start rather than the end or the winner is stated wrongly
            user_input = player_input(self.current_player) # TODO: should these be class attributes?
            while self.validate_input(user_input) is False:   # This order is important as I don't want to pass an invalid string to the check_move_allowed method.
                user_input = player_input(self.current_player)
            while self.check_move_allowed(user_input) is False:
                user_input = player_input(self.current_player)
            user_input_indices = self.str_to_index(user_input)
            self.update_board(user_input_indices)
            self.display_board()

    def display_board(self):

        print(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}")

    def check_winner(self):   # TODO: a more succinct way of doing this

        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] is not None:
            self.goodbye_message()
            return True

        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] is not None:
            self.goodbye_message()    
            return True

        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] is not None:
            self.goodbye_message()
            return True

        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] is not None:
            self.goodbye_message()
            return True

        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] is not None:
            self.goodbye_message()
            return True

        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] is not None:
            self.goodbye_message()
            return True

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.goodbye_message()
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.goodbye_message()
            return True

        else:
            return False

    def update_board(self, user_input_indices):

        if self.current_player == self.player_one_name:
            self.board[user_input_indices[0]][user_input_indices[1]] = "X"
        else:
            self.board[user_input_indices[0]][user_input_indices[1]] = "0"

    def check_move_allowed(self, user_input):

        player_input_indices = self.str_to_index(user_input)
        if self.board[player_input_indices[0]][player_input_indices[1]] is not None:
            print("This space is occupied. Try Again.")
            return False
        else:
            return True 

    def validate_input(self, user_input):

        valid_player_inputs = ["top-left","top-middle","top-right","middle-left","middle-middle","middle-right","bottom-left","bottom-middle","bottom-right"]
        if user_input not in valid_player_inputs:
            print("This is not a valid input position. Try Again.")
            return False
        else:
            return True

    def str_to_index(self, user_input):   

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

        return str_to_index_dict[user_input]
        
    def goodbye_message(self):

        print("Congratulations {}, you are the winner!".format(self.current_player))        

def player_names():  

    player_one_name = input("Enter player one name: ")
    player_two_name = input("Enter player two name: ")

    return player_one_name, player_two_name

def player_input(current_player):

    player_input = input("{}, where would you like to place your counter? ".format(current_player))
    return player_input.strip() # remove any whitespace 

if __name__ == "__main__":

    game = TicTacToe(player_names())
    game.play()

