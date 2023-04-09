# Coordinates:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Empty: 0
# X: 1
# O: 2

from termcolor import colored
import os

def CheckBoard(board): # Check if the game is won or tied
    # Check if the game is won
    possibleSolutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for solution in possibleSolutions:
        fields = [] # For the three tiles in a solution, check what player occupies the tiles
        for field in solution:
            fields.append(board[field])
        # If all three tiles in a solution are occupied by the same player, this player has won
        if len(list(dict.fromkeys(fields))) == 1 and fields[0] != 0:
            return 1
    
    # Check for a tie
    tie = not 0 in board # If there's no empty tile, the game is tied
    if tie:
        return 2
    return 0

def Turn(board, playerNum): # One player takes a turn and the board gets updated
    validTurn = False
    while not validTurn:
        field = int(input(f"Which field does the {playerNum}. player choose? "))
        validTurn = validTurn = board[field] == 0 # Check if the tile is empty
    board[field] = playerNum # Update the board

    return board

def PrintBoard(board): # Print the board in a nice way
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
    niceBoard = [] # Board with colored text
    for field in board:
        if field == 0:
            niceBoard.append("-")
        elif field == 1:
            niceBoard.append(colored("X", "blue"))
        else:
            niceBoard.append(colored("O", "red"))
    print(f"{niceBoard[0]} | {niceBoard[1]} | {niceBoard[2]}")
    print(f"{niceBoard[3]} | {niceBoard[4]} | {niceBoard[5]}")
    print(f"{niceBoard[6]} | {niceBoard[7]} | {niceBoard[8]}")
    print("")

def Main():
    # Generate the board and print it
    board = [0] * 9
    finished = False
    PrintBoard(board)

    while not finished: # Take turns until the game is over
        for playerNum in range(1, 3): # Loop through each player
            board = Turn(board, playerNum) # The player takes one turn
            PrintBoard(board)
            result = CheckBoard(board) # Check the board for victory or tie
            if result == 1: # Victory
                print(f"The winner is Player {playerNum}!")
                finished = True
                break
            elif result == 2: # Tie
                print("It's a tie!")
                finished = True
                break

if __name__ == "__main__":
    Main() # Run the game