import random
board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
player = random.choice(['x','o'])
original_board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
def display_board(board):
    print(f'''
     {board[0]} | {board[1]} | {board[2]}
    ---+---+---
     {board[3]} | {board[4]} | {board[5]}
    ---+---+---
     {board[6]} | {board[7]} | {board[8]}''')

def player_input(board):
    global player
    while True:
        try:
            print(f'player {player} turn.')
            user_choice = int(input('please enter your choice: '))
            if 1 <= user_choice <= 9 and board[user_choice-1].isdigit():
                board[user_choice - 1] = player
                return board
            else:
                print('error - you need to pick a number between 1 - 9.')
        except ValueError:
            print('error - you need to pick a number between 1 - 9.')

def check_winner(board):
    tie_check = False
    if (board[0] == 'x' and board[1] == 'x' and board[2] == 'x'or board[0] == 'o' and board[1] == 'o' and board[2] == 'o'
            or board[3] == 'x' and board[4] == 'x' and board[5] == 'x' or board[3] == 'o' and board[4] == 'o' and board[5] == 'o'
            or board[6] == 'x' and board[7] == 'x' and board[8] == 'x'or board[6] == 'o' and board[7] == 'o' and board[8] == 'o'):
        if board[0] == 'x' or board[3] == 'x' or board[6] == 'x':
            return 'x winner'
        else:
            return 'o winner'
    if (board[0] == 'x' and board[3] == 'x' and board[6] == 'x'or board[0] == 'o' and board[3] == 'o' and board[6] == 'o'
            or board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or board[1] == 'o' and board[4] == 'o' and board[7] == 'o'
            or board[2] == 'x' and board[5] == 'x' and board[8] == 'x'or board[2] == 'o' and board[5] == 'o' and board[8] == 'o'):
        if board[0] == 'x' or board[1] == 'x' or board[2] == 'x':
            return 'x winner'
        else:
            return 'o winner'
    if (board[0] == 'x' and board[4] == 'x' and board[8] == 'x'or board[0] == 'o' and board[4] == 'o' and board[8] == 'o'
            or board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or board[2] == 'o' and board[4] == 'o' and board[6] == 'o'):
        if board[4] == 'x':
            return 'x winner'
        else:
            return 'o winner'
    for i in board:
        if i.isdigit():
            tie_check = True
    if tie_check:
        return True
    elif not tie_check:
        return 'tie'
    return True

def play_game():
    global player
    global board
    regame = False
    print('''
    --------------------------------
    | wellcome to Tic Tac Toe game |
    --------------------------------''')
    display_board(board)
    while check_winner(board):
        player_input(board)
        display_board(board)
        if player == 'x' and board != original_board:
            player = 'o'
        else:
            player = 'x'
        if check_winner(board) == 'x winner':
            print('x winner')
            regame = True
            break
        elif check_winner(board) == 'o winner':
            print('o winner')
            regame = True
            break
        elif check_winner(board) == 'tie':
            print('tie')
            regame = True
            break
    if regame:
        restart = input("play again? ").lower().split()
        if restart == 'y':
            board = original_board
            play_game()

play_game()
