import neat
import os
import random
from termcolor import colored
from time import sleep

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    p = neat.Checkpointer.restore_checkpoint("neat-data/5290")

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(Game, 1)

    print('\nBest genome:\n{!s}'.format(winner))
    input()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        SingleGame(Random, neat.nn.FeedForwardNetwork.create(winner, config), True)

def Mean(lst):
    return sum(lst) / len(lst)

class Random:
    def Turn(board):
        validTurn = False
        while not validTurn:
            turn = random.randint(0, 8)
            validTurn = board[turn] == 0
        board[turn] = 2
        return board

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

def Turn(board, net): # One player takes a turn and the board gets updated
    inputs = tuple(board)
    output = net.activate(inputs)[0]
    field = (output + 1) * 9/2
    field = int(field - (field % 1))
    if field == 9:
        field = 8
    
    if board[field] != 0:
        return board, False
    board[field] = 1
    return board, True

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
    sleep(1)

def SingleGame(bot, net, printGame):
    board = [0] * 9
    finished = False
    if printGame:
        PrintBoard(board)

    while not finished: # Take turns until the game is over
        for player in range(1, 3):
            if player == 1:
                board, validTurn = Turn(board, net) # Player takes one turn
                if not validTurn:
                    return -2
            elif player == 2:
                board = bot.Turn(board)
            if printGame:
                PrintBoard(board) # Print if neither victory nor tie are achieved
            result = CheckBoard(board) # Check the board for victory or tie
            if result == 1: # Victory
                if player == 1:
                    if printGame:
                        print("You win!\n\n\n")
                    return 1
                else:
                    if printGame:
                        print("You lose!\n\n\n")
                    return -1
            elif result == 2: # Tie
                print("It's a tie!\n\n\n")
                return 0

def Game(genomes, config):
    bot = Random
    for g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g[1], config)
        fitness = 0
        for i in range(50):
            fitness += SingleGame(bot, net, False)

        g[1].fitness = fitness

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)