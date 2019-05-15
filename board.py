import time
import numpy as np

class Board(object):
    BOARD_SIZE = 4 # 0 indexed

    #moves
    SLIDE_LEFT = 0
    SLIDE_UP = 1
    SLIDE_RIGHT = 2
    SLIDE_DOWN = 3

    #Piece Values
    BLANK = 0
    X = 1
    O = 2

    def __init__(self,board=None,turn = 1):
        if(board == None):
            self.board = np.zeros((self.BOARD_SIZE + 1,self.BOARD_SIZE + 1),dtype=int)
            self.turn = turn
        else:
            self.board = np.reshape(board,(5,5))
            self.turn = turn

    def play(self,piece,move):
        legalMove = self.checkMove(piece,move)
        if(not legalMove):
            pass

        self.board[piece] = self.turn
        self.shift(piece,move)
        self.changeTurn()

    def checkMove(self,piece,move):
        #Only blank and owned pieces
        if(not (self.board[piece] == self.BLANK or self.board[piece] == self.turn)):
            return False

        if(0 < piece[0] < self.BOARD_SIZE and 0 < piece[1] < self.BOARD_SIZE):
            return False

        possibleMoves = self.getPossiblePieceMoves(piece)
        if(move in possibleMoves):
            return True
        else:
            return False

    def shift(self,piece,move):
        row,col = piece

        if(move == self.SLIDE_RIGHT):
            self.board[row,0:col + 1] = np.roll(self.board[row,0:col + 1],1)
        elif(move == self.SLIDE_LEFT):
            self.board[row,col:self.BOARD_SIZE + 1] = np.roll(self.board[row,col:self.BOARD_SIZE + 1],-1)
        elif(move == self.SLIDE_UP):
            self.board[row:self.BOARD_SIZE + 1,col] = np.roll(self.board[row:self.BOARD_SIZE + 1,col],-1)
        else:
            self.board[0:row + 1,col] = np.roll(self.board[0:row + 1,col],1)

        return

    def changeTurn(self):
        if(self.turn == self.X):
            self.turn = self.O
        else:
            self.turn = self.X

    def isGameEnd(self):
        firstDiagonal = np.diagonal(self.board)
        secondDiagonal = np.diagonal(np.rot90(self.board))

        if(np.all(firstDiagonal == self.X) or np.all(firstDiagonal == self.O)):
            return self.board[0,0]
        if(np.all(secondDiagonal == self.X) or np.all(secondDiagonal == self.O)):
            return self.board[0,self.BOARD_SIZE]
        
        for i in range(0,self.BOARD_SIZE + 1):
            row = self.board[i,:]
            col = self.board[:,i]
            if(np.all(row == self.X) or np.all(row == self.O)):
                return self.board[i,0]
            if(np.all(col == self.X) or np.all(col == self.O)):
                return self.board[0,i]
        
        return 0
      
    def getPossiblePieceMoves(self,piece):
        row,col = piece
        possibleMoves = []

        if(row < self.BOARD_SIZE):
            possibleMoves.append(self.SLIDE_UP)
        if(row > 0):
            possibleMoves.append(self.SLIDE_DOWN)
        if(col < self.BOARD_SIZE):
            possibleMoves.append(self.SLIDE_LEFT)
        if(col > 0):
            possibleMoves.append(self.SLIDE_RIGHT)

        return possibleMoves

    def getPossibleMoves(self):
        if(self.turn == self.X):
            opponent = self.O 
        else:
            opponent = self.X

        edgeMatrix = np.full((self.BOARD_SIZE + 1,self.BOARD_SIZE + 1),opponent)
        edgeMatrix[0,:] = self.board[0,:]
        edgeMatrix[self.BOARD_SIZE,:] = self.board[self.BOARD_SIZE,:]
        edgeMatrix[:,0] = self.board[:,0]
        edgeMatrix[:,self.BOARD_SIZE] = self.board[:,self.BOARD_SIZE]

        edgeIndices = np.where(edgeMatrix != opponent)
        edgeIndices = np.column_stack((edgeIndices[0],edgeIndices[1]))
        allMoves = []
        for piece in edgeIndices:
            piece = (piece[0],piece[1])
            moves = self.getPossiblePieceMoves(piece)
            for move in moves:
                allMoves.append((piece,move))

        np.random.shuffle(allMoves)

        return allMoves      

    def printTurn(self):
        if(self.turn == self.X):
            print("Turn: X")
        else:
            print("Turn: O")

    def printBoard(self):            
        def valToChar(x):
            if(x == 0):
                return '-'
            elif(x == 1):
                return 'X'
            else:
                return 'O'
        print(np.array2string(self.board,formatter = {'all': valToChar}))
        print()

    def printWinner(self):
        if(self.turn == Board.X):
            print("Winner is X")
        elif(self.turn == Board.O):
            print("Winner is O")

    def directionToText(self,direction):
        if(direction == 0):
            return "SLIDE_LEFT"
        elif(direction == 1):
            return "SLIDE_UP"
        elif(direction == 2):
            return "SLIDE_RIGHT"
        elif(direction == 3):
            return "SLIDE_DOWN"

    def serialize(self):
        return self.board
        # b_size = (self.BOARD_SIZE + 1) ** 2
        # feauture_vector_size = b_size + 0 # 5x5 + 1 for turn
        # fv = np.zeros(feauture_vector_size)
        # fv[0:b_size] = np.ravel(self.board)
        # fv[-1] = self.turn * 1.0
        # return fv
        # k = np.ravel(self.board)
        # return ''.join([str(i) for i in k.tolist()])