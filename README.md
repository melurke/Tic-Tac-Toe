# Tic-Tac-Toe

This is just a little side project about the popular game Tic-Tac-Toe.
There are several little programs where you can play the game against another player or against some bots.

## How the game works

In the normal version of this game, there is a 3x3 field where the players take turns in chosing one field where they place their tile. Player 1 has an X and player 2 has an O. The first player to get three of their own tiles to align wins.

A typical board can look like this:

"- | - | X"

"O | X | X"

"O | - | O"

If both players play perfectly from this point on, the game is a tie.

The standard version of the game can be played with the file game.py

### Different board sizes

With the file nxn.py one can also play the game with different board sizes. At the beginning, one can chose the length of the board at will.

The rules are pretty much the same, but now to win one has to align n tiles.

Example with 4x4:

"X | - | - | O"

"O | X | O | -"

"- | X | O | -"

"- | - | X | -"


## Bots

I tried to program a couple of different bots. Their nothing special and just the standard bots one would consider to program in a project like this.

### Random bot

As the name suggests, this bot just makes a random legal move. Nothing special to see here.

### Simple bot

This bot is a bit more complicated, though still easy to understand.

If it is possible for this bot to win in one move, the bot makes that move.

And if you, the player, could win in the next move if the bot isn't careful, it tries to stop this.

This bot can still be beat pretty easily with the right strategy, if there are two possible moves for the player to win, the bot can only prevent one of them, so you are still able to win.

An example for this kind of situation can look like this:

"X | - | -"

"- | X | -"

"X | O | O"


In this situation, the bot (O) can't do anything to stop the player (X) from winning in the next move.

### Perfect bot

This bot plays in the best way possible. This is achieved by using the Minimax-algorith to search through all possible future stages of the game to find out the best move.