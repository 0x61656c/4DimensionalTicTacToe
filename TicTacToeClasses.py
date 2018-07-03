
###
#2d Tic Tac toe for nDimensional Tic Tac Toe
###

def checkEqual(list):
    return list[1:] == list[:-1]
    
class TicTacToe2D(object):
    def __init__(self, board = [[0,0,0],
                                [0,0,0],
                                [0,0,0]], turn = 0):
        self.board = board
        self.turn = turn 
        
    def __repr__(self):
        titleString = """2D game: turn number = %i""" %self.turn
        newline = """
        """
        boardString = "board : " + str(self.board)
        return titleString + newline + boardString
        
    def __hash__(self):
        return hash(self.board)
    
    def __eq__(self, other):
        return self.board == other.board and self.turn == other.turn
            
    def turnNumber(self):
        return self.turn
    
    def isLegalMove(self,row,col):
        return self.board[row][col] == 0
    
    def makeMove(self,row,col):
        if self.isLegalMove(row,col):
            if not self.turn % 2 == 0:
                self.board[row][col] = 1
            else: self.board[row][col] = 2
            self.turn += 1
        else: pass
        
    def showBoard(self):
       return self.board
    
    def boardFull(self):
        return self.turn == 9
       
    def checkWinner(self):
        
        for row in self.board:
            if 0 not in set(row):
                if checkEqual(row):
                    return True
                
        for i in range(len(self.board)):
            check = []
            check += (row[i] for row in self.board)
            
            if 0 not in set(check):
                if checkEqual(check):
                    return True
                else: 
                    continue
        
        diagonalList1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonalList2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        
        if not 0 in diagonalList1:
            if checkEqual(diagonalList1):
                return True
        
        if not 0 in diagonalList2:
            if checkEqual(diagonalList2):
                return True
        
        
        return False

def test2dTicTacToe(): 
    print("Testing Tic Tac Toe...")
    
    t1 = TicTacToe2D()
    print(t1)
    t1.makeMove(0,0)
    print(t1)
    t1.makeMove(0,1)
    print(t1)
    t1.makeMove(1,1)
    print(t1)
    t1.makeMove(1,0)
    print(t1)
    t1.makeMove(2,2)
    print(t1)
    assert(t1.checkWinner() == True)
    
    t2 = TicTacToe2D()
    t2.makeMove(0,2)
    t2.makeMove(1,0)
    t2.makeMove(1,1)
    t2.makeMove(0,1)
    t2.makeMove(2,0)
    assert(t2.checkWinner() == True)
    
    t3 = TicTacToe2D()
    t3.makeMove(1,0)
    t3.makeMove(0,2)
    t3.makeMove(1,1)
    t3.makeMove(0,1)
    t3.makeMove(2,0)
    assert(t3.checkWinner() == True)
    
    t4 = TicTacToe2D()
    print(t4)
    t4.makeMove(0,1)
    print(t4)
    t4.makeMove(0,2)
    print(t4)
    t4.makeMove(0,0)
    print(t4)
    print(t4.checkWinner())
    
    print("...Passed!")

def main():
    #test2dTicTacToe()
    pass
    
if __name__ == "__main__":
    main()
                    