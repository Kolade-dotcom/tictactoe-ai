"""
Tic Tac Toe Player
"""

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
    x_count = sum([row.count(X) for row in board])
    o_count = sum([row.count(O) for row in board])

    if terminal(board):
        return None

    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))       
    if terminal(board):
        actions = None
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]
    if action is None:
        return new_board
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action: cell already filled")
    player_symbol = player(board)
    new_board[action[0]][action[1]] = player_symbol
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

        # check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
            
    # it is a tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not any(EMPTY in row for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        elif winner(board) == None:
            return 0
        
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    if p == X:
        value = float("-inf")
        optimal_action = None
        alpha = float("-inf")
        beta = float("inf")
        for action in actions(board):
            v = min_value(result(board, action), alpha, beta)
            if v > value:
                value = v
                optimal_action = action
            # Check for immediate win
            if value == 1:
                return optimal_action
            alpha = max(alpha, value)
        return optimal_action
    elif p == O:
        value = float("inf")
        optimal_action = None
        alpha = float("-inf")
        beta = float("inf")
        for action in actions(board):
            v = max_value(result(board, action), alpha, beta)
            if v < value:
                value = v
                optimal_action = action
            # Check for immediate win
            if value == -1:
                return optimal_action
            beta = min(beta, value)
        return optimal_action
    
    raise NotImplementedError


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    value = float("-inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value