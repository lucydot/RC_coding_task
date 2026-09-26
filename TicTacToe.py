#!/usr/bin/env python3

# I've created a class so that I don't need to shuttle around lots of variables
class TicTacToe:
    def __init__(self, game_settings):

        self.grid_size = int(game_settings["grid_size"])
        self.player_one_name = game_settings["player_one_name"]
        self.player_two_name = game_settings["player_two_name"]
        self.board = [[None] * self.grid_size for i in range(self.grid_size)]
        self.current_input_indices = None
        self.current_player = self.player_two_name  # switched before first move
        self.next_player = self.player_one_name

    def play(self):

        self.welcome_message()

        while self.winner_exists() is False:
            if self.full_board() is True:
                self.draw_message()
                return

            # this needs to come at loop start or the winner is stated wrongly
            self.current_player, self.next_player = (
                self.next_player,
                self.current_player,
            )
            # I've went back on forth on this being an attribute or not
            # I've decided no as input could be garbage
            # and I'm not going down route of using setters
            current_input = player_input(self.current_player)

            # Loop ordering is important as I don't want to
            # pass an invalid string to the check_square_empty method.
            while self.validate_input(current_input) is False:
                current_input = player_input(self.current_player)

            while self.check_square_empty(current_input) is False:
                current_input = player_input(self.current_player)

            # I'm creating this attribute as it could be used
            # to determine the win state
            self.current_input_indices = self.str_to_index(current_input)
            self.update_board()
            self.display_board()

        self.win_message()

    # Could perhaps improve this using knowledge of the winning move?
    def winner_exists(self):

        n = self.grid_size
        columns = [[self.board[i][j] for i in range(n)] for j in range(n)]
        primary_diagonal = [[self.board[i][i] for i in range(n)]]
        secondary_diagonal = [[self.board[i][n - 1 - i] for i in range(n)]]

        lines = self.board + columns + primary_diagonal + secondary_diagonal

        for line in lines:
            if line[0] is not None and all(
                counter == line[0] for counter in line
            ):
                return True

        return False

    def full_board(self):

        # this is a bit dense to read but I'm trying to avoid using external
        # libraries which implement their own flatten functions
        return None not in [square for row in self.board for square in row]

    def validate_input(self, current_input):

        current_input_list = current_input.split()

        try:
            row = int(current_input_list[0])
            column = int(current_input_list[1])
        except ValueError:
            print("This is not a valid input position. Try Again.")
            return False

        if row >= self.grid_size or column >= self.grid_size:
            print("This is not a valid input position. Try Again.")
            return False

        return True

    def check_square_empty(self, current_input):

        current_input_indices = self.str_to_index(current_input)
        if (
            self.board[current_input_indices[0]][current_input_indices[1]]
            is not None
        ):
            print("This space is occupied. Try Again.")
            return False

        return True

    def str_to_index(self, current_input):

        current_input_list = current_input.split()
        return (int(current_input_list[0]), int(current_input_list[1]))

    def update_board(self):

        if self.current_player == self.player_one_name:
            self.board[self.current_input_indices[0]][
                self.current_input_indices[1]
            ] = "X"
        else:
            self.board[self.current_input_indices[0]][
                self.current_input_indices[1]
            ] = "O"

    def display_board(self):

        for row in self.board:
            print(row)

    def welcome_message(self):

        print(
            """Welcome to Lucy's TicTacToe. To specify the position use 
            Python-style indexing (row first, counting from zero). 
            Separate each index with a space. You know the 
            rest of the rules..."""
        )
        print(
            f"{self.player_one_name}, you will play first with the X counters"
        )
        print(
            f"{self.player_two_name}, you will play second with the O counters"
        )

    def win_message(self):

        print(f"Congratulations {self.current_player}, you are the winner!")

    def draw_message(self):

        print("It's a Draw!")


# I'm keeping the user input functions outside the class to
# de-couple player input and game mechanics
def game_settings():

    player_one_name = input("Enter player one name: ")
    player_two_name = input("Enter player two name: ")
    grid_size = input(
        "Enter the size of the square playing grid (as a single integer): "
    )
    game_settings = {
        "player_one_name": player_one_name,
        "player_two_name": player_two_name,
        "grid_size": grid_size,  # should make this so that user can input
    }

    return game_settings


def player_input(current_player):

    player_input = input(
        f"{current_player}, where would you like to place your counter? "
    )
    return player_input.strip()  # remove any whitespace


if __name__ == "__main__":
    game = TicTacToe(game_settings())
    game.play()
