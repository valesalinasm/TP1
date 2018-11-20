from image_util import*
from tkinter import*

class Character(object):
    def __init__(self,r=11):
        self.r= r
        self.dcx=25.5
    def moveRight(self):
        self.cx+=self.dcx
    def moveLeft(self):
        self.cx-=self.dcx
    def moveUp(self):
        self.cy-=(self.r*2)
    def moveDown(self):
        self.cy+=(self.r*2)

class Scarlet(Character):
    def __init__(self,r=11):
        super().__init__(r)
        self.cx = 456
        self.cy = 32
    def draw(self, canvas, color="red"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
class White(Character):
    def __init__(self):
        super().__init__()
        self.cx = 404.40
        self.cy = 614.58
    def draw(self, canvas, color="white"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
class Peacock(Character):
    def __init__(self):
        super().__init__()
        self.cx = 49
        self.cy = 472.92
    def draw(self, canvas, color="blue"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
class Plum(Character):
    def __init__(self):
        super().__init__()
        self.cx = 49
        self.cy = 156.25
    def draw(self, canvas, color="purple"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
class Green(Character):
    def __init__(self):
        super().__init__()
        self.cx = 278
        self.cy = 614.58
    def draw(self, canvas, color="green"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
class Mustard(Character):
    def __init__(self):
        super().__init__()
        self.cx = 635.48
        self.cy = 202.08
    def draw(self, canvas, color="yellow"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)


def init(data):
    #in order to be able to have images be shown I had to take the code given to
    #us to do homework 6// http://www.cs.cmu.edu/~112/notes/hw6.html
    data.clueBoard=PhotoImage(file="images/clueBoard.gif")
    data.mode="choose"
    data.xCoordsChoose=data.width/5
    data.yCoordsChoose=data.height/4
    data.numPlayers=0
    data.players=[]
    data.character=Scarlet()

#the outline for the next code was taken from the animation mode demo given
#to us in the 112 website: 
#http://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
def mousePressed(event, data):
    if (data.mode == "choose"): chooseMousePressed(event, data)
    elif (data.mode == "players"): playersMousePressed(event, data)
    elif (data.mode == "gameScreen"): gameScreenMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "choose"): chooseKeyPressed(event, data)
    elif (data.mode == "players"): playersKeyPressed(event, data)
    elif (data.mode == "gameScreen"): gameScreenKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "choose"): chooseTimerFired(data)
    elif (data.mode == "players"): playersTimerFired(data)
    elif (data.mode == "gameScreen"): gameScreenTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "choose"): chooseRedrawAll(canvas, data)
    elif (data.mode == "players"): playersRedrawAll(canvas, data)
    elif (data.mode == "gameScreen"): gameScreenRedrawAll(canvas, data)

##choose Mode##
def chooseMousePressed(event, data):
    if data.xCoordsChoose<event.x<data.xCoordsChoose*2 and \
        data.yCoordsChoose<event.y<data.yCoordsChoose*2:
        numPlayers=3
        for i in range(1,numPlayers+1):
            data.players.append(i)
        data.mode="players"
        
    if data.xCoordsChoose*3<event.x<data.xCoordsChoose*4 and \
        data.yCoordsChoose<event.y<data.yCoordsChoose*2:
        numPlayers=4
        for i in range(1,numPlayers+1):
            data.players.append(i)
        data.mode="players"
    
    if data.xCoordsChoose<event.x<data.xCoordsChoose*2 and \
        data.yCoordsChoose*2.5<event.y<data.yCoordsChoose*3.5:
        numPlayers=5
        for i in range(1,numPlayers+1):
            data.players.append(i)
        data.mode="players"
    
    if data.xCoordsChoose*3<event.x<data.xCoordsChoose*4 and \
        data.yCoordsChoose*2.5<event.y<data.yCoordsChoose*3.5:
        numPlayers=6
        for i in range(1,numPlayers+1):
            data.players.append(i)
        data.mode="players"

def chooseKeyPressed(event, data):
    pass

def chooseTimerFired(data):
    pass
    
def chooseRedrawAll(canvas, data):
    canvas.create_text(data.width/2,data.height/10,\
        text="Choose how many players you have.", \
        font="Times 20 bold")
    canvas.create_rectangle(data.xCoordsChoose,data.yCoordsChoose,\
        data.xCoordsChoose*2,data.yCoordsChoose*2,fill="green")
    canvas.create_text((data.xCoordsChoose+data.xCoordsChoose*2)/2,\
        (data.yCoordsChoose+data.yCoordsChoose*2)/2,text="3 players",\
        font="Times 25 bold")
    canvas.create_rectangle(data.xCoordsChoose*3,data.yCoordsChoose,\
        data.xCoordsChoose*4,data.yCoordsChoose*2,fill="blue")
    canvas.create_text((data.xCoordsChoose*3+data.xCoordsChoose*4)/2,\
        (data.yCoordsChoose+data.yCoordsChoose*2)/2,text="4 players",\
        font="Times 25 bold")
    canvas.create_rectangle(data.xCoordsChoose,data.yCoordsChoose*2.5,\
        data.xCoordsChoose*2,data.yCoordsChoose*3.5,fill="red")
    canvas.create_text((data.xCoordsChoose+data.xCoordsChoose*2)/2,\
        (data.yCoordsChoose*2.5+data.yCoordsChoose*3.5)/2,text="5 players",\
        font="Times 25 bold")
    canvas.create_rectangle(data.xCoordsChoose*3,data.yCoordsChoose*2.5,\
        data.xCoordsChoose*4,data.yCoordsChoose*3.5,fill="yellow")
    canvas.create_text((data.xCoordsChoose*3+data.xCoordsChoose*4)/2,\
        (data.yCoordsChoose*2.5+data.yCoordsChoose*3.5)/2,text="6 players",\
        font="Times 25 bold")

##players Mode##
def playersMousePressed(event, data):
    pass

def playersKeyPressed(event, data):
    if event.keysym=="k":
        data.players.remove(data.players[0])
    if event.keysym=="p":
        data.mode="gameScreen"
    pass
    
def playersTimerFired(data):
    pass
    
def playersRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/10, \
    text=("Player %d choose" % data.players[0]),font="Times 20 bold")
    

##gameScreen Mode##

def gameScreenMousePressed(event,data):
    pass
    
def gameScreenKeyPressed(event,data):
    if event.keysym=="Up":
        data.character.moveUp()
    if event.keysym=="Down":
        data.character.moveDown()
    if event.keysym=="Left":
        data.character.moveLeft()
    if event.keysym=="Right":
        data.character.moveRight()
    
def gameScreenTimerFired(data):
    pass
    
def gameScreenRedrawAll(canvas,data):
    canvas.create_image(0,0,anchor=NW,image=data.clueBoard)
    data.character.draw(canvas)

##Taken from:http://www.cs.cmu.edu/~112/notes/notes-animations-demos.html##
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
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
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
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

run(685, 650)