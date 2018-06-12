import max_connect_4
import gameboard
import copy

class alphabeta_minmax:
	def __init__(self, game, depth):
		self.currentTurn = game.currentTurn
		self.game = game
		self.maxDepth = int(depth)
    #endmethod

		
	def takedecision(self):
		minValues = []
		possiblemove = possiblemoves(self.game.gameBoard)
		for move in possiblemove:
			value = result(self.game, move)
			minValues.append(self.minvalue(value, 99999, -99999))
        #endfor
		chosen = possiblemove[minValues.index(max(minValues))]
		return chosen
    #endmethod


	def minvalue(self, state, alpha, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
			return self.utility(state)
        #endif
		v = 99999
		for move in possiblemoves(state.gameBoard):
			newState = result(state, move)
			v = min(v, self.maxvalue(newState, alpha, beta))
			if v <= alpha:
				return v
            #endif
			beta = min(beta, v)
        #endif
		return v
    #endmethod

		
	def maxvalue(self, state, alpha, beta):
		if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
			return self.utility(state)
        #endif
		v = -99999
		for move in possiblemoves(state.gameBoard):
			newState = result(state, move)
			v = max(v, self.minvalue(newState, alpha, beta))
			if v >= beta:
				return v
            #endif
			alpha = max(alpha, v)
        #endfor
		return v
    #endmethod


	def utility(self, state):
		if self.currentTurn == 1:
			utility = state.player1Score * 2 - state.player2Score
        #endif
		elif self.currentTurn == 2:
			utility = state.player2Score * 2 - state.player1Score
        #endif
		return utility
    #endmethod


def possiblemoves(board):
    possiblemoves = []
    for col, colVal in enumerate(board[0]):
        if colVal == 0:
            possiblemoves.append(col)
        #endif
    #endfor
    return possiblemoves
#endmethod


def result(oldGame, column):
    newGame = max_connect_4.max_connect_4()
    try:
        newGame.nodeDepth = oldGame.nodeDepth + 1
    #endtry
    except AttributeError:
        newGame.nodeDepth = 1
    #endexcept
    newGame.pieceCount = oldGame.pieceCount
    newGame.gameBoard = copy.deepcopy(oldGame.gameBoard)
    if not newGame.gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not newGame.gameBoard[i][column]:
                newGame.gameBoard[i][column] = oldGame.currentTurn
                newGame.pieceCount += 1
                break
            #endif
        #endfor
    #endif
    if oldGame.currentTurn == 1:
        newGame.currentTurn = 2
    #endif
    elif oldGame.currentTurn == 2:
        newGame.currentTurn = 1
    #endif
    newGame.checkPieceCount()
    newGame.countScore()
    return newGame
#endmethod



