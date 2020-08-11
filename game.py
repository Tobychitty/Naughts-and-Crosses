positions_board = f"""
Board Positions:
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
"""

# Game Board
board = ["   ", "   ", "   ",
         "   ", "   ", "   ",
         "   ", "   ", "   "]

# If game is active
game_on = True

# Who's turn it is
current_player = 1

# Who won the game
winner = None

player = {
    1: ' X ',
    2: ' O '
}


def display_board():
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('---+---+---')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('---+---+---')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def play_game():

    print("""-xo- Welcome to Naughts & Crosses -xo-
    
(Type 'help' to view position numbers)
    """)

    # Displays initial game board
    display_board()

    # While the game is active
    while game_on:
        # Handles current players turn
        handle_turn(current_player)

        # Check to see if the game is over
        check_game_end()

        # Change player
        swap_player()

    # Result of game
    if winner == 1 or winner == 2:
        print(f'Player {winner} won!')
    elif winner is None:
        print('The game was a draw!')


# Handle a single turn for the current player
def handle_turn(player_number):

    print(f"""
--- Player {current_player}'s turn ---""")

    valid = False
    while not valid:

        choice = input("Choose your position 1-9: ")

        if choice == 'help':
            print(positions_board)

        while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            choice = input("Choose your position 1-9: ")

        choice = int(choice) - 1

        if board[choice] == "   ":
            valid = True
        else:
            print("You can't go there, go again")

    board[choice] = player[player_number]

    display_board()


def check_game_end():
    # Set up global variables
    global winner

    # Checks if someone has won
    check_for_win()

    if winner == ' X ':
        winner = 1
    elif winner == ' O ':
        winner = 2

    # Checks if there has been a draw
    check_for_draw()


def swap_player():
    # Set up global variables
    global current_player

    # Swapping the current player
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1

    return


def check_for_win():
    # Set up global variables
    global winner

    # Check rows
    row_winner = check_rows()
    # Check cols
    col_winner = check_cols()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_cols():
    # Setup global variables
    global game_on

    # Check rows for 3 same values unless blanks
    col1 = board[0] == board[3] == board[6] != '   '
    col2 = board[1] == board[4] == board[7] != '   '
    col3 = board[2] == board[6] == board[8] != '   '

    # If one col has won, stop game
    if col1 or col2 or col3:
        game_on = False

    # Return the winner (X or O)
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]


def check_rows():
    # Setup global variables
    global game_on

    # Check rows for 3 same values unless blanks
    row1 = board[0] == board[1] == board[2] != '   '
    row2 = board[3] == board[4] == board[5] != '   '
    row3 = board[6] == board[7] == board[8] != '   '

    # If one row has won, stop game
    if row1 or row2 or row3:
        game_on = False

    # Return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_diagonals():
    # Setup global variables
    global game_on

    # Check rows for 3 same values unless blanks
    diagonal1 = board[0] == board[4] == board[8] != '   '
    diagonal2 = board[2] == board[4] == board[6] != '   '

    # If one diagonal has won, stop game
    if diagonal1 or diagonal2:
        game_on = False

    # Return the winner (X or O)
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]


def check_for_draw():
    # Set up global variables
    global game_on

    if "   " not in board:
        game_on = False


play_game()
