# Coordinates:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Empty: 0
# Player (X): 1
# Computer (O): -1

import random
from termcolor import colored
import os

class Random: # Makes a random move
    def Turn(self, board):
        # Generate all of the empty tiles on the board
        emptyTiles = []
        for tile in board:
            if tile == 0:
                emptyTiles.append(tile)
        
        # Randomly choose an empty tile
        randomTile = random.choice(emptyTiles)
        
        # Apply the change to the board
        board[randomTile] = -1
        return board
    
class Simple: # Wins if possible, tries to prevent the player from winning
    def Turn(self, board):
        # Generate lists of the different tile types
        botTiles = []
        playerTiles = []
        emptyTiles = []
        for i, tile in enumerate(board):
            if tile == 0:
                emptyTiles.append(i)
            elif tile == 1:
                playerTiles.append(i)
            elif tile == -1:
                botTiles.append(i)

        # For every possible move, check if it results in a win, loss or tie
        for tile in emptyTiles:
            newBoard = board.copy()
            newBoard[tile] = -1
            if CheckBoard(newBoard) == 1: # If the move results in a win for the bot, make the move
                board[tile] = -1
                return board
            newBoard[tile] = 1
            if CheckBoard(newBoard) == 1: # If not making the move would allow the player to win, make the move
                board[tile] = -1
                return board
        # If it's not possible to win or prevent a loss, make a random move
        randomTile = random.choice(emptyTiles)
        board[randomTile] = -1
        return board

class Perfect: # Plays perfectly using minimax
    def Turn(self, board):
        # Calculate the optimal move and make it
        calculation = self.Minimax(self, board, -1)
        print(calculation)
        board[calculation[1]] = -1
        return board
    
    def Minimax(self, board, player):
        # Check if the board is won or tied
        boardState = CheckBoard(board)
        if boardState == 1:
            if player == 1:
                return 1, 9
            return -1, 9
        if boardState == -1:
            if player == 1:
                return -1, 9
            return 1, 9

        move = -1
        score = -2

        for i in range(9): # Go through all tiles
            if board[i] == 0: # Only continue if the tile is empty
                board[i] = player # Make the move
                moveScore = - self.Minimax(self, board, -player)[0] # Apply minimax to the new position
                board[i] = 0 # Unmake the move
                # Update score and move if the position is a new optimum
                if moveScore > score:
                    score = moveScore
                    move = i
        # If there are no possible moves, the game is tied
        if move == -1:
            return 0, 9
        return score, move # Return the score of the position and the best move

def CheckBoard(board): # Check if the game is won or tied
    # Check if the game is won
    possibleSolutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for solution in possibleSolutions:
        fields = [] # For the three tiles in a solution, check what player occupies the tiles
        for field in solution:
            fields.append(board[field])
        # If all three tiles in a solution are occupied by the same player, this player has won
        if len(list(dict.fromkeys(fields))) == 1 and fields[0] != 0:
            return fields[0]
    
    # Check for a tie
    tie = not 0 in board # If there's no empty tile, the game is tied
    if tie:
        return 2
    return 0

def Turn(board): # One player takes a turn and the board gets updated
    validTurn = False
    while not validTurn:
        tile = int(input(f"Which tile do you choose? "))
        validTurn = board[tile] == 0 # Check if the tile is empty
    board[tile] = 1 # Update the board

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

def Main(bot):
    # Generate the board and print it
    board = [0] * 9
    finished = False
    PrintBoard(board)

    while not finished: # Take turns until the game is over
        for player in [1, -1]: # Loop through each player
            if player == 1:
                board = Turn(board) # The player takes one turn
            elif player == -1:
                board = bot.Turn(bot, board) # The bot takes one turn
            PrintBoard(board) # Print the updated board
            result = CheckBoard(board) # Check the board for victory or tie
            if result == 1: # Victory
                print("You win!")
                finished = True
                break
            elif result == -1: # Defeat
                print("You lose!")
                finished = True
                break
            elif result == 2: # Tie
                print("It's a tie!")
                finished = True
                break

if __name__ == "__main__":
    bot = Simple # Choose which bot you want to play agains (Random, Simple, Perfect)
    Main(bot) # Run the game