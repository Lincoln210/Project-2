def solve_CSP(input_dict):
    # YOUR CODE HERE. Do not change the name of the function
    """initializes csp from input_dict and starts the backtracking algorithm"""
    # initialize variables from the dictionary
    rows = input_dict["rows"]
    cols = input_dict["cols"]
    input_squares = input_dict["input_squares"]
    obstacles = input_dict["obstacles"]
    
    # sort list of squares by descending order of size
    squares = []
    for size, count in input_squares.items():
        for _ in range(count):
            squares.append((size, count))
            
    squares.sort(reverse = True)
    
    # initialize a matrix with empty spaces
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(None)
        matrix.append(row)
    
    # mark obstacles on the grid with an "X"
    placements = [] # list to track placements of squares
    for row, col in obstacles:
        matrix[row][col] = "X"
        
    # start backtracking
    if backtrack(matrix, squares, 0, placements):
        return placements # return list of placements for the squares
    else:
        return None # no solution found
    
def backtrack(matrix, squares, index, placements):
    """this is the main recursive backtracking function. it assigns values to variables and backtracks when necessary"""
    # base case where all squares have been placed
    if index == len(squares):
        return True
        
    # place the current square on the grid
    size, _ = squares[index]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_consistent(matrix, size, row, col):
                # insert the square
                insert_square(matrix, size, row, col, placements, True)
                # recurse with the next square
                if backtrack(matrix, squares, index + 1, placements):
                    return True # successful placement
                # backtrack and remove square because placement was not successful
                insert_square(matrix, size, row, col, placements, False)
                
    return False
    
def is_consistent(matrix, size, row, col):
    """check if a variable is consistent with constraints after assigning it a value"""
    # check if square is out of bounds or on an obstacle
    if row + size > len(matrix) or col + size > len(matrix[0]) or matrix[row][col] == "X":
        return False
    # check if square is on other squares
    for r in range(row, row + size):
        for c in range(col, col + size):
            if matrix[r][c] is not None: # overlap
                return False
    
    return True
    
def insert_square(matrix, size, row, col, placements, valid_placement):
    """if there is a valid placement, the square is either inserted or removed from the matrix"""
    # loop over the square within the matrix
    for r in range(row, row + size):
        for c in range(col, col + size):
            if valid_placement:
                matrix[r][c] = size # insert square by marking its size on the matrix
            else:
                matrix[r][c] = None # remove square
    
    if valid_placement:
        placements.append((size, row, col)) # mark valid placement of square
    else:
        placements.pop() # remove the last placement because the placement of the square is not valid