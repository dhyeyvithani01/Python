# Chess Game (Basic Version)
# This code represents a simple text-based chess game without advanced features.
# You can expand it later to include castling, en passant, pawn promotion, and checkmate detection.

# Define the board setup with uppercase for white pieces and lowercase for black pieces.
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black pieces
    ["p", "p", "p", "p", "p", "p", "p", "p"],  # Black pawns
    [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
    [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
    [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
    [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
    ["P", "P", "P", "P", "P", "P", "P", "P"],  # White pawns
    ["R", "N", "B", "Q", "K", "B", "N", "R"]   # White pieces
]

# Print the board in a readable format
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Convert board positions (like 'a2', 'h8') to matrix indices (row, col)
def position_to_indices(pos):
    col, row = pos
    col = ord(col) - ord('a')  # Convert letter to column index
    row = 8 - int(row)  # Convert number to row index
    return row, col

# Convert matrix indices (row, col) to board positions (like 'a2', 'h8')
def indices_to_position(row, col):
    return chr(col + ord('a')) + str(8 - row)

# Check if a move is within the board's boundaries
def is_valid_position(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Move a piece on the board
def move_piece(start, end, board):
    start_row, start_col = position_to_indices(start)
    end_row, end_col = position_to_indices(end)

    if not is_valid_position(end_row, end_col):
        print("Invalid move. Position out of bounds!")
        return False

    piece = board[start_row][start_col]
    
    if piece == " ":
        print("Invalid move. No piece at starting position!")
        return False
    
    # Make the move
    board[end_row][end_col] = piece
    board[start_row][start_col] = " "
    return True

# Main function that runs the game
def main():
    current_turn = "white"  # White starts
    game_over = False

    while not game_over:
        print_board(board)
        print(f"{current_turn.capitalize()}'s turn")

        start_pos = input("Enter the start position (e.g., 'e2'): ").lower()
        end_pos = input("Enter the end position (e.g., 'e4'): ").lower()

        if len(start_pos) != 2 or len(end_pos) != 2:
            print("Invalid input. Please enter valid positions (e.g., 'e2').")
            continue

        if not (start_pos[0].isalpha() and start_pos[1].isdigit() and
                end_pos[0].isalpha() and end_pos[1].isdigit()):
            print("Invalid input. Please enter valid positions (e.g., 'e2').")
            continue

        if move_piece(start_pos, end_pos, board):
            # Switch turns
            current_turn = "black" if current_turn == "white" else "white"
        else:
            print("Invalid move. Try again.")

        # Check for checkmate, stalemate, etc. (basic check for now)
        # You can expand this to detect checkmate, stalemate, or draw conditions later.

# Run the game
if __name__ == "__main__":
    main()
