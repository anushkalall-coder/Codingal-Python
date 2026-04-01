board = [' ']*10
wins=[(4,5,6),(1,2,3),(7,4,1),(7,8,9),(8,5,2),(9,6,3),(7,5,3),(1,5,9)]

def show():
    print(board[7]+'|'+board[8]+'|'+board[9]+'\n-+-+-\n'+board[4]+'|'+board[5]+'|'+board[6]+'\n-+-+-\n'+board[1]+'|'+board[2]+'|'+board[3])

while True:
    board=[' ']*10
    turn='X'
    for _ in range(9):
        show()
        m=int(input(f"{turn} move(1-9): "))
        if board[m]!=' ': continue
        board[m]=turn
        if any(board[a]==board[b]==board[c]!= 1' ' for a,b,c in wins):
            show(); print(turn, "wins"); break
        turn='O' if turn=='X' else 'X'
    else:
        show(); print("Tie")
    if input("Again? ").lower()!='y': break