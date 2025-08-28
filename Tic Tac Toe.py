def main():
    introduction = intro()
    board = grid()
    pretty = prettyBoard(board)
    symbol_1, symbol_2 = symbol_selection()
    full = isfull(board, symbol_1, symbol_2) 


def intro():
    print("Welcome to tic tac toe game....!")
    print("\n")
    input("Press Enter to continue...!")
    print("\n")


def grid():
    print("This is your play board")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def symbol_selection():
    print("There are two symbols one is X and the other one is O")
    print("Who wants to choose first?\n " \
    "1: for player 1\n" \
    "2: for player 2.")
    choose = int(input("Enter you choice: "))
    if choose == 1:
        symbol_1 = "X"
        symbol_2 = "O"
    else:
        symbol_1 = "O"
        symbol_2 = "X"

    input("Press enter to continue.")
    print("\n")

    return symbol_1, symbol_2



def start_gaming(board, symbol_1, symbol_2, count):

    if count % 2 == 0:
        player = symbol_1
    else:
        player = symbol_2
    print("Player "+ player + " its your turn.")

    row = int(input("Pick a row:" "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]: "))
    column = int(input("Pick a column:" "[left column: enter 0, middle column: enter 1, right column: enter 2]: "))

  
    while (row < 0 or row > 2) or (column < 0 or column > 2):
        outofboard(row, column)
        row = int(input("Pick a row:" "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]: "))
        column = int(input("Pick a column:" "[left column: enter 0, middle column: enter 1, right column: enter 2]: "))
    
  
    while board[row][column] != " ":
        illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row:" "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]: "))
        column = int(input("Pick a column:" "[left column: enter 0, middle column: enter 1, right column: enter 2]: "))

    board[row][column] = player
    return board  

def isfull(board, symbol_1, symbol_2):
    count = 0
    winner = False
    
    while count < 9 and winner == False:
        board = start_gaming(board, symbol_1, symbol_2, count)
        pretty = prettyBoard(board)
        winner = isWinner(board, symbol_1, symbol_2)
        if winner:
            break
        count += 1
    
    if count == 9 and winner == False:
        print("The board is full...!")
        print("This match is tied")
    
    if winner == True:
        print("Game Over..! ")

    report(count, winner, symbol_1, symbol_2)

def prettyBoard(board):
    rows = len(board)
    print("------+------+------")

    for r in range(rows):
        print(board[r][0], " | ", board[r][1], " | ", board[r][2], " | ")
        print("------+------+------")
    return board

def isWinner(board, symbol_1, symbol_2):
    winner = False

    # Check rows
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2] != " "):
            winner = True
            print(f"{board[row][0]} wins...!")

    # Check columns
    for column in range(3):
        if( board[0][column] == board[1][column] == board[2][column] != " "):
            winner = True
            print(f"{board[0][column]} wins...!")

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
          winner = True
          print(f"Player {board[0][0]}, you won!")

    elif board[0][2] == board[1][1] == board[2][0] != " ":
          winner = True
          print(f"Player {board[0][2]}, you won!")

    return winner



def outofboard(row, column):
    print("Invalid selection. Pick another one")


def illegal(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Pick another one.")

def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if winner == True:
        if count % 2 == 0:
            print("Winner : Player " + symbol_1 + ".")
        else:
            print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")


main()
