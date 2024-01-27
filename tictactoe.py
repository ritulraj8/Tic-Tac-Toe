board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
print("******TIC TAC TOE******")
currentplayer = "X"
winner = None
gamerunning = True
print("1"+" | "+"2"+" | "+"3")
print("----------")
print("4"+" | "+"5"+" | "+"6")
print("----------")
print("7"+" | "+"8"+" | "+"9")
print("\n")
ch="Y"

def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def playerinput(board):
    while True:
        take = int(input("Enter a number between 1 and 9: "))
        if take > 9 or take <= 0:
            print("Invalid Input. Please enter a number between 1 and 9.")
        else:
            if board[take - 1] == "-":
                board[take - 1] = currentplayer
                break
            else:
                print("Already occupied. Please choose an empty position.")


def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[4]
        return True
    
def checkvertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkwin(board):
    global gamerunning
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        printboard(board)
        print("The winner is",winner)
        gamerunning = False

def checktie(board):
    global gamerunning
    if "-" not in board:
        print("It is a tie")
        gamerunning=False

def Switch():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "0"
    else:
        currentplayer = "X"
while ch=="y" or ch=="Y":
 gamerunning=True
 while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    Switch()
    if gamerunning==False:
        print("\n")
        print("Do you want to play again: ")
        print("Enter 'Y' for yes and 'N'for no: ")
        print("\n")
        ch=input("")
        board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
    

        
    
