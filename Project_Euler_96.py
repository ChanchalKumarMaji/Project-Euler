import copy

board=[]


for i in range(9):
    row=input()
    board.append(row)

#board=['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300']


def main():
    global board
    for idx,line in enumerate(board):
        board[idx] = list(line)
        
    solve()
    printBoard()
    
       
def solve():
    global board
    
    try:
        fillAllObvious()
    except:
        return False
    
    if isComplete():
        return True
    
    i,j = 0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == "0":
                i,j = rowIdx, colIdx
                
    possibilities = getPossibilities(i,j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
    
        board[i][j] = value
        result = solve()
        if result == True:
            return True
        else:
            board = copy.deepcopy(snapshot)
            
    return False

def fillAllObvious():
    global board
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities(i,j)
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    somethingChanged = True
                    
        if somethingChanged == False:
            return
                
def getPossibilities(i,j):
    global board
    if board[i][j] != "0":
        return False
        
    possibilities = {str(n) for n in range(1,10)}
    
    for val in board[i]:
        possibilities -= set(val)
        
    for idx in range(0,9):
        possibilities -= set( board[idx][j] )
        
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
    
    subboard = board[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]
    
    for row in subboard:
        for col in row:
            possibilities -= set(col)
            
    return list(possibilities)

def printBoard():
    global board
    for row in board:
        for col in row:
            print(col, end="")
        print("")
        
def isComplete():
    for row in board:
        for col in row:
            if (col == "0"):
                return False
                
    return True
    
main()
