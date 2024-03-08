
def check(board, row, column, num):
    if num in board[row]:
        return False
    
        
    for i in range(9):
        if num == board[i][column]:
            return False


    #can either be 0, 3, 6
    box_row = (row//3)*3
    box_column = (column//3)*3

    #we check for the grid 
    for i in range(3):
        for j in range(3):
            if board[box_row+i][box_column+i]== num:
                return False
            
    return True

def solve(board, row=0, column=0):
    #if row is index 9, then we have filled every cell
    if row == 9:
      return True
    #if column is index 9, then move to next row and continue searching
    elif column == 9:
        return solve(board,row+1,0)
    #when we are searching, if the element is filled, then move to next element
    elif  board[row][column] != 0:
        return solve(board, row, column+1)
    else:

        #we check for each number 1 to 10
        for i in range (1,10):
            #if we can find a valid number, we set the number to that
            if check(board, row, column, i):
                board[row][column] = i
                #we use recursion to 

                #if we go to the next column, we keep continuing the recursion
                #when we break out, we should have our final board
                if solve(board, row, column + 1):

                    
                    return board
                
                #while we exit the recursive calls, if we want to go back, we should set the number back to 0
                board[row][column] = 0
                
        
        return False
    
    
sudoku = [[0,3,5,4,1,6,9,2,7],
 [0,9,0,8,5,0,0,0,1],
 [0,1,7,2,9,0,6,5,8],
 [0,6,9,1,3,4,7,8,2],
 [0,2,3,6,7,8,5,0,9],
 [0,4,0,5,2,9,1,6,3],
 [0,5,2,7,8,0,3,9,0],
 [0,8,1,3,4,5,2,7,6],
 [0,7,0,9,6,2,8,1,5]]

test = solve(sudoku,0,0)


for arr in test:
    print(arr)

