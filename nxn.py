# Coordinates:
# 0 | 1 | 2 | 3
# 4 | 5 | 6 | 7
# 8 | 9 | 10 | 11
# 12 | 13 | 14 | 15

# Empty: 0
# X: 1
# O: 2

from termcolor import colored
import os

def GeneratePossibleSolutions(boardSize):
    possibleSolutions = []

    diagonal1 = []
    diagonal2 = []
    for i in range(boardSize):
        diagonal1.append(i*(boardSize+1))
        diagonal2.append((i+1)*(boardSize-1))
        solution1 = []
        solution2 = []
        for j in range(boardSize):
            solution1.append(boardSize*i+j)
            solution2.append(i+boardSize*j)
        possibleSolutions.append(solution1)
        possibleSolutions.append(solution2)
    possibleSolutions.append(diagonal1)
    possibleSolutions.append(diagonal2)
    return possibleSolutions

def CheckBoard(board, boardSize): # Check if the game is won or tied
    # Check if the game is won
    possibleSolutions = GeneratePossibleSolutions(boardSize)
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

def Turn(board, playerNum, boardSize): # One player takes a turn and the board gets updated
    validTurn = False
    while not validTurn:
        field = int(input(f"Which field does the {playerNum}. player choose? "))
        if field >= boardSize * boardSize:
            pass
        else:
            validTurn = board[field] == 0 # Check if the tile is empty
    board[field] = playerNum # Update the board

    return board

def PrintBoard(board, boardSize): # Print the board in a nice way
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
    niceBoard = [] # Board with colored text
    for field in board:
        if field == 0:
            niceBoard.append("-")
        elif field == 1:
            niceBoard.append(colored("X", "blue"))
        else:
            niceBoard.append(colored("O", "red"))
    boardString = f""
    for i in range(boardSize):
        for j in range(boardSize):
            boardString += f"{niceBoard[i*boardSize+j]} | "
        boardString = boardString[:-3]
        boardString += f"\n"
    print(boardString)

def Main(boardSize):
    # Generate the board and print it
    board = [0] * boardSize * boardSize
    finished = False
    PrintBoard(board, boardSize)

    while not finished: # Take turns until the game is over
        for playerNum in range(1, 3): # Loop through each player
            board = Turn(board, playerNum, boardSize) # The player takes one turn
            PrintBoard(board, boardSize)
            result = CheckBoard(board, boardSize) # Check the board for victory or tie
            if result == 1: # Victory
                print(f"The winner is Player {playerNum}!")
                finished = True
                break
            elif result == 2: # Tie
                print("It's a tie!")
                finished = True
                break

if __name__ == "__main__":
    boardSize = int(input("How big should the board be? "))
    Main(boardSize) # Run the game