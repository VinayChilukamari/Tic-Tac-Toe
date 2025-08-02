# Tic Tac Toe ~ project idea credit -tech with tim

import random

def print_board(board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if j!=len(row)-1:
                print(" "+ col, end=' |')
            elif j==len(row)-1:
                print(" "+col)
        if i!=len(board)-1:
            for l in range(len(board)*4-1):
                print("-",end='')
            print()

# def board_position(board):
#     row=len(board)
#     col=len(board[0])
#     row_board_position=[[(i,j) for j in range(col)] for i in range(row)]
#     col_board_position=[[(j,i) for j in range(col)] for i in range(row)]
#     diagonal_boad_position=[[(i,i) for i in range(min(row,col))]]
#     anti_diagonal_boad_position=[[(i,(col-1)-i) for i in range(min(row,col))]]
    
#     matrix_location=list(row_board_position+col_board_position+diagonal_boad_position+anti_diagonal_boad_position)
    
#     return matrix_location

def board_position():
    matrix_location=[[(0,0),(0,1),(0,2)],
                     [(1,0),(1,1),(1,2)],
                     [(2,0),(2,1),(2,2)],
                     [(0,0),(1,0),(2,0)],
                     [(0,1),(1,1),(2,1)],
                     [(0,2),(1,2),(2,2)],
                     [(0,0),(1,1),(2,2)],
                     [(0,2),(1,1),(2,0)]]
    return matrix_location

def win_board(board):
    for i in board_position():
        win=[]
        for j in i:
            win.append(board[j[0]][j[1]])
        if win==['X','X','X']:
            print("\nCongratulations! 'X' has Won")
            return True
        elif win==['O','O','O']:
            print("\nCongratulations! 'O' has Won")
            return True
        else:
            continue

def user_location_input():
    while True:
        try:
            row_inp, col_inp=input("\nEnter location of 'board' you want to insert (seperated by ','): ").split(',')
            row_inp, col_inp=int(row_inp)-1,int(col_inp)-1
            if row_inp<0 or row_inp>2 or col_inp<0 or col_inp>2:
                print("\nInvalid location input, try again.")
            elif board[row_inp][col_inp]=='X' or board[row_inp][col_inp]=='O':
                print("\nPlace is already occupied, try again.")
            else:
                return row_inp,col_inp
        except ValueError:
            print("Invalid input, enter only integer values.")
   

def choose_turn_vs_2_player():
    while True:
        user1_turn=input("Choose 'X' or 'O': ").upper()
        if user1_turn=='X':
            user2_turn='O'
            return user1_turn,user2_turn
        elif user1_turn=='O':
            user2_turn='X'
            return user1_turn,user2_turn
        else:
            print("Invalid input, try again.")


def two_player(board):
    print()
    print_board(board)
    user1_turn,user2_turn=choose_turn_vs_2_player()
    exit_game=True
    for num_of_inp in range(9):
        while exit_game:
            if num_of_inp in [0,2,4,6,8]:
                row_inp,col_inp=user_location_input()
                board[row_inp][col_inp]=user1_turn
                print()
                print_board(board)
                if win_board(board):
                    exit_game=False
                    break
                if num_of_inp!=8:
                    print("\nTurn change")
                else:
                    print("\nMatch draw 💔")
                break
            elif num_of_inp in [1,3,5,7]:
                row_inp,col_inp=user_location_input()
                board[row_inp][col_inp]=user2_turn
                print()
                print_board(board)
                if win_board(board):
                    exit_game=False
                    break
                print("\nTurn change")
                break
            else:
                print("This is TIC TAC TOE ❤")

def comp_location_input(board):
    not_X_or_O=[(i,j) for i, row in enumerate(board) for j, col in enumerate(board) if board[i][j]!='X' or board[i][j]!='O']
    return random.choice(not_X_or_O)


def choose_turn_vs_computer():
    while True:
        user_turn=input("Choose 'X' or 'O': ").upper()
        if user_turn=='X':
            computer_turn='O'
            return user_turn,computer_turn
        elif user_turn=='O':
            computer_turn='X'
            return user_turn,computer_turn
        else:
            print("Invalid input, try again.")

def vs_computer(board):
    print()
    print_board(board)
    user1_turn,computer_turn=choose_turn_vs_computer()
    exit_game=True
    for num_of_inp in range(9):
        while exit_game:
            if num_of_inp in [0,2,4,6,8]:
                row_inp,col_inp=user_location_input()
                board[row_inp][col_inp]=user1_turn
                print()
                print_board(board)
                if win_board(board):
                    exit_game=False
                    break
                if num_of_inp!=8:
                    print("\nTurn change")
                else:
                    print("\nMatch draw 💔")
                break
            elif num_of_inp in [1,3,5,7]:
                while True:
                    row_inp,col_inp=comp_location_input(board)
                    if board[row_inp][col_inp]=='X' or board[row_inp][col_inp]=='O':
                        continue
                    else:
                        board[row_inp][col_inp]=computer_turn
                        break
                print()
                print_board(board)
                if win_board(board):
                    exit_game=False
                    break
                print("\nTurn change")
                break
            else:
                print("This is TIC TAC TOE ❤")


board=[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

if __name__=='__main__':
    print("TIC TAC TOE")
    while True:
        game_type=input("Do you want to play against 'player' or 'computer' (p/c): ").lower()
        if game_type=='p':
            two_player(board)
            break
        elif game_type=='c':
            vs_computer(board)
            break
        else:
            print("Invalid game type.")