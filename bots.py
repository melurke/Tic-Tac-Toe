# Coordinates:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Empty: 0
# Player (X): 1
# Computer (O): -1

import random
from termcolor import colored

class Random: # Makes a random move
    def Turn(self, board):
        emptyTiles = []
        for tile in board:
            if tile == 0:
                emptyTiles.append(tile)
        
        randomTile = random.choice(emptyTiles)
        board[randomTile] = -1
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
            elif tile == -1:
                botTiles.append(i)
        for tile in emptyTiles:
            newBoard = board.copy()
            newBoard[tile] = -1
            if CheckBoard(newBoard) == 1:
                board[tile] = -1
                return board
            newBoard[tile] = 1
            if CheckBoard(newBoard) == 1:
                board[tile] = -1
                return board
        randomTile = random.choice(emptyTiles)
        board[randomTile] = -1
        return board

class Perfect:
    def Turn(self, board):
        calculation = self.Minimax(self, board, -1)
        print(calculation)
        board[calculation[1]] = -1
        return board
    
    def Minimax(self, board, player):
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

        for i in range(9):
            if board[i] == 0:
                board[i] = player
                moveScore = - self.Minimax(self, board, -player)[0]
                board[i] = 0
                if moveScore > score:
                    score = moveScore
                    move = i
        if move == -1:
            return 0, 9
        return score, move

def CheckBoard(board): # Check if the game is won or if it's a tie
    # Check if the game is won
    possibleSolutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for solution in possibleSolutions:
        fields = []
        for field in solution:
            fields.append(board[field])
        if len(list(dict.fromkeys(fields))) == 1 and fields[0] != 0:
            return fields[0]
    
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
        for player in [1, -1]:
            if player == 1:
                board = Turn(board) # Player takes one turn
            elif player == -1:
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
    bot = Perfect
    Main(bot)