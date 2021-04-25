board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ' '

def boardlayout(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isboardfull(board):
    if board.count(' ') > 1:
        return False 
    else:
        return True

def iswinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or              
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or             
    (b[3] == l and b[5] == l and b[7] == l))

def playermove():
    run = True
    while run:
        move = input("Please select a position to enter the X b\w 1-9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                 run = False
                 insertLetter('X' , move)
                else:
                    print('Sorry this space is occupied')
            else:
                print("Please enter a number b\w 1 and 9: ")
        except:
            print("Please type a number :")

def computerMove(): #ai
    possiblemoves = [x for x , letter in enumerate(board) if letter == '' and X != 0]
    move = 0

    for let in ['0' , 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(boardcopy, let):
                move = i
                return move

        
