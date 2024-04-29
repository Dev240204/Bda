import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print(" ---- ")

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def minimax(board, depth, is_maximizing_player):
    scores = {'X': -1, 'O': 1, 'tie': 0}
    if is_winner(board, 'O'):
        return scores['O'] - depth
    if is_winner(board, 'X'):
        return scores['X'] + depth
    if is_board_full(board):
        return scores['tie']
    empty_cells = get_empty_cells(board)
    if is_maximizing_player:
        max_eval = float('-inf')
        for row, col in empty_cells:
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in empty_cells:
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    empty_cells = get_empty_cells(board)
    for row, col in empty_cells:
        board[row][col] = 'O'
        move_val = minimax(board, 0, False)
        board[row][col] = ' '
        if move_val > best_val:
            best_move = (row, col)
            best_val = move_val
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    opponent = 'O'
    print_board(board)
    while True:
        if player == 'X':
            position = int(input("Enter your move (1-9): "))
            row, col = divmod(position - 1, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                print_board(board)
                if is_winner(board, player):
                    print("You win!")
                    break
                elif is_board_full(board):
                    print("It's a tie!")
                    break
                player, opponent = opponent, player
            else:
                print("Invalid move. Try again.")
        else:
            print("Opponent's move:")
            row, col = best_move(board)
            board[row][col] = player
            print_board(board)
            if is_winner(board, player):
                print("Opponent wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
            player, opponent = opponent, player

if __name__ == "__main__":
    main()
