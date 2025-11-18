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
    if board == initial_state():
        return X
    count = 0

    for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                count += 1
                
    #If the amount of empty tiles is even, is is O. Else, it is X
    if count % 2 == 0:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    new_board = copy.deepcopy(board)
    if action[0] > len(board) or action[0] < 0 or action[1] > len(board) or action[1] < 0:
        raise Exception("Move Invalid")
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = current_player
    else:
        raise Exception("Move Invalid")
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Checks for horizontal win
    for i in range(len(board)):
        if all(ele == board[i][0] for ele in board[i]) and not board[i][0] == EMPTY:
            return board[i][0]
        
    #Checks for vertical win
    for i in range(len(board)):
        if all(board[j][i] == board[0][i] for j in range(len(board[i]))) and not board[0][i] == EMPTY:
            return board[0][i]
        
    #Checks for left diagonal win
    if all(board[i][i] == board[0][0] for i in range (len(board))) and not board[0][0] == EMPTY:
        return board[0][0]
    
    #Checks for right diagonal win
    if all(board[i][len(board) - i - 1] == board[0][len(board) - 1] for i in range (len(board))) and not board[0][len(board) - 1] == EMPTY:
        return board[0][len(board) - 1]
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Check for terminal position
    if terminal(board):
        return None
    best_move = ()

    #Check whoes turn it is
    if player(board) == X:
        max_val = -math.inf

        #Iterate over possible actions
        for action in actions(board):
            temp = min_value(result(board, action))
            if temp > max_val:
                max_val = temp
                best_move = action
    else:
        min_val = math.inf

        #Iterate over possible actions
        for action in actions(board):
            temp = max_value(result(board, action))
            if temp < min_val:
                min_val = temp
                best_move = action

    #Return calculated move
    return best_move


def max_value(board):

    #Check for terminal position, and return the utility of the position
    if terminal(board):
        return utility(board)
    
    #Iterate recursivly over possible positions, and return with the best possible path
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):

    #Check for terminal position, and return the utility of the position
    if terminal(board):
        return utility(board)
    
    #Iterate recursivly over possible positions, and return with the best possible path
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value

        
        
