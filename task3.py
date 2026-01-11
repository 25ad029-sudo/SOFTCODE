import math

board = [' ']*9

def is_winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==p for a,b1,c in wins)

def minimax(b, is_max):
    if is_winner(b, 'O'):
        return 1
    if is_winner(b, 'X'):
        return -1
    if ' ' not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                best = max(best, minimax(b, False))
                b[i]=' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                best = min(best, minimax(b, True))
                b[i]=' '
        return best