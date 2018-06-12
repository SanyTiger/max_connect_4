import max_connect_4

class gameboard(object):
    """description of class"""

    def __init__(self):
        self.playBoard = [[0 for x in range(max_connect_4.max_connect_4.rows)] for y in range(max_connect_4.max_connect_4.columns)]
        self.pieceCount = 0
        self.counter = 0
        self.gameData = ""
        self.currentTurn = 0
        self.computerFirst = True
    #endmethod


    def exitBoard(self, errorNumber):
        print("Error! Exiting game, error value = \n%d", errorNumber)
        sys.exit(errorNumber)
    #endmethod


    def getCurrentTurn(self):
        return (self.pieceCount % 2) + 1
    #endmethod


    def startboard(self, inputFile):
        try:
            file1 = open(inputFile, 'r')
        except IOError:
            sys.exit("\nError opening input file.\nCheck file name.\n")

        # Read the initial game state from the file and save in a 2D list
        fileLines = file1.readlines()
        self.playBoard = [[int(char) for char in line[0:7]] for line in fileLines[0:-1]]
        self.currentTurn = int(fileLines[-1][0])
        file1.close()

        print '\nMaxConnect-4 game\n'
        print 'Game state before move:'
        self.printBoard()
        self.counter = 0
        return self.playBoard
    #endmethod


    def board(self, master):
        self.playBoard = [[0 for x in range(max_connect_4.max_connect_4.rows)] for y in range(max_connect_4.max_connect_4.columns)]
        self.pieceCount = 0
        for i in range(max_connect_4.max_connect_4.rows):
            for j in range(max_connect_4.max_connect_4.columns):
                self.playBoard[i][j] = master[i][j]
                if int(self.playBoard[i][j]) > 0:
                    self.pieceCount = self.pieceCount + 1
                #endif
            #endfor
        #endfor
    #endmethod


    def getScore(self, player):
        self.score = 0

        # Check horizontally across rows
        for i in range(max_connect_4.max_connect_4.rows):
            for j in range(4):
                if int(self.playBoard[i][j]) == player and int(self.playBoard[i][j + 1]) == player and int(self.playBoard[i][j + 2]) == player and int(self.playBoard[i][j + 3]) == player:
                    self.score = self.score + 1
            #endfor
        #endfor

        # Check vertically across columns
        for i in range(3):
            for j in range(max_connect_4.max_connect_4.columns):
                if int(self.playBoard[i][j]) == player and int(self.playBoard[i + 1][j]) == player and int(self.playBoard[i + 2][j]) == player and int(self.playBoard[i + 3][j]) == player:
                    self.score = self.score + 1
            #endfor
        #endfor

        # Check diagonally across the matrix -> \ Back Slash
        for i in range(3):
            for j in range(4):
                if int(self.playBoard[i][j]) == player and int(self.playBoard[i + 1][j + 1]) == player and int(self.playBoard[i + 2][j + 2]) == player and int(self.playBoard[i + 3][j + 3]) == player:
                    self.score = self.score + 1
            #endfor
        #endfor

        # Check diagonally across the matrix -> / Forward Slash
        for i in range(3):
            for j in range(4):
                if int(self.playBoard[i + 3][j]) == player and int(self.playBoard[i + 2][j + 1]) == player and int(self.playBoard[i + 1][j + 2]) == player and int(self.playBoard[i][j + 3]) == player:
                    self.score = self.score + 1
            #endfor
        #endfor
        return self.score
    #endmethod


    def isValidMove(self, column):
        # Check column bounds
        if not int(column) >= 0 and not int(column) <= 7:
            return False;
        #endif

        # Check if column is full
        elif int(self.playBoard[0][column]) > 0:
            return False
        #endif
        else:
            return True
        #endif
    #endmethod


    def getCurrentBoard(self):
        return int(self.playBoard)
    #endmethod


    def getPieceCount(self):
        return int(self.pieceCount)
    #endmethod


    def movePiece(self, column):
        column = int(column)
        if not self.isValidMove(column):
            return False
        #endif
        else:
            for i in range(5, 0, -1):
                if int(self.playBoard[i][column]) == 0:
                    if int(self.pieceCount) % 2 == 0:
                        self.playBoard[i][column] = 1
                        self.pieceCount = self.pieceCount + 1
                    #endif
                    else:
                        self.playBoard[i][column] = 2
                        self.pieceCount = self.pieceCount + 1
                    #endif
                    return True
                #endif
            #endfor

            # Incase of error
            print("Error! Check sub routine movePiece()")
            return False
        #endif
    #endmethod


    def setComputerFirst(self, isFirst):
        self.computerFirst = isFirst
    #endmethod


    def printBoard(self):
        print("-------------")
        for i in range(max_connect_4.max_connect_4.rows):
            print("|")
            for j in range(max_connect_4.max_connect_4.columns):
                print(self.playBoard[i][j])
                print(" ")
            #endfor
            print("| ")
        #endfor
        print("------------")
    #endmethod


    def printBoardToFile(self, outputFile):
        try:
            with open(outputFile, 'w') as theFile:
                for i in range(6):
                    for j in range(7):
                        theFile.write(int(self.playBoard[i][j]))
                    #endfor
                    theFile.write("\r\n")
                #endfor

                # Write current file
                theFile.write(self.getCurrentTurn() + "\r\n")
            #endwith
        #endtry
        except Exception as e:
            print(e)
            self.exitBoard(3)
        raise e
    #endmethod








