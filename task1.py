import math

b = [' '] * 9

def show():
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")

def win(p):
    return any(all(b[i]==p for i in c) for c in
        [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def mini(maxi):
    if win('O'): return 1
    if win('X'): return -1
    if ' ' not in b: return 0
    best = -math.inf if maxi else math.inf
    for i in range(9):
        if b[i]==' ':
            b[i]='O' if maxi else 'X'
            s = mini(not maxi)
            b[i]=' '
            best = max(best,s) if maxi else min(best,s)
    return best

def ai():
    m = max((mini(False), i) for i in range(9) if b[i]==' ')[1]
    b[m] = 'O'

while True:
    show()
    b[int(input("Move (1-9): "))-1] = 'X'
    if win('X'): show(); print("You win"); break
    if ' ' not in b: print("Draw"); break
    ai()
    if win('O'): show(); print("AI wins"); break
