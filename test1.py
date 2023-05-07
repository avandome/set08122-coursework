import random
import copy

def create_board():
    # Create an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Fill in the diagonal boxes
    for i in range(0, 9, 3):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = nums.pop()
    
    # Fill in the rest of the board
    solve_board(board)
    
    return board

def is_valid(board, num, row, col):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                continue
            num = int(board[i][j])
            for k in range(9):
                # check row
                if k != j and board[i][k] == num:
                    return False
                # check column
                if k != i and board[k][j] == num:
                    return False
            # check region
            region_x = (j // 3) * 3
            region_y = (i // 3) * 3
            for x in range(region_x, region_x + 3):
                for y in range(region_y, region_y + 3):
                    if x != j and y != i and board[y][x] == num:
                        return False
    return True





    # Check row
   # for i in range(9):
    #    if board[row][i] == num:
     #       return False
        
    # Check column
    #for i in range(9):
     #   if board[i][col] == num:
      #      return False
        
    # Check 3x3 box
    #box_row = (row // 3) * 3
    #box_col = (col // 3) * 3
    #for i in range(box_row, box_row + 3):
     #   for j in range(box_col, box_col + 3):
      #      if board[i][j] == num:
       #         return False
            
    #return True

def solve_board(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try each number in the cell
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        # Recursively solve the rest of the board
                        if solve_board(board):
                            return True
                        # Backtrack if the board cannot be solved
                        board[row][col] = 0
                return False
    return True
    
def print_board(board):
    print("   123 456 789")
    print("  +---+---+---+")
    for i in range(9):
        row = chr(ord('A') + i) + " |"
        for j in range(9):
            if board[i][j] == 0:
                row += " "
            else:
                row += str(board[i][j])
            if j % 3 == 2:
                row += "|"
            else:
                row += ""
        print(row)
        if i%3==2:
            print("  +---+---+---+")


def remove_numbers(board, num_to_remove):
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)
    for row, col in cells:
        value = board[row][col]
        board[row][col] = 0
        solutions = get_solutions(copy.deepcopy(board))
        num_solutions = len(solutions)
        if num_solutions != 1:
            board[row][col] = value
        else:
            num_to_remove -= 1
            if num_to_remove == 0:
                break
    return board



def get_solutions(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try each number in the cell
                solutions = []
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        # Recursively solve the rest of the board
                        if solve_board(board):
                            solutions.append([row, col, num])
                # Backtrack if the board cannot be solved
                board[row][col] = 0
                return solutions
    return [[]] 


# Test the functions
#board = create_board()
#remove_numbers(board, 30)
#print_board(board)
