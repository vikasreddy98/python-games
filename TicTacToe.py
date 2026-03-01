from IPython.display import clear_output


# PRINTS A SIMPLE 3 * 3 BOARD

def display_board(board):
    
    clear_output()

    print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
    print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')
    

# TAKES THE PLAYER INPUT AND ASSIGNS THEIR MARKER AS 'X' OR 'O'

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose between X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# ASSIGNS DESIRED POSITION ON THE BOARD
  
def place_marker(board, marker, position):
    board[position] = marker


# CHECKS IF A PLAYER WON

def win_check(board,mark):
    return (board[9] == board[8] == board[7] == mark or
    (board[4] == board[5] == board[6] == mark) or
    board[1] == board[2] == board[3] == mark or
    board[7] == board[4] == board[1] == mark or
    board[8] == board[5] == board[2] == mark or
    board[9] == board[6] == board[3] == mark or
    board[7] == board[5] == board[3] == mark or
    board[9] == board[5] == board[1] == mark)


# RANDOMLY SELECTS WHICH PLAYER GOES FIRST

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'P1'
    else:
        return 'P2'


# CHECKS IF THE SPACE IS EMPTY ON THE BOARD

def space_check(board, position):
    return board[position] == ' '
   
# CHECKS IF THE BOARD IS FULL

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# ASKS PLAYER FOR THEIR NEXT MOVE AND CHECKS IF THAT SPACE IS TAKEN

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please choose a position between 1 and 9: "))
    return position


# ASKS PLAYERS IF THEY WANT TO PLAY AGAIN

def replay():

    return input("Would you like to play again (y/n)?").lower().startswith('y')

# GAME LOGIC

print ("WELCOME TO 'SIMPLE' TIC-TAC-TOE!")

while True:
    # Reset the board
    newBoard = [' ']*10
    P1_marker, P2_marker = player_input()
    turn = choose_first()
    print(turn+ ' will go first!')

    play_game = input('Are you ready to play (y/n)?')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'P1':

            # P1's turn

            display_board(newBoard)
            position = player_choice(newBoard)
            place_marker(newBoard, P1_marker, position)

            if win_check(newBoard, P1_marker):
                display_board(newBoard)
                print("Congrats! P1 won the game!")
                game_on = False
            else:
                if full_board_check(newBoard):
                    display_board(newBoard)
                    print ("OOPS! It's a Draw!")
                    break
                else:
                    turn = 'P2'
        else:

            # P2's turn

            display_board(newBoard)
            position = player_choice(newBoard)
            place_marker(newBoard, P2_marker, position)

            if win_check(newBoard, P2_marker):
                display_board(newBoard)
                print("Congrats! P2 won the game!")
                game_on = False
            else:
                if full_board_check(newBoard):
                    display_board(newBoard)
                    print ("OOPS! It's a Draw!")
                    break
                else:
                    turn = 'P1'
    if not replay():
        break

