# TIC-TAC-TOE AI
import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, 'O'):
        return -1
    elif check_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def ai_move(board):
    best_move = None
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'X'
        eval = minimax(board, 0, False, alpha, beta)
        board[move[0]][move[1]] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'O' if random.choice([True, False]) else 'X'

    print_board(board)

    while True:
        if current_player == 'O':
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'O'
            else:
                print("Invalid move. Try again.")
                continue
        else:
            row, col = ai_move(board)
            print(f"AI moves to ({row}, {col})")
            board[row][col] = 'X'

        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_tic_tac_toe()
