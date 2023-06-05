"""
Tic Tac Toe Player
"""

import math

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
    x_count = 0 
    o_count = 0
    if terminal(board):
        return None
    else:
        for row in board:
            for element in row:
                if element == 'O':
                    o_count = o_count +1
                elif element == 'X':
                    x_count = x_count +1
                
        if x_count > o_count:
            return 'O'
        elif x_count == 0 and o_count ==0 :
            return 'X'
        elif x_count < o_count:
            
            return 'X'
        
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    List = []
    
    if terminal(board):
        return None
    else:
        for index1,row in enumerate(board):
            for index, element in enumerate(row):
                if element == EMPTY:
                    List.append((index1,index))
    
    return List
        
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        return None
    else:
        gamer = player(board)
        board_copy = board
        board_copy[action[0]][action[1]] = gamer
        return board_copy
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == 'X' and row[1] == 'X' and row[2] =='X':
            return 'X'   
    transposed_board = [list(row) for row in zip(*board)]  
    for row in transposed_board:
        if row[0] == 'X' and row[1] == 'X' and row[2] == 'X' :
            return 'X'
        
    if board[0][0] == 'X' and board[1][1]== 'X' and board[2][2] == 'X':
        return 'X'
    
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
        
    for row in board:
        if row[0] == 'O' and row[1] == 'O' and row[2] =='O':
            return 'O'

    for row in transposed_board:
        if row[0] == 'O' and row[1] == 'O' and row[2] == 'O' :
            return 'O'
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'
    
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 'O'
        
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    print(board)
    for row in board:
        for i in range(len(row)):
            if row[i] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0
        
def max_value(board):
    if terminal(board):
        return utility(board)   
    
    v = float('-inf')
    
    for action in actions(board):
        if v < min_value(result(board, action)):
            v = min_value(result(board, action))
            opt_action = action
    return opt_action
        
def min_value(board):
    if terminal(board):
        return  utility(board)
    
    v = float('inf')
    
    for action in actions(board):
        if v > max_value(result(board, action)):
            v = max_value(result(board, action))
            opt_action = action
        
    return opt_action
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board) == 'X':
        return max_value(board)
    
    elif player(board) == 'O':
        return min_value(board)
        
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
