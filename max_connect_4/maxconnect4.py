import sys
from max_connect_4 import *
from alphabeta_minmax import *

def onemovegame(currentGame, depth):
    # Check if board is full
    if currentGame.pieceCount == 42:
        print ("The Board Is Full!\n\nGame Over!\n")
        sys.exit(0)
    #endif
    searchTree = alphabeta_minmax(currentGame, depth)
    nextMove = searchTree.takedecision()
    result = currentGame.PlayPiece(nextMove)
    aftermoveoperations(currentGame,nextMove)
    currentGame.gameFile.close()
#endmethod


def interactivegame(currentGame, depth):
    while not currentGame.pieceCount == 42:
        if currentGame.currentTurn == 1:
            userMove = input("Enter the column number [1-7] where you would like to play : ")
            if not userMove:
                print ("Invalid column number!\n")
                continue
            #endif
            if userMove == 99:
                sys.exit('Player1 forfits!\n\n Computer Wins!\n')
            if not 0 < userMove < 8:
                print ("Invalid column number!\n")
                continue
            #endif
            if not currentGame.PlayPiece(userMove - 1):
                print ("This column is full!\n")
                continue
            #endif
            try:
                currentGame.gameFile = open("human.txt", 'w')
            #endtry
            except:
                sys.exit('Error opening output file.')
            #endexcept
            aftermoveoperations(currentGame, userMove - 1)

        elif not currentGame.pieceCount == 42:
            searchTree = alphabeta_minmax(currentGame, depth)
            nextMove = searchTree.takedecision()
            result = currentGame.PlayPiece(nextMove)
            try:
                currentGame.gameFile = open("comupter.txt", 'w')
            #endtry
            except:
                sys.exit('Error opening output file.')
            #endexcept
            aftermoveoperations(currentGame, nextMove)
        #endif
    #endwhile
    currentGame.gameFile.close()

    if currentGame.player1Score > currentGame.player2Score:
        print "Player 1 wins"
    #endif
    elif currentGame.player2Score > currentGame.player1Score:
        print "Computer wins"
    #endif
    else:
        print "It's a draw"
    #endif
    print "Thank you for playing MaxConnect4Game!\n"
#endmethod


def aftermoveoperations(currentGame, move):    
    print("\n\nMove Number: %d,\t Player: %d,\t Column: %d\n" % (currentGame.pieceCount, currentGame.currentTurn, move + 1)),
    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    #endif
    elif currentGame.currentTurn == 2:
        currentGame.currentTurn = 1
    #endif
    print ("Game State After Move:\n")
    currentGame.printGameBoard()
    currentGame.countScore()
    print("Scores\n Player 1: %d,\t Player 2: %d\n" % (currentGame.player1Score, currentGame.player2Score))
    currentGame.printGameBoardToFile()
#endmethod


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)
    #endif

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)
    #endif

    currentGame = max_connect_4.max_connect_4() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    #endtry
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")
    #endexcept

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:\n'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == 'computer-next': #override current turn according to commandline arguments
            currentGame.currentTurn = 2
        #endif
        else: #human-next
            currentGame.currentTurn = 1
        #endif
        interactivegame(currentGame,argv[4]) # Be sure to pass whatever else you need from the command line
    #endif
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        #endtry
        except:
            sys.exit('Error opening output file.')
        #endexcept
        onemovegame(currentGame, argv[4]) # Be sure to pass any other arguments from the command line you might need.
    #endif
#endmethod



if __name__ == '__main__':
    main(sys.argv)
