# Max Connect 4 Using AI

This program is an attempt to implement an agent that plays the Max-Connect4 game using search where the game is over when all positions are occupied. Obviously, every complete game consists of 42 moves, and each player makes 21 moves. 
The score, at the end of the game is determined as follows: consider each quadruple of four consecutive positions on board, either in the horizontal, vertical, or each of the two diagonal directions (from bottom left to top right and from bottom right to top left). The red player gets a point for each such quadruple where all four positions are occupied by red pieces. Similarly, the green player gets a point for each such quadruple where all four positions are occupied by green pieces. The player with the most points wins the game.

The program will run in two modes: 
> **interactive mode**, that is best suited for the program playing against a human player.

> **one-move mode**, where the program reads the current state of the game from an input file, makes a single move, and writes the resulting state to an output file. The one-move mode can be used to make programs play against each other.

# Code Structure

> The class minimax performs the decision making. Contains methods makedecision() which returns minimax's decision, maxvlue() which performs maximizing operations, minvalue() which performs minimizing operations, and utility() which returns the utility that needs to be maximized or minimized.

> result() calculates the new state after a particular move

> possiblemoves() returns the moves that are possible on a state

# Compilation and Execution

To run the code, execute maxconnect4.py with standard python compilation commands.

For **interactive mode**, pass the following arguments:
> python maxconnect4.py interactive <input_file> <computer-next/human-next> <depth>

For **one-move mode**, pass the following arguments:
> python maxconnect4.py one-move <input_file> <output_file> <depth>	
	

