# Coordinates:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Empty: 0
# X: 1
# O: 2

import random
from termcolor import colored

class Random: # Makes a random move
    def Turn(self, board):
        emptyTiles = []
        for tile in board:
            if tile == 0:
                emptyTiles.append(tile)
        
        randomTile = random.choice(emptyTiles)
        board[randomTile] = 2
        return board
    
class Simple: # Wins if possible, tries to prevent the player from winning
    def Turn(self, board):
        botTiles = []
        playerTiles = []
        emptyTiles = []
        for i, tile in enumerate(board):
            if tile == 0:
                emptyTiles.append(i)
            elif tile == 1:
                playerTiles.append(i)
            elif tile == 2:
                botTiles.append(i)
        for tile in emptyTiles:
            newBoard = board.copy()
            newBoard[tile] = 2
            if CheckBoard(newBoard) == 1:
                board[tile] = 2
                return board
            newBoard[tile] = 1
            if CheckBoard(newBoard) == 1:
                board[tile] = 2
                return board
        randomTile = random.choice(emptyTiles)
        board[randomTile] = 2
        return board

class Perfect:
    def Turn(self, board):
        playerTiles = []
        botTiles = []
        emptyTiles = []
        for tile in board:
            if tile == 1:
                playerTiles.append(tile)
            elif tile == 2:
                botTiles.append(tile)
            else:
                emptyTiles.append(tile)
        calculation = self.CalculateTurn(self, board, playerTiles, botTiles, emptyTiles)
        print(calculation)
        if calculation[0] in [1, 2]:
            board[calculation[1]] = 2
            return board
        else:
            randomTile = random.choice(emptyTiles)
            board[randomTile] == 2
            return board

    def CalculateTurn(self, board, playerTiles, botTiles, emptyTiles):
        botTurn = len(playerTiles) > len(botTiles)
        outcomes = []

        if len(emptyTiles) == 0 and botTurn:
            return 0, 9
        if len(emptyTiles) == 1 and not botTurn:
            return 1, emptyTiles[0]
        for tile in emptyTiles:
            newBoard = board.copy()
            newBotTiles = botTiles.copy()
            newPlayerTiles = playerTiles.copy()
            newEmptyTiles = emptyTiles.copy()

            newBoard[tile] = int(botTurn) + 1
            newEmptyTiles.remove(tile)
            if botTurn:
                newBotTiles.append(tile)
            else:
                newPlayerTiles.append(tile)
            calculation = self.CalculateTurn(self, newBoard, newPlayerTiles, newBotTiles, newEmptyTiles)
            outcomes.append(calculation[0])
            newEmptyTiles.append(tile)
            try:
                newBotTiles.remove(tile)
            except:
                newPlayerTiles.remove(tile)
            newBoard[tile] = 0
            if botTurn and calculation[0] == 1:
                return 1, calculation[1]
            if not botTurn and calculation[0] == 0:
                return 0, 9
        if 2 in outcomes:
            return 2, emptyTiles[outcomes.index(2)]
        if botTurn:
            return 0, 9
        else:
            return 1, random.choice(emptyTiles)

def CheckBoard(board): # Check if the game is won or if it's a tie
    # Check if the game is won
    possibleSolutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for solution in possibleSolutions:
        fields = []
        for field in solution:
            fields.append(board[field])
        if len(list(dict.fromkeys(fields))) == 1 and fields[0] != 0:
            return 1
    
    # Check for a tie
    tie = True
    for field in board:
        if field == 0:
            tie = False
    if tie:
        return 2
    return 0

def Turn(board): # One player takes a turn and the board gets updated
    validTurn = False
    while not validTurn:
        field = int(input(f"Which field do you choose? "))
        validTurn = board[field] == 0
    board[field] = 1

    return board

def PrintBoard(board): # Print the board in a nice way
    niceBoard = []
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
    board = [0] * 9
    finished = False
    PrintBoard(board)

    while not finished: # Take turns until the game is over
        for player in range(1, 3):
            if player == 1:
                board = Turn(board) # Player takes one turn
            elif player == 2:
                board = bot.Turn(bot, board)
            PrintBoard(board) # Print if neither victory nor tie are achieved
            result = CheckBoard(board) # Check the board for victory or tie
            if result == 1: # Victory
                if player == 1:
                    print("You win!")
                else:
                    print("You lose!")
                finished = True
                break
            elif result == 2: # Tie
                print("It's a tie!")
                finished = True
                break

if __name__ == "__main__":
    bot = Simple
    Main(bot)