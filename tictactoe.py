"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_sum = 0
    O_sum = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                X_sum += 1
            elif board[i][j] == 'O':
                O_sum += 1
    
    if X_sum == O_sum:
        return 'X'
    elif X_sum > O_sum:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] == EMPTY:
        actual_player = player(board)
        new_state = copy.deepcopy(board)
        new_state[i][j] = actual_player
        return new_state
    else:
        raise Exception("Something wrong")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            return 'X'
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return 'O'
        
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'X'
        if board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'O'
    
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 'X'
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return 'O'
    
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X'
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O'
    
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == 'X':
        best_value = -math.inf
        best_move = (-1, -1)

        for action in actions(board):
            new_best_value = get_min_value(result(board, action))
            if new_best_value == 1:
                best_move = action
                break
            if new_best_value > best_value:
                best_value = new_best_value
                best_move = action
        return best_move
    
    if player(board) == 'O':
        best_value = math.inf
        best_move = (-1, -1)

        for action in actions(board):
            new_best_value = get_max_value(result(board, action))
            if new_best_value == -1:
                best_move = action
                break
            if new_best_value < best_value:
                best_value = new_best_value
                best_move = action
        return best_move


def get_max_value(board):
    if terminal(board):
        return utility(board)
    best_value = -math.inf
    for action in actions(board):
        best_value = max(best_value, get_min_value(result(board, action)))
        if best_value == 1:
            break
    return best_value


def get_min_value(board):
    if terminal(board):
        return utility(board)
    best_value = math.inf
    for action in actions(board):
        best_value = min(best_value, get_max_value(result(board, action)))
        if best_value == -1:
            break
    return best_value
