import test1

board = test1.create_board()

#num_to_remove = 30
#test1.remove_numbers(board, num_to_remove)

#undo_board = [row[:] for row in board]

#test1.print_board(board)


def welcome_page():
    instructions = """The goal of sudoku is simple: fill in the numbers 1-9 exactly once in every row, column, and 3x3 region.
    For this program, choose a difficulty and the program will generate a board of that difficulty.
    Next, follow the on screen prompts to input the row identifier (A-I), then the column identifier (1-9), and finally the number that you wish to place there.
    The program will then print your updated board for you to repeat the steps until you are finished playing.
    Enjoy!

    """
    print("  _______________________ ")
    print(" |  ___________________  |")
    print(" | | Welcome to Sudoku | |")
    print(" | |___________________| |")
    print(" |_______________________|")

    while True:
        print("Press 'e' to play an easy game")
        print("Press 's' to play a standard game")
        print("Press 'h' to play a hard game")
        print("Press 'i' for how to play")
        print("Press 'q' to quit")
        welcome_choice = input("Enter your choice: ").strip().lower()
        if welcome_choice == 'e':
            num_to_remove = 1
            break
        elif welcome_choice == 's':
            num_to_remove = 28
            break
        elif welcome_choice == 'h':
            num_to_remove = 37
            break
        elif welcome_choice == 'i':
            print(instructions)
            continue
        elif welcome_choice == 'q':
            exit()
        else:
            print("Invalid input, try again")
            continue
    test1.remove_numbers(board, num_to_remove)

def play_game():
    
    while True:
        # Get user input
        row_input = input("Enter row (A-I): ").strip().upper()
        if row_input not in "ABCDEFGHI" or len(row_input) !=1:
            print("Invalid input, try again")
            continue
        col_input = input("Enter column (1-9): ")
        if col_input not in "123456789" or len(col_input) !=1:
            print("Invalid input, try again")
            continue
        num_input = input("Enter number (1-9): ")
        if num_input not in "123456789" or len(num_input) !=1:
            print("Invalid input, try again")
            continue
    
        # Convert user input to row and column indices
        row = ord(row_input) - ord('A')
        col = int(col_input) - 1
        num = int(num_input)
    
    
        # Check if the space is empty
        if board[row][col] != 0:
            print("Space is already filled, please choose another space")
            continue
    
        # Fill in the space with the user's number
        board[row][col] = num
    
        # Print the updated board
        test1.print_board(board)


        board_full = True
        for row in board:
            for cell in row:
                if cell == '0':
                    board_full = False
                    break
            if not board_full:
                break



        # If the board is full, check if it's valid and print the end message
        if board_full:
            if test1.is_valid(board, num, row, col):
                print("Congratulations! You have solved the puzzle!")
            else:
                print("Sorry, the board is not valid.")
            break


welcome_page()
test1.print_board(board)
play_game()
