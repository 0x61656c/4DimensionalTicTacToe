from tkinter import *
import math
from TicTacToeClasses import *
import copy
import random

def init(data):
    #window dimension data
    data.width = 500
    data.height = 500
    data.margin = 100
    
    data.delta1 = 0
    data.delta2 = 0
    data.time = 0
    #textcolor for menu items
    data.textColor = "orange"
    
    data.emptyBoard = [[0,0,0],
                       [0,0,0],
                       [0,0,0]]
                  
    data.sideLength = 100
    
    data.game = TicTacToe2D()
    
    #gamestate data
    data.statelist = ['start', 'options', 'menu1',
                      'paused', 'in progress', 'over']
                      
    data.gameState = 'start'
    
    #gamemode selection data
    data.modeList = ['2D','3D','4D']
    data.mode = ''
    #data.game = ''
    
    #click location data
    data.xclick = 0
    data.yclick = 0
    
def mousePressed(event, data):
    #feeds click data into data structure
    data.xclick = int(event.x)
    #print(data.xclick)
    data.yclick = int(event.y)
    #print(data.yclick)
    
    #start menu click directions
    if data.gameState == 'start' and\
    data.xclick in range(int(data.width/2) - 100, int(data.width/2) + 100) and\
    data.yclick in range(data.height - 100, data.height - 50):
         data.gameState = 'menu1'
        
    #menu 1 click directions
    if data.gameState == 'menu1' and\
    data.xclick in range(int(data.width/2) -100, int(data.width/2) + 100) and\
    data.yclick in range(int(data.height/2)-85, int(data.height/2) - 35):
        data.switch = 'in progress'
        data.mode = '2D'
         
         
    if data.gameState == 'in progress':
        if data.mode == '2D':
            if data.xclick in range(100,200) and data.yclick in range(100,200):
                data.game.makeMove(0,0)
                
            elif data.yclick in range(200,300) and data.xclick in range(100,200):
                data.game.makeMove(1,0)
                
            elif data.yclick in range(300,400) and data.xclick in range(100,200):
                data.game.makeMove(2,0)
           
            elif data.yclick in range(100,200) and data.xclick in range(200,300):
                data.game.makeMove(0,1)
                
            elif data.yclick in range(100,200) and data.xclick in range(300,400):
                data.game.makeMove(0,2)
            
            elif data.yclick in range(200,300) and data.xclick in range(200,300):
                data.game.makeMove(1,1)
                
            elif data.yclick in range(300,400) and data.xclick in range(300,400):
                data.game.makeMove(2,2) 
                
            elif data.yclick in range(200,300) and data.xclick in range(300,400):
                data.game.makeMove(1,2)
                
            elif data.yclick in range(300,400) and data.xclick in range(200,300):
                data.game.makeMove(2,1)
            
            print(data.game)
           
def keyPressed(event, data):
    if data.gameState == 'over':
        if event.keysym == 'space':
            data.game = TicTacToe2D(copy.deepcopy(data.emptyBoard))
            data.gameState = 'menu1'
            data.mode = ''
    
def timerFired(data):
    data.time += 1
    if data.mode == '2D':
        data.gameState = 'in progress'
        
        
        if data.gameState == 'in progress':
            if data.game.checkWinner() or data.game.boardFull():
                data.gameState = 'over'
    
    if data.time % 100 == 0:
        data.delta1 = random.randint(10,20)
        data.delta2 = random.randint(50,150)
    
###
#Draw Functions
###

def drawStart(canvas, data):

    # canvas.create_text(
    # data.width / 2,
    # data.height / 3,
    # text = """N-Dimensional 
    # Tic Tac Toe""",
    # font = "Helvetica 36 bold",
    # fill = "Black")
    
    canvas.create_text(
    data.width / 2,
    data.height / 3,
    text = """N-Dimensional 
    Tic Tac Toe""",
    font = "Helvetica 35 bold",
    fill = data.textColor)
    
    canvas.create_rectangle(
    data.width/2 - 100,
    data.height - 50,
    data.width/2 + 100, 
    data.height - 100,
    width = 4,
    outline = 'white'
    )
    
    # canvas.create_text(
    # data.width / 2,
    # data.height - 75,
    # text = "Start",
    # font = "Helvetica 36 bold",
    # fill = "Black")
    
    canvas.create_text(
    data.width / 2,
    data.height - 75,
    text = "Start",
    font = "Helvetica 34 bold",
    fill = data.textColor)
    
def drawMenu1(canvas, data):
    
    canvas.create_rectangle(
    data.width/2 -100,
    data.height/2 - 85,
    data.width/2 + 100,
    data.height/2 - 35,
    width = 4,
    outline = 'white')
    
    canvas.create_rectangle(
    data.width/2 -100,
    data.height/2 - 25,
    data.width/2 + 100,
    data.height/2 + 25,
    width = 4,
    outline = 'white')
    
    canvas.create_rectangle(
    data.width/2 -100,
    data.height/2 + 35,
    data.width/2 + 100,
    data.height/2 + 85,
    width = 4,
    outline = 'white')
    
    # canvas.create_text(
    # data.width/2,
    # data.height/2 - 60,
    # text = "2D",
    # fill = "Black",
    # font = "Helvetica 26 bold")
    # 
    canvas.create_text(
    data.width/2,
    data.height/2 - 60,
    text = "2D",
    fill = data.textColor,
    font = "Helvetica 24 bold")


def drawTicTacToeBoard(canvas, data, size = 100, margin = 100):
    for row in range(len(data.emptyBoard)):
        for col in range(len(data.emptyBoard[0])):
            canvas.create_rectangle(
            margin + size * row,
            margin + size * col, 
            margin + size * (row + 1),
            margin + size * (col + 1),
            outline = 'white',
            width = 6)
            
def drawEx(canvas, data, col, row): #notice that row and col are switched!
    canvas.create_rectangle(
    data.sideLength * (row + 1) + 3,
    data.sideLength * (col+ 1) +3,
    data.sideLength * (row + 2) - 3,
    data.sideLength * (col + 2) -3,
    fill = "orange")

def drawOh(canvas, data, col, row): #notice that row and col are switched!
    canvas.create_rectangle(
    data.sideLength * (row + 1) + 3,
    data.sideLength * (col+ 1) + 3,
    data.sideLength * (row + 2) - 3,
    data.sideLength * (col + 2)- 3,
    fill = "yellow")
            
            
def drawPieces(canvas, data):
    for row in range(len(data.game.board)):
        for col in range(len(data.game.board[0])):
            if data.game.board[row][col] == 1:
                drawEx(canvas, data, row , col)
            elif data.game.board[row][col] == 2:
                drawOh(canvas, data, row, col)
        
def draw2dGUI(canvas, data):
   
    # canvas.create_text(
    # data.width/2, 
    # data.margin / 2,
    # text = "2D Tic Tac Toe",
    # font = "Helvetica 24 bold")
    
    canvas.create_text(
    data.width/2, 
    data.margin / 2,
    text = "2D Tic Tac Toe",
    font = "Helvetica 23 bold",
    fill = data.textColor)

def draw2DInProgress(canvas, data):
    draw2dGUI(canvas, data)
    drawTicTacToeBoard(canvas, data)

def drawEndScreen(canvas, data):
    
    # canvas.create_text(
    # data.width/2,
    # data.height - data.sideLength/2 - 10,
    # text = '--Game Over--',
    # font = "Helvetica 20 bold",
    # fill = "black")
    
    
    canvas.create_text(
    data.width/2,
    data.height - data.sideLength/2 - 10,
    text = '--Game Over--',
    font = "Helvetica 19 bold",
    fill = data.textColor)
    
    
    currentplayer = str((data.game.turn + 1)%2 + 1)
    
  
    if data.game.checkWinner():

        canvas.create_text(
        data.width/2,
        data.height - data.sideLength/2 + 10,
        text = 'Player %s wins!' %currentplayer,
        font = "Helvetica 20",
        fill = "black")
        
        canvas.create_text(
        data.width/2,
        data.height - data.sideLength/2 + 10,
        text = 'Player %s wins!' %currentplayer,
        font = "Helvetica 19",
        fill = data.textColor)

    else:
        canvas.create_text(
        data.width/2,
        data.height - data.sideLength/2 + 10,
        text = 'Draw!',
        font = "Helvetica 20",
        fill = "black")
        
        canvas.create_text(
        data.width/2,
        data.height - data.sideLength/2/ + 10,
        text = 'Draw!',
        font = "Helvetica 19",
        fill = data.textColor)
    
    canvas.create_text(
    data.width/2,
    data.height - data.sideLength/2 + 35,
    text = "Press Space to return to menu",
    font = "Helvetica 12",
    fill = data.textColor)
            
def redrawAll(canvas, data):
    if data.gameState == 'start':
        drawStart(canvas, data)
        #drawTicTacToeBoard(canvas, data, data.delta1, data.delta2)
    
    if data.gameState == 'menu1':
        drawMenu1(canvas, data)
        
    if data.gameState == 'in progress' and data.mode == '2D':
        draw2DInProgress(canvas, data)
        drawPieces(canvas, data)
        
    if data.gameState == 'over':
        draw2DInProgress(canvas, data)
        drawPieces(canvas, data)
        drawEndScreen(canvas, data)

    

####
#Run function and Wrapper
####

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
###
#Main function
###

def main():
    run()

if __name__ == "__main__":
    main()