#!/usr/bin/env python3

class TicTacToe: # I've created a class so that I don't need to shuttle around lots of variables 

    def __init__(
            self,
            game_settings
    ):

        self.grid_size = game_settings["grid_size"]
        self.player_one_name = game_settings["player_one_name"]
        self.player_two_name = game_settings["player_two_name"]
        self.board = [[None]*self.grid_size for i in range(self.grid_size)]
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

        print("""Welcome to Lucy's TicTacToe. Your grid is 3x3. To specify a position use e.g. "top-left", "middle-left", "bottom-middle", "middle-middle". You know the rest of the rules...""" )
        print("{}, you will play first with the X counters".format(self.player_one_name))
        print("{}, you will play second with the O counters".format(self.player_two_name))

    def display_board(self):

        for row in self.board:
            print(row)

    def full_board(self):

        if None in [square for row in self.board for square in row]:  # this is a bit dense to read but I'm trying to avoid using external libraries which implement their own flatten functions
            return False
        
        return True

    def winner_exists(self):   # Could perhaps improve this using knowledge of the winning move?

        n = self.grid_size
        columns = [[self.board[i][j] for i in range(n)] for j in range(n)]
        primary_diagonal = [[self.board[i][i] for i in range(n)]] 
        secondary_diagonal = [[self.board[i][n-1-i] for i in range(n)]]

        lines = self.board + columns + primary_diagonal + secondary_diagonal

        for line in lines:
            if line[0] is not None and all(counter == line[0] for counter in line):
                return True

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
        
        return True 

    def validate_input(self, current_input):

        valid_player_inputs = ["top-left","top-middle","top-right","middle-left","middle-middle","middle-right","bottom-left","bottom-middle","bottom-right"]
        if current_input not in valid_player_inputs:
            print("This is not a valid input position. Try Again.")
            return False
        
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

def game_settings():  # I'm keeping the user input functions outside the class to de-couple player input and game mechanics

    player_one_name = input("Enter player one name: ")
    player_two_name = input("Enter player two name: ")
    game_settings = {
        "player_one_name": player_one_name,
        "player_two_name": player_two_name,
        "grid_size": 3 # should make this so that user can input
    }

    return game_settings

def player_input(current_player):

    player_input = input("{}, where would you like to place your counter? ".format(current_player))
    return player_input.strip() # remove any whitespace 

if __name__ == "__main__":

    game = TicTacToe(game_settings())
    game.play()

