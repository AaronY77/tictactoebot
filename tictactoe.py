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
    first=0
    second=0
    for x in board:
        for y in x:
            if y==X:
                first+=1
            if y==O:
                second+=1
    if first<=second:
        return X
    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    output=set()
    row=1
    for x in range (0,3):
        cell=1
        for y in range(0,3):
            
            if board[row][cell]==EMPTY:
                output.add((row,cell))
            cell = 0 if cell==2 else cell+1
        row = 0 if row==2 else row+1

    return output
            
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    output=copy.deepcopy(board)
    if not board[action[0]][action[1]]==EMPTY:
        print(str(board)+str(action))
        raise Exception
    else:
        output[action[0]][action[1]]=player(board)
    return output
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row=0
    while(row<3):
        if board[row][0]==board[row][1]==board[row][2]:
            return board[row][0]
        row+=1
    cell=0
    while(cell<3):
        if (board[0][cell]==board[1][cell]==board[2][cell]):
            return board[0][cell]
        cell+=1
    if (board[0][0]==board[1][1]==board[2][2]) | (board[0][2]==board[1][1]==board[2][0]):
            return board[1][1]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board) == None:
        return True
    for row in board:
        for cell in row:
            if cell==EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ=winner(board)
    return 1 if champ==X else -1 if champ==O else 0
    raise NotImplementedError

def minimax (board):
    actAndScores=set()
    for action in actions(board):
        actioned=result(board,action)
        actAndScores.add((action,minimaxhelper(actioned)))
    if player(board)==X:
        max=((0,0),-10)
        for act,score in actAndScores:
            if act==(1,1):
                score+=0.01
            if score>max[1]:
                max=(act,score)
        return max[0]
    else:
        min=((0,0),10)
        for act,score in actAndScores:
            if act==(1,1):
                score-=0.01
            if score<min[1]:
                min=(act,score)
        return min[0]
        




                
        
        


def minimaxhelper(board2):
    """
    Returns the optimal action for the current player on the board.
    """
    moveValues=set()
    if terminal(board2):
        return utility(board2)
    
    else: 
        for action in actions(board2):
            moveValues.add(minimaxhelper(result(board2,action)))
    if player(board2)==X:
        max=-10
        
        for score in moveValues:
            if score>max:
                max=score
        return max
    else:
        min =10
        
        for score in moveValues:
            if score<min:
                min=score
        return min

    
            
    
    raise NotImplementedError
