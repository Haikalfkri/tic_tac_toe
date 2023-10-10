# initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# display board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


# check player who win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# check draw
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


# main function
def play_game():
    current_player = "X"
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")
            

if __name__ == "__main__":
    play_game()            