x='X'
o='O'
EMPTY=' '
NUM_SQUARES=9
played_moves=[]
board=[]
c=0
def instructions():
    print("Tic tac toe game.\nPlayer 1 is always the first to move and he gets 'X' by default")
    print('The game board is: \n')
    print(0 ,'|', 1, '|' ,2)
    print(3, '|' ,4, '|', 5)
    print(6, '|' ,7, '|', 8)
    print("The numbers in the squares represent the respective squares")
def create_board():
     for square in range(NUM_SQUARES):
        board.append(EMPTY)
def display_board():
    print('The game board is: \n')
    print(board[0] ,'|', board[1], '|' ,board[2])
    print(board[3], '|' ,board[4], '|', board[5])
    print(board[6], '|' ,board[7], '|', board[8])
def legal_move(n):
    if(n<0):
        print('That is not possible!!!')
        return 1
    elif(n>=9):
        print('That is not possible!!!')
        return 1
    elif(n in played_moves):
        print('This square is already occupied!Please try another move.')
        return 1
    else:
        return 0
def check_result():
    if(board[0]==x and board[1]==x and board[2]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[0]==x and board[3]==x and board[6]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[0]==x and board[4]==x and board[8]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[1]==x and board[4]==x and board[7]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[2]==x and board[5]==x and board[8]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[2]==x and board[4]==x and board[6]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[3]==x and board[4]==x and board[5]==x):
        print("Congrats Player 1.You win!!!")
        return 1
    elif(board[6]==x and board[7]==x and board[8]==x):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[0]==o and board[1]==o and board[2]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[0]==o and board[3]==o and board[6]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[0]==o and board[4]==o and board[8]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[1]==o and board[4]==o and board[7]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[2]==o and board[5]==o and board[8]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[2]==o and board[4]==o and board[6]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[3]==o and board[4]==o and board[5]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    elif(board[6]==o and board[7]==o and board[8]==o):
        print("Congrats Player 2.You win!!!")
        return 1
    else:
        if(board[0]!=EMPTY and board[1]!=EMPTY and board[2]!=EMPTY and board[3]!=EMPTY and board[4]!=EMPTY and board[5]!=EMPTY and board[6]!=EMPTY and board[7]!=EMPTY and board[8]!=EMPTY):
            print("The game is a draw!!!")
            return 1
def move():
    while(1):
        while(1):
            p1=int(input('\nPlayer 1 enter the square where you want to place X: '))
            check_move=legal_move(p1)
            if(check_move==0):
                board[p1]=x
                played_moves.append(p1)
                display_board()
                c=check_result()
                break
        if(c==1):
            break
        while(1):
            p2=int(input('\nPlayer 2 enter the square where you want to place O: '))
            check_move=legal_move(p2)
            if(check_move==0):
                board[p2]=o
                played_moves.append(p2)
                display_board()
                c=check_result()
                break
        if(c==1):
            break
def main():
    instructions()
    create_board()
    move()

main()
    
    
    
    
    
    


