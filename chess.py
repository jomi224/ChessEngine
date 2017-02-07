from copy import*
from time import*
from graphics import*
from random import*  
def is_checked(board,enemy,side):
    if side=="w":
        king=board.index("wk")
    else:
        king=board.index("bk")
    for i in enemy:
        for j in move_options(board,i,True):
            if j==king:
                return True
    return False
def out_of_check(l1,moves,white,black,board):
    options=[]
    for i in moves:
        c1=board[:]
        c2=white[:]
        c3=black[:]
        side=c1[l1][0]
        move(l1,i,c1,c2,c3)
        if side=="w":
            if not is_checked(c1,c3,"w"):
                options.append(i)
        else:
            if not is_checked(c1,c2,"b"):
                options.append(i)
    return options
        
def move(l1,l2,board,white,black):
    side=board[l1][0]
    if board[l2]!="e":
        if board[l2][0]=="b":
            black.remove(l2)
        else:
            white.remove(l2)
    if side=="w":
        white.remove(l1)
        white.append(l2)
    else:
        black.remove(l1)
        black.append(l2)
    board[l2]=board[l1]
    board[l1]="e"

def computer_move3(board,black,white,layer):
    moves=[]
    for i in black:
        for j in move_options(board,i,False):
            moves.append([rate_move(i,j,board,black,white),i,j])
    maxi=-1000
    maxvalue=[]
    for i in moves:
        a=mini(board,i,black,white,layer,maxi)
        if a>maxi:
            maxi=a
            maxvalue=[i]
        elif a==maxi:
            maxvalue.append(i)
    num=randrange(0,len(maxvalue))
    move(maxvalue[num][1],maxvalue[num][2],board,white,black)
def mini(board,moves,black,white,layer,highest):
    if layer==1:
        boardcopy=copy(board)
        blackcopy=copy(black)
        whitecopy=copy(white)
        move(moves[1],moves[2],boardcopy,whitecopy,blackcopy)
        mini=-500
        for i in whitecopy:
            for j in move_options(boardcopy,i,False):
                a=rate_move(i,j,boardcopy,blackcopy,whitecopy)
                c=moves[0]-a
                if c<highest:
                    return c
                if c>mini:
                    mini=c
        return mini
def computer_move2(board,black,white):
    moves=[]
    for i in black:
        for j in move_options(board,i,False):
            moves.append([i,j])
    maxi=-10
    maxvalue=[]
    for i in moves:
        a=rate_move(i[0],i[1],board,black,white)
        if a>maxi:
            maxi=a
            maxvalue=i
    move(maxvalue[0],maxvalue[1],board,white,black)
def computer_move1(board,black,white):
    moves=[]
    for i in black:
        for j in move_options(board,i,False):
            moves.append([i,j])
    move1=moves[randrange(0,len(moves))]
    move(move1[0],move1[1],board,white,black)
def rate_move(l1,l2,board,black,white):
    movevalue=0
    side=board[l1][0]
    if side=="w":
        enemy="b"
    else:
        enemy="w"
    if board[l2][0]==enemy:
        if board[l2][1:]=="p":
            movevalue+=1
        elif board[l2][1:]=="kn" or board[l2][1:]=="b":
            movevalue+=3
        elif board[l2][1:]=="r":
            movevalue+=5
        elif board[l2][1:]=="q":
            movevalue+=8
    if l2==8*3+3 or l2==8*4+3 or l2==8*3+4 or l2==8*4+4:
        movevalue+=2
    if side=="w" and l1<16 or side=="b" and l1>64-16:
        movevalue+=2
    return movevalue
def move_options(board,location,checking):
    y=location//8
    x=location%8    
    if board[location][0]=="b":
        side="b"
        enemy="w"
        direction=-1
    else:
        enemy="b"
        side="w"
        direction=1    
    if board[location]=="bp" or board[location]=="wp":        
        options=[]
        if board[location][0]=="b" and y<7 or board[location][0]=="w" and y>0:
            if board[x+(y+direction)*8]=="e":
                options.append(x+(y+direction)*8)
                if side=="w" and location//8==1 or side=="b" and location//8==6:
                    if board[x+(y+2*direction)*8]=="e":
                        options.append(x+(y+direction+direction)*8)
        if x>0:
            if board[x-1+8*(y+direction)][0]==enemy:
                options.append(x-1+8*(y+direction))
        if x<7:
            if board[x+1+8*(y+direction)][0]==enemy:
                options.append(x+1+8*(y+direction))      
        if not checking:
            return out_of_check(location,options,white,black,board)
        else:
            return options
    if board[location]=="wr" or board[location]=="br":
        options=[]
        i=0
        d=[True,True,True,True]
        while True:
            i+=1
            if d[0]:
                if location+8*i<64:
                    if board[location+8*i][0]==side:
                        d[0]=False
                    elif board[location+8*i][0]==enemy:
                        d[0]=False
                        options.append(location+8*i)
                    else:
                        options.append(location+8*i)
                else:
                    d[0]=False
            if d[1]:
                if location-8*i>=0:
                    if board[location-8*i][0]==side:
                        d[1]=False
                    elif board[location-8*i][0]==enemy:
                        d[1]=False
                        options.append(location-8*i)
                    else:
                        options.append(location-8*i)
                else:
                    d[1]=False
            if d[2]:
                if (location+i)%8!=0:
                    if board[location+i][0]==side:
                        d[2]=False
                    elif board[location+i][0]==enemy:
                        d[2]=False
                        options.append(location+i)
                    else:
                        options.append(location+i)
                else:
                    d[2]=False
            if d[3]:
                if (location-i)%8!=7:
                    if board[location-i][0]==side:
                        d[3]=False
                    elif board[location-i][0]==enemy:
                        d[3]=False
                        options.append(location-i)
                    else:
                        options.append(location-i)
                else:
                    d[3]=False
            if not d[1] and not d[2] and not d[3] and not d[0]:
                if not checking:
                    return out_of_check(location,options,white,black,board)
                else:
                    return options
    if board[location]=="wkn" or board[location]=="bkn":
        options=[]
        moves=[]
        #add moves
        if not checking:
            return out_of_check(location,options,white,black,board)
        else:
            return options
    if board[location]=="wk" or board[location]=="bk":
        options=[]
        if location%8<7:
            options.append(location+1)
            if location+9<64:
                options.append(location+9)
            if location-7>=0:
                options.append(location-7)
        if location%8>0:
            options.append(location-1)
            if location+7<64:
                options.append(location+7)
            if location-9>=0:
                options.append(location-9)
        if location+8<64:
            options.append(location+8)
        if location-8>=0:
            options.append(location-8)
        real=[]
        for i in options:
            if board[i][0]!=side:
                real.append(i)
        if not checking:
            return out_of_check(location,real,white,black,board)
        else:
            return real
    if board[location]=="wq" or board[location]=="bq":
        d=[True,True,True,True,True,True,True,True]
        i=0
        options=[]
        while True:
            i+=1
            if d[0]:
                if location+8*i<64:
                    if board[location+8*i][0]==side:
                        d[0]=False
                    elif board[location+8*i][0]==enemy:
                        d[0]=False
                        options.append(location+8*i)
                    else:
                        options.append(location+8*i)
                else:
                    d[0]=False
            if d[1]:
                if location-8*i>=0:
                    if board[location-8*i][0]==side:
                        d[1]=False
                    elif board[location-8*i][0]==enemy:
                        d[1]=False
                        options.append(location-8*i)
                    else:
                        options.append(location-8*i)
                else:
                    d[1]=False
            if d[2]:
                if (location+i)%8!=0:
                    if board[location+i][0]==side:
                        d[2]=False
                    elif board[location+i][0]==enemy:
                        d[2]=False
                        options.append(location+i)
                    else:
                        options.append(location+i)
                else:
                    d[2]=False
            if d[3]:
                if (location-i)%8!=7:
                    if board[location-i][0]==side:
                        d[3]=False
                    elif board[location-i][0]==enemy:
                        d[3]=False
                        options.append(location-i)
                    else:
                        options.append(location-i)
                else:
                    d[3]=False
            if d[4]:
                if location+9*i<64 and (location+i)%8!=0:
                    if board[location+9*i][0]==side:
                        d[4]=False
                    elif board[location+9*i][0]==enemy:
                        d[4]=False
                        options.append(location+9*i)
                    else:
                        options.append(location+9*i)
                else:
                    d[4]=False
            if d[5]:
                if location+7*i<64 and (location-i)%8!=7:
                    if board[location+7*i][0]==side:
                        d[5]=False
                    elif board[location+7*i][0]==enemy:
                        d[5]=False
                        options.append(location+7*i)
                    else:
                        option.s.append(location+7*i)       
                else:
                    d[5]=False
            if d[6]:
                if location-9*i>=0 and (location+i)%8!=7:
                    if board[location-9*i][0]==side:
                        d[6]=False
                    elif board[location-9*i][0]==enemy:
                        d[6]=False
                        options.append(location-9*i)
                    else:
                        options.append(location-9*i)
                else:
                    d[6]=False
            if d[7]:
                if location-7*i>=0 and (location+i)%8!=0:
                    if board[location-7*i][0]==side:
                        d[7]=False
                    elif board[location-7*i][0]==enemy:
                        d[7]=False
                        options.append(location-7*i)
                    else:
                        options.append(location-7*i)  
                else:
                    d[7]=False
            if not True in d:
                if not checking:
                    return out_of_check(location,options,white,black,board)     
                else:
                    return options
    if board[location]=="wb" or board[location]=="bb":
        d=[True,True,True,True]
        i=0
        options=[]
        while True:
            i+=1
            if d[0]:
                if location+9*i<64 and (location+i)%8!=0:
                    if board[location+9*i][0]==side:
                        d[0]=False
                    elif board[location+9*i][0]==enemy:
                        d[0]=False
                        options.append(location+9*i)
                    else:
                        options.append(location+9*i)
                else:
                    d[0]=False
            if d[1]:
                if location+7*i<64 and (location-i)%8!=7:
                    if board[location+7*i][0]==side:
                        d[1]=False
                    elif board[location+7*i][0]==enemy:
                        d[1]=False
                        options.append(location+7*i)
                    else:
                        options.append(location+7*i)       
                else:
                    d[1]=False
            if d[2]:
                if location-9*i>=0 and (location-i)%8!=7:
                    if board[location-9*i][0]==side:
                        d[2]=False
                    elif board[location-9*i][0]==enemy:
                        d[2]=False
                        options.append(location-9*i)
                    else:
                        options.append(location-9*i)
                else:
                    d[2]=False
            if d[3]:
                if location-7*i>=0 and (location+i)%8!=0:
                    if board[location-7*i][0]==side:
                        d[3]=False
                    elif board[location-7*i][0]==enemy:
                        d[3]=False
                        options.append(location-7*i)
                    else:
                        options.append(location-7*i)  
                else:
                    d[3]=False
            if not d[1] and not d[0] and not d[3] and not d[2]:
                if not checking:
                    return out_of_check(location,options,white,black,board)
                else:
                    return options
    print(location,checking, board)
            
class Board:
    def __init__(self,win):
        self.win=win
        board=[[0 for i in range(8)] for j in range(8)]
        self.pieces=[[0 for i in range(8)] for j in range(8)]
        self.labels=[[0 for i in range(8)] for j in range(8)]
        self.captions=Text(Point(260,50),"")
        self.captions.draw(win)
        self.txt=""
        for i in range(8):
            for j in range(8):
                board[i][j]=Rectangle(Point(20+60*i,100+60*j),Point(80+60*i,160+60*j))
                board[i][j].draw(win)
                self.pieces[i][j]=Circle(board[i][j].getCenter(),30)
                self.labels[i][j]=Text(board[i][j].getCenter(),"")
                if (i+j)%2==0:
                    board[i][j].setFill("black")
                else:
                    board[i][j].setFill("white")
    def click(self,point):
        x=(point.getX()-20)//60
        y=(point.getY()-100)//60
        return int(y*8+x)
    def draw_board(self,board1):
        for i in range(8):
            for j in range(8):
                try:
                    self.pieces[i][j].undraw()
                    self.labels[i][j].undraw()
                except:
                    a=0
        self.captions.setText(self.txt)
        for i in range(len(board1)):
            if board1[i][0]!="e":
                if board1[i][0]=="w":
                    color="white"
                    enemy="black"
                else:
                    color="black"
                    enemy="white"
                self.pieces[i%8][i//8].draw(self.win)
                self.pieces[i%8][i//8].setFill(color)
                self.pieces[i%8][i//8].setOutline(enemy)
                self.labels[i%8][i//8].draw(self.win)
                self.labels[i%8][i//8].setText(board1[i][1:])
                self.labels[i%8][i//8].setTextColor(enemy)
    
board=["wr","wb","wkn","wq","wk","wkn","wb","wr"]+["wp" for i in range(8)]+["e" for i in range(8)]*4+["bp" for i in range(8)]+["br","bb","bkn","bq","bk","bkn","bb","br"]
white=[i for i in range(16)]
black=[63-i for i in range(16)]
win=GraphWin("Chess",520, 600)
win.setCoords(0,0,520,600)
a=Board(win)
turn="w"
game=True
while game:
    a.draw_board(board)
    decision=False
    while not decision:
        p=a.click(win.getMouse())
        if 0<=p<64:
            if board[p][0]==turn:
                p2=a.click(win.getMouse())
                print(p2)
                if 0<=p2<64:
                    if p2 in move_options(board,p,False):
                        move(p,p2,board,white,black)
                        decision=True
    if is_checked(board,white,"b"):
        a.txt="CHECK!!!"
    a.draw_board(board)
    sleep(2)
    computer_move3(board,black,white,1)
    a.txt=""
    if is_checked(board,black,"w"):
        a.txt="CHECK!!!"
win.close()