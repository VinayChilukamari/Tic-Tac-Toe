# Procol_inpect: Tic Tac Toe ~ procol_inpect idea credit -tech with tim

def print_board(board):
    for i, row in enumerate(board):
        for J, col in enumerate(row):
            if J==0:
                print(" "+ col, end=' | ')
            elif J==1:
                print(col, end=' | ')
            else:
                print(col)
        if i!=2:
            print("-----------")


def win_board(board):
    if [board[0][0],board[0][1],board[0][2]]==['X','X','X'] or [board[1][0],board[1][1],board[1][2]]==['X','X','X'] or [board[2][0],board[2][1],board[2][2]]==['X','X','X'] or [board[0][0],board[1][0],board[2][0]]==['X','X','X'] or [board[0][1],board[1][1],board[2][1]]==['X','X','X'] or [board[0][2],board[1][2],board[2][2]]==['X','X','X'] or [board[0][0],board[1][1],board[2][2]]==['X','X','X'] or [board[0][2],board[1][1],board[2][0]]==['X','X','X']:
        return True
    elif [board[0][0],board[0][1],board[0][2]]==['O','O','O'] or [board[1][0],board[1][1],board[1][2]]==['O','O','O'] or [board[2][0],board[2][1],board[2][2]]==['O','O','O'] or [board[0][0],board[1][0],board[2][0]]==['O','O','O'] or [board[0][1],board[1][1],board[2][1]]==['O','O','O'] or [board[0][2],board[1][2],board[2][2]]==['O','O','O'] or [board[0][0],board[1][1],board[2][2]]==['O','O','O'] or [board[0][2],board[1][1],board[2][0]]==['O','O','O']:
        return True

def inp_turn(board):
    print()
    print_board(board)
    for num_of_inp in range(9):
        while True:
            try:
                row_inp, col_inp=input("\nEnter location of 'board' you want to insert (seperated by ','): ").split(',')
                row_inp, col_inp=int(row_inp)-1,int(col_inp)-1
                if row_inp<0 or row_inp>2 and col_inp<0 or col_inp>2:
                    print("\nInvalid location input, try again.")
                elif board[row_inp][col_inp]=='X' or board[row_inp][col_inp]=='x' or board[row_inp][col_inp]=='O' or board[row_inp][col_inp]=='o':
                    print("\nPlace is already occupied, try again.")
                else:
                    inp_board=input(f"Enter what you want to input at loaction {row_inp+1},{col_inp+1}: ")
                    if inp_board=='X' or inp_board=='O':
                        break
                    else:
                        print("Only 'X' or 'O' is allowed.")
            except ValueError:
                print("Invalid input, enter only integer values.")
        
        board[row_inp][col_inp]=inp_board
        print()
        print_board(board)
        if win_board(board):
            print(f"\nCongratulation! {inp_board} has won.")
            break
        print("\nTurn change")


board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

if __name__=='__main__':
    inp_turn(board)